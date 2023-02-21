#Técnicas Gananciosas
#Barcos para salvar pessoas
def barco(self):
    cont = 0
    for i in arr:
        cont+=i
    result = cont/n

    if cont%n != 0:
        return int(result) +1

    else:
        return int(result)
 

if __name__ == '__main__':
    arr =[3, 4, 5, 3, 4]
    n = 6
    print(barco(n))