#Subconjuntos
#Permutações
from itertools import permutations

def per(self):
    perm = permutations(arr)
    box = []

    print(perm)
    for i in list(perm):
        box.append(i)
    
    return box

if __name__ == '__main__':
    arr = "xy"
    print(per(arr))