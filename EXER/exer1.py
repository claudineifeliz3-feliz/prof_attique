# Crie uma função chamada potencia que receba um
# numero e seu expoente e retorne somente o resultado
# para o usuário.


def potencia():
    numero = float(input("Digite um número: "))
    expoente = int(input("Digite um expoente: "))
    return numero ** expoente

if __name__ == "__main__":
    resultado = potencia()
    print(f"O resultado é: {resultado}")
