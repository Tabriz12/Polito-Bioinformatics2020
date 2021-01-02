import argparse
from collections import defaultdict



class CommandLine:
	def __init__(self):
		self._parser = argparse.ArgumentParser()
		self._parser.add_argument("file_1")
		self._parser.add_argument("file_2")
		self._parser.add_argument("file_write")
		self._parser.add_argument("-common", "--common", type=int)
		self._args = self._parser.parse_args()
	
	@property
	def args(self):
		return self._args
	
class Docs:
	def __init__(self, file_1, file_2, file_write, common=None):
		self.file_1 = file_1
		self.file_2 = file_2
		self.file_write = file_write
		self.common = common
	
	def read_file(self, file):
		data = defaultdict(str)
		with open(file, "r") as f:
			for i, line in enumerate(f):
				if(line.startswith(">")):
					keyname=line[1:-1]
				else:
					data[keyname]+=line[:-1] # in case sequence is more than one line
		
		return data
	
	def compare(self, file_1, file_2):
		data_1 = self.read_file(file_1)
		data_2 = self.read_file(file_2)
		matched=[] #Sets aren't faster than lists in general -- membership test is faster for sets, and so is removing an element. 
				   #As long as you don't need these operations, lists are often faster.
		if(self.common is None):
			comm = set(data_1.values()).intersection(set(data_2.values()))
			for element in comm:
				first = list(data_1.keys())[list(data_1.values()).index(element)]
				second = list(data_2.keys())[list(data_2.values()).index(element)]
				matched.append(str(first) + "_" + str(second))
		
		else:
			for x in data_1.items():
				for y in data_2.items():
					match=0
					for i in range(min(len(x[1]),len(y[1]))):
						if x[1][i]==y[1][i]:
							match+=1
					if match>=self.common:       
						matched.append(str(x[0]) + "_" + str(y[0]))
		
			
		
		return matched
		
	
	def write(self):
		with open(self.file_write, "w") as f:
			print("Writing...\n")
			f.write(str(self.compare(self.file_1, self.file_2))[1:-1].replace(", ", "\n"))
			print("Done!")
			
		
		
		

if __name__ == '__main__':
	run = CommandLine()
	print("\n You can also use optional argument --common\n to decide how many common base pair is enough for the match!\n")
	docs = Docs(**vars(run.args)) # vars() returns __dict__ attribute of an object
	docs.write()
	
				
			
	