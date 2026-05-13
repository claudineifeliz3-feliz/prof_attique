
import timeit
from functools import reduce

def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

def soma_for(lista):
    total = 0
    for n in lista:
        total += n
    return total

def soma_while(lista):
    total = 0
    i = 0
    while i < len(lista):
        total += lista[i]
        i+= 1
    return total
    
numeros =[3,8,20,21,34,44]
N = 100_000

resultados = {
    "Recursiva"  :timeit.timeit(lambda: soma_recursiva(numeros), number=N),
    "Loop for"   :timeit.timeit(lambda: soma_for(numeros),       number=N),
    "Loop while" :timeit.timeit(lambda: soma_while(numeros),     number=N),
    "Sum()"      :timeit.timeit(lambda: sum(numeros),            number=N),
    "Reduce()"   :timeit.timeit(lambda: reduce(lambda a,b: a+b, numeros), number=N),
}

# Ordena do mais lento para o mais rápido
resultado = dict(sorted(resultados.items(), key=lambda x: x[1], reverse=True))

mais_rapido = min(resultados.values())


print(f"\n{'Método':<12} {'tempo (s)':>10} {'Comparação':>15}")
print("-"*40)
for metodo, tempo in resultados.items():
    print(f"{metodo:<12} {tempo:>10.4f}s {tempo/mais_rapido:>13.1f}x")
print("-"*40)