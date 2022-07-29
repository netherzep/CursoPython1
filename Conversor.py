
pesos = input("Cuantos pesos Colombianos tiene?: ")
pesos = float(pesos)
deseo = int(input("Que desea hacer? \n1. Peso a Dolar\n2. Peso a Euro \n"))




def Euros(pesos):
    valor_Euro = 4381
    euro = pesos/valor_Euro
    euro = round(euro, 2)
    print()
    return euro

def Dolares(pesos):
    valor_dolar = 4300
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    
    return dolares


if deseo == 1:
    
    print ("Usted tiene USD: " + str(Dolares(pesos)))

if deseo == 2:
    
    print ("Usted tiene EU: " + str(Euros(pesos)))
