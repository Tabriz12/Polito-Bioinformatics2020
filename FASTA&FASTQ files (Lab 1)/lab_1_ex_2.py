import sys
from collections import Counter

if len(sys.argv)!=4:
	sys.exit("Number of arguments should be 3! \
\ file to read, file to write, and GC threshold	")
read_file = sys.argv[1]
write_file = sys.argv[2]

gcth = int(sys.argv[3]) # GC threshold
low_complexity = ['AAAAAA', 'TTTTTT', 'CCCCCC', 'GGGGGG']
lc_reads = [] # reads containing low complexity sequence
gc_reads = {}
base_pair=Counter()

with open(read_file, "r") as file:
	for i, line in enumerate(file):
		if(line[0]!='>'):
			base_pair += (Counter(line))
			for sequence in low_complexity:
				if sequence in line:
					lc_reads.append((i-1)/2) # considering each read takes one line, can be buggy if reads exceeds one line
					break
			if line.count('GC') > gcth:
				gc_reads['id-' + str(int((i-1)/2))] = line.count('GC')

base_pair.pop("\n")

with open(write_file, "w") as wfile:
	print("Writing to the {} file ...".format(write_file))
	wfile.write("Base pair:\n {} \n Low Complexity Sequence read_id: \n {} \n GC sequence reads/counts: \n {} \r\n".format(base_pair, lc_reads, gc_reads))
	
print("Done!")
				
			


