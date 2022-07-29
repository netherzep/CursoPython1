
def palindromo(Word):

    pali = Word.replace(' ','').lower()
    Derecho = pali[::]
    Reves = pali[::-1]
    
    if Derecho == Reves:
        print("Es Palindromo")
    else:
        print("No Es palinromo")


Word = input("Digite una palabra: \n")
palindromo(Word)

