import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
import time
#Programaçao dinamica
#N-ésimo número de Tribonacci
#Given a number n, calculate the corresponding Tribonacci number.
#The Tribonacci sequence T_n is defined as:
def tribbonaci(self):
    box = [0,1,1]
    while len(box) <= n:
        soma = box[-1] + box[-2] + box[-3]
        box.append(soma)
    print(box)
    return box[- 1]
if __name__ == '__main__':
    n = 7
    print(tribbonaci(n))