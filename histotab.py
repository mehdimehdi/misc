

import sys
from array import array

data = [(1,3), 
        (2, 3),
        (50, 3),
        (0, 2),
        (3, 3),
        (2, 3)]


#find the max number of column
max_x = 0

for d in data:
    max_x = max(max_x,d[0]+1)

#create the array for the datastructure
sum_tuple = [0] * max_x

#fill up the data structure
for d in data:
    current = sum_tuple.pop(d[0])
    sum_tuple.insert(d[0],d[1]+current)


#start from the top
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

Build a command line tool which takes a CSV file input, and creates an histogram in ASCII

0,1
2,4
4,2
3,3


Each row in the CSV is data which helps build the histogram. The first value is the bar #, the second value is the height of the bar in the histogram.

There can be more than one row (in the CSV) for each bar.


mehdi$ python histogram.py data.csv
  *   
  **  
  ***
* ***
01234

#for bar 0, there is 1 star, which represent the value of (0,1) in the data list.
#for bar 1, there are 0 stars, because there is no tupe (1,)
#for bar 2, there are 4 stars, because there is (4,2) in the data list
#for bar 3, there are 3 stars, because there is (3,3) in the data list

"""
