#Fração em Decimal Recorrente
# Mapas de hash

def fracao():
    result = num/den
    valores = []
    repetidos = set()
    aux = ''
    aux_2 = ''
    val = False
    print(result)
    result = 1.56401010101

    for dado in str(result):
        if val == False:
            aux = aux + dado
        elif val == True:
            if dado not in valores:
                valores.append(dado)
            else:
                repetidos.add(dado)
        if dado == ".":
            val = True

    for i in str(repetidos):
        if i != "{" and i != "}" and i != "'" and i != "," and i != " ":
            aux_2 = aux_2 + i

    aux = aux + "(" + aux_2 + ")"
    print(aux)

    return

if __name__ == '__main__': 
    num = 456
    den = 199
    fracao()