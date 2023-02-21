import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
import time
#Manipulação de bits
#Encontre a diferença
def manipulacao(self):
    if self is None:
        return

    cont_1 = len(string_1) -1 
    cont_2 = len(string_2) -1 
    box = [cont_1, cont_2]
    aux = []
    
    for i in range(0, min(box)+1):
        if string_1[i] != string_2[i]:
            aux.append(i)
            break
    
    if aux == []:
        aux.append(box[-1])
    
    return aux
        

if __name__ == '__main__':
    string_1 = "prq"
    string_2 = "prqs"
    print(manipulacao(string_1))