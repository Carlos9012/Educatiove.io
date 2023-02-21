import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
import time
#Fusão K-way
#Mesclar matriz classificada
def mesclar():

    box = []
    num = 0
    
    for i in arr_1:
        box.append(i)
        num += 1
        if num >= m:
            break
    
    num = 0

    for j in arr_2:
        box.append(j)
        num +=1
        if num >= n:
            break
    
    box.sort()
    return box
    

if __name__ == '__main__':
    arr_1 = [1, 2, 7, 92, 0, 0, 0]
    m = 4
    arr_2 = [3, 4, 5]
    n = 3
    print(mesclar())