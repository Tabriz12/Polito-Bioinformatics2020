import numpy as np
import sys




first  = sys.argv[1]
second = sys.argv[2]
m = int(sys.argv[3])
mm = int(sys.argv[4])
g = int(sys.argv[5])

row, column = len(first)+1, len(second)+1; #
matrix = [[0 for x in range(column)] for y in range(row)] 


for r in range(row):
    for c in range(column):
        if r*c==0:
                
            matrix[r][c] = 0
                
        else:
        
            top = matrix[r-1][c] + g
            left = matrix [r][c-1] + g
            diagonal = matrix[r-1][c-1]
            
            if first[r-1]==second[c-1]:
                    diagonal+=m
                    
            else:
                diagonal+=mm
                    
           
            matrix[r][c] = max(top,left,diagonal, 0)



position = np.argmax(matrix)

c = position % column
r = int (position / column)

s = 0
while matrix[r][c]!=0:
    s+=1
    r-=1
    c-=1

f = first[r:r+s]
s = second[c:c+s]

print("\nLocal alignment score: {}\n".format(len(f)))
print(np.matrix(matrix))
print("\n{}\n{}\n{}".format(f, "|"*len(f), s))

