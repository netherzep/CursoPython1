import random

def adivina(numero_aleatorio, numero_adivina):
    
    if(numero_adivina == numero_aleatorio):
        return True
    else:
        return False


def run():
    numero_adivina = int(input('Digita un numero para adivinar del 1 al 10: \n'))
    numero_aleatorio = random.randint(1, 10)

    if(adivina (numero_aleatorio, numero_adivina)):
        print('Adivinaste!')
    else:
        print('intenta de nuevo, el número era: '+ str(numero_aleatorio))


if __name__ ==  '__main__':
    run()