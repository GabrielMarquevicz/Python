# Python

def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end= ' ')
    a, b = b, a + b
fib(int(input("Digite o  número pra fazer fibonacci: ")))
