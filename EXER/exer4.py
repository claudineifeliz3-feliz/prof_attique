# Crie uma função chamada fatorial que receba um número
# qualquer e retorne.

def fatorial():
    num = int(input("Digite um numero: "))
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *=i
    return fatorial
if __name__=="__main__":
    print(fatorial())