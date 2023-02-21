#tente
#Números Lexicográficos
#Given an integer value n, write a function that returns all the numbers in the range 1
#to n in lexicographical order.
def sortLexo(num): 
    box = []
    palavra = ""
    for i in range(1, num+1):
        palavra = palavra + str(i) + ' '
    
    
    words = palavra.split() 
    words.sort() 
    
    for i in words: 
        box.append(i)
    print(box)
if __name__ == '__main__': 
    sortLexo(12) 