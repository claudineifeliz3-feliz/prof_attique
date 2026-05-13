def fatorial(n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1)
print(fatorial(4))
print(fatorial(1))

for n in reversed (range(1,5)):
    print((n-1)*n)