
from pickle import TRUE


def primo(numero):
    

    for i in range(1, numero+1):
        print(i)
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            return False
            break
        else:
            return True
            break
       

def run():
    numero = int(input('Digite un numero para verificar su primalidad: '))
    
    if(primo(numero)):
        print('El numero es primo')
    else:
        print('El numero NO es primo')


if __name__ == '__main__':
    run()