import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
#Saber o que rastrear
#Primeiro caractere único em uma string
#For a given string of characters, s, your task is to find the first non-repeating 
#character in it and return its index. Return
#−1 if there’s no unique character in the given string.

def counting(dados):
    valores = []
    repetidos = set()
    
    for dado in dados:
        if dado not in valores:
            valores.append(dado)
        else:
            repetidos.add(dado)
    print(f'Valores = {valores}')
    print(f'Repetidos = {repetidos}')
    aux_1 = ''.join(valores)
    aux_2 = ''.join(repetidos)
    print(aux_1)

    if repetidos == set():
        return -1

    else:
        for i in range(0, len(aux_2)):
            aux_1 = aux_1.replace(aux_2[i], '')
        print(aux_1)
        
        
        
        for i in range(0, len(valores)):
            if valores[i] == aux_1[0]:
                cont = i
                break
        return cont
    

if __name__ == '__main__':
    arr = 'awsjawuh'
    print(counting(arr))