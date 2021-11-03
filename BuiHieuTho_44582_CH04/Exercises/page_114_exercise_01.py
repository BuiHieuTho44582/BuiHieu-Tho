"""
Author: Bui Hieu Tho
Date: 24/09/2021

Problem: Translate each of the following numbers to decimal numbers:
a. 110012
b. 1000002
c. 111112

Solution:
    ....
"""
binary = input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print (decimal)
