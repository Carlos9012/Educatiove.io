import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
import time
#Elementos K principais
#Kth Maior Elemento em um Stream
#Dado um fluxo infinito de números inteiros,nuns, crie uma classe para encontrar ok^{th} 
# maior elemento em um fluxo.
def maior(j):
    arr.sort()
    aux = arr[-j]
    print(arr)
    return aux

if __name__ == '__main__':
    arr = [-8, -11, -7, -9, -12, -10, -20, -33, -14, -17, -42, -8, -47, -72, -89, -16 , -15, -26, -38, -44, -52, 57, -68, -90]
    n = 8
    print(maior(n))