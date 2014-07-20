# print the mean of the numbers in the file
import sys
#change sum to var
var = 0
n = 0
# var inpute values
for num in open('data.txt'):
    var += float(num)
    n += 1
print var / n
# Programming is fun!
