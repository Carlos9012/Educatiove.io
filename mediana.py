import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
import time
#Dois montes
#Janela Deslizante Mediana
#Given an integer array nums and an integer k, there is a sliding window of size k
#which is moving from the very left of the array to the very right. You can only see the k
#numbers in the window. Each time the sliding window moves right by one position,
# return the median of the current window. Answers within 10^{-5}10^−5
#of the actual value will be accepted.
def mediana(janela):
    if janela is None:
        return

    box = []
    box_2 = []
    aux = []
    med = 0 
    
    if janela%2 != 0:
        j = janela/2 - 0.5
        for i in arr:
            box.append(i)
            if len(box) == janela:
                box_2 = box.copy()
                box_2.sort()
                aux.append(box_2[int(j)])
                print(box_2)
                box_2.clear()
                box.pop(0)

    else:
        j1 = janela/2
        j2 = janela/2 - 1
        for i in arr:
            box.append(i)
            if len(box) == janela:
                box_2 = box.copy()
                box_2.sort()
                med = (box_2[int(j1)] + box_2[int(j2)])/2
                aux.append(med)
                print(box_2)
                box_2.clear()
                box.pop(0)

    return aux

if __name__ == '__main__':
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    print(mediana(4))