# print the mean of the numbers in the file
import sys

sum = 0
n = 0
# sum inpute values
for num in open('data.txt'):
    sum += float(num)
    n += 1
print sum / n
# Programming is fun!
