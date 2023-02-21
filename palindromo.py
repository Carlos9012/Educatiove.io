import math
from operator import le
import os
import random
import re
import sys
from tokenize import Double
from unittest import result
import time
#Dois ponteiros
#Palíndromo válido
#Write a function that takes a string s as input and checks whether it’s a palindrome or not.
def palindromo(self):
    if self is None:
        return

    cont = len(string) -1 
    aux = 0
    
    for i in string:
        print(string[cont] , i)
        if string[cont] == i:
            aux+=1
        cont-=1

    if aux == len(string):
        return True
    
    else:
        return False

if __name__ == '__main__':
    string = "RACEACAR"
    print(palindromo(string))