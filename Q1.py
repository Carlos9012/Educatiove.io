import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
#Dado um array de inteiros e uma janela de tamanho w, 
# encontre o valor máximo atual na janela conforme ela desliza por todo o array.
def q1(janela):
    if janela is None:
        return
    '''max = float('-inf')
    sec = float('-inf')'''
    box = []
    aux = []
    
    if len(arr) >= janela:
        '''for i in arr:
            box.append(i)
            if i > max:
                max = i
            if len(box) == janela:
                print(box)
                aux.append(max)
                f = box.pop(0)
                if f == max:
                    max = sec'''
        
        for i in arr:
            box.append(i)
            if len(box) == janela:
                print(box)
                aux.append(max(box)), box.pop(0)
    else:
        for i in arr:
            box.append(i)

        aux.append(max)
    return aux

if __name__ == '__main__':
    arr =   [1, 2, 3, 1, 1, 0, 0, 1, 6]
    print(q1(3))