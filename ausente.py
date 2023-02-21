import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
import time
#Classificação cíclica
#Número ausente
#Given an array, nums, containing n distinct numbers in the range [0, n]
#  return the only number in the range that is missing from the array.
def ausente():
    arr.sort()
    box = []
    cont = 0
    for i in range(0, len(arr)):
        print(arr[i], cont)
        if cont != arr[i]:
            box.append(cont)
            cont+=1
        cont+=1

    if box == []:
        box.append(len(arr))
        
    return box


    

if __name__ == '__main__':
    arr = [0, 12, 4, 6, 7, 8, 3, 9, 5, 10, 2, 1]
    print(ausente())