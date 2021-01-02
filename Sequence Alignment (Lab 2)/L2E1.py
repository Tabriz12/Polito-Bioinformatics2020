import numpy as np
import sys




first  = sys.argv[1]
second = sys.argv[2]
m = int(sys.argv[3])
mm = int(sys.argv[4])
g = int(sys.argv[5])

row, column = len(first)+1, len(second)+1; #
matrix = [[0 for x in range(column)] for y in range(row)] 


choices=[[0 for x in range(column)] for y in range(row)]

for r in range(row):
    for c in range(column):
        if(r+c>0):
            if r==0:
                matrix[r][c] = matrix[r][c-1] + g
                choices[r][c] = "l"
            elif c==0:
                matrix[r][c] = matrix[r-1][c] + g
                choices[r][c] = "t"
            else:
        
                top = matrix[r-1][c] + g
                left = matrix [r][c-1] + g
                diagonal = matrix[r-1][c-1]
                
                if first[r-1]==second[c-1]:
                    diagonal+=m
                    
                else:
                    diagonal+=mm
                
                if max(diagonal,left,top)==diagonal:
                    if(choices[r][c] == 0):
                        choices[r][c] = "d"
                    else:
                        choices[r][c] +="_d"
                        
                if max(diagonal,left,top)==left:
                    if(choices[r][c] == 0):
                        choices[r][c] = "l"
                    else:
                        choices[r][c] +="_l"
                if max(diagonal,left,top)==top:
                    if(choices[r][c] == 0):
                        choices[r][c] = "t"
                    else:
                        choices[r][c] +="_t"
                    
                matrix[r][c] = max(top,left,diagonal)

#### solution takes only one path prioratizing moving to top or left over moving diagonal in case of path split
i = row-1
k = column -1
a = []
b = []
index_a = -1
index_b = -1
sign=[]
while choices[i][k] != 0:
	if choices[i][k][-1] == 'd':
		a = [first[index_a]] + a
		sign = ["|"] + sign
		b = [second[index_b]] + b
		index_a -= 1
		index_b -= 1
		i -= 1
		k -= 1
        
	elif choices[i][k][-1] == 't':
		a = [first[index_a]] + a
		b = ["_"] + b
		sign = [" "] + sign
		index_a -= 1
		i -= 1
	else:
		a = ["_"] + a
		b = [second[index_b]] + b
		sign = [" "] + sign
		index_b -= 1
		k -= 1
        
a="".join(a)
b="".join(b)
sign="".join(sign)

print(np.matrix(matrix))

print("{}\n{}\n{}".format(a, sign, b))

        
        
        
    
            
