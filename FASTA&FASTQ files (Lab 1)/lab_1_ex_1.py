import sys
import random


if len(sys.argv)!=7:
    sys.exit("Number of arguments should be 6! \n \
Format: filename, number of reads, weights for each base pair")

seq_len = 50 # length of read
filename = sys.argv[1] #name of file to write
num_reads = int(sys.argv[2]) # number of reads
base = list('ATCG')
weights = [int(arg) for arg in sys.argv[3:7]] #weights for each base pair


data = random.choices(base, weights = weights, k=seq_len*num_reads)

with open(filename,"w") as new_file:
	for read_id in range(num_reads):
		new_file.write(">id-{}\n{}\n".format(read_id, "".join(data[read_id*seq_len : (read_id+1)*seq_len])))
	
print("Done!")

 
 