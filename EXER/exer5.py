# Faça uma função que receba o nome, peso, idade e altura de um
# individuo e retorne o calculo do Indice de Massa Corporal.
# IMC = Peso/Altura².

def calcula_imc():
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    idade = int(input("Digite sua idade:"))
    
    calcula_imc = peso / (altura**2)
    return f"{nome}, tem {idade} anos de idade e seu IMC é {calcula_imc:.2f}"

if __name__=="__main__":
    print(calcula_imc())


