# Crie uma função que contenha um laço para pegar 3 frutas e
# salvar em uma lista externa ao vetor.

def repeti():
    frutas = []
    for i in range(3):
        fruta = input("🍉 Digite o nome da fruta: ")
        frutas.append(fruta.title())
    print(f"As fruta que você digitou foi: {', '.join(frutas)}")

if __name__=="__main__":
    repeti()