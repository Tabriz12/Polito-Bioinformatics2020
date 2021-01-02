
reference = 'ATTTCGGCGGCGACACAGGGATGACACAGGGCACGCAGCATTTAAAAAATTTTTGGACACAGCAGCAT'
index = [i for i in range(len(reference))]
#dict = {index[i]: list(reference[i]) for i in range(len(index))} that was wrong because we do not consider original
# genome in the calculation of reference genome
dict={}

with open("alignment.txt", "r") as file:
	for line in file:
		genome = line.split()[1]
		start = int(line.split()[2])
		
		for base in genome:
			dict.setdefault(start, []).append(base)
			start+=1

keys = dict.keys()
difference = list(set(index).difference(set(keys)))

for element in difference:
	dict[element]=list(reference[element])

 
def most_frequent(List): 
    return max(set(List), key = List.count) 


for i in range(len(reference)):
	dict[i] = most_frequent(dict[i])


ordered_dict = {i: dict[i] for i in range(len(reference))}


result = "".join(ordered_dict.values())

print(result)


