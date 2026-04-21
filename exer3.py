
def mensagem():
    texto = (input("Digite a mensagem:"))
    print(texto.upper())
    print(texto.lower())
    print(texto.swapcase())

if __name__== "__main__":
    mensagem()