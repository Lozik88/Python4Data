# i = 100
# for i in range(i):
#     x = i+1
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0: 
#         print('Fizz')
#     elif i % 5 == 0: 
#         print('Buzz')
#     else:
#         print(i)
import json
import requests
import random
import os

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)