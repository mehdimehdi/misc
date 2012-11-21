import sys
from array import array

data = [(1,3), 
        (2, 3),
        (50, 3),
        (0, 2),
        (3, 3),
        (2, 3)]

max_x = 0

for d in data:
    max_x = max(max_x,d[0]+1)

sum_tuple = [0] * max_x

for d in data:
    current = sum_tuple.pop(d[0])
    sum_tuple.insert(d[0],d[1]+current)

index = max(sum_tuple)
while (index > 0):
    for boom in sum_tuple:
        if index <= boom:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")

    sys.stdout.write("\n")
    index = index - 1


"""
data = [(0,1),
        (2, 4),
        (4, 2),
        (3, 3)]



mehdi$ python histogram.py
  *   
  **  
  ***
* ***
01234

#for column 0, there is 1 star, which represent the value of (0,1) in the data list.
#for column 1, there are 0 stars, because there is no tupe (1,)
#for column 2, there are 4 stars, because there is (4,2) in the data list
#for column 3, there are 3 stars, because there is (3,3) in the data list
#for column 4, there are 2 stars, because there is (4,2) in the data list
"""
