print(max(97, 80)) # prints the maximum number
print(min(45, 37)) # prints the minimum number

print(pow(2, 3)) # acts as 2^3 = 2 x 2 x 2 = 8
print(abs(-90)) # prints the absolute value of -90

print(round(10.4)) # round off the numbers to nearest value; here 10
print(round(10.6)) # rounds off to 11
# if decimal values <= .5 then it becomes the next small num i.e round(1.5) = 1
# if decimal values >= .6 then it becomes the next large num i.e, round(1.6) = 2

from math import * # importing all functions present in module 'math'
# NOTE: the functions used below requires to import math modules 
print(sqrt(25)) # gets the square root of the number
print(ceil(56.1)) #  rounds a number up to the next largest integer (large num >= num)
print(floor(8.7)) # rounds the number to the next smallest integer (small num <= num)