# #Crie uma função que receba o dia, mês e ano e retorne
# para o usuário uma data no formato dd/mm/aaaa. 

def formatar_data():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    return f"{dia:02d}/{mes:02d}/{ano}"

if __name__ =="__main__":
    print(formatar_data())

