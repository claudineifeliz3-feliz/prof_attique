
import timeit

def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

numeros =[3,8,20,21,34,44]

tempo_recursiva = timeit.timeit(lambda: soma_recursiva(numeros), number=100000)
tempo_sum       = timeit.timeit(lambda: sum(numeros), number=100000)

print(f"Recursiva: {tempo_recursiva:.4f}s")
print(f"sum()   : {tempo_sum:.4f}s")
print(f"sum() é {tempo_recursiva / tempo_sum:.1f}x mais rápido")