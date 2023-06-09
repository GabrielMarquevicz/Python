# Python

def fib(n): # def= criação de uma função com nome logo em seguida
  a, b = 0, 1 # definição das variáveis
  while a < n: # while = loop enquanto não chegar o resultado pedido
    print(a, end= ' ') # print = imprimir o resultado e o end = vai fazer com que o resultado apareça no final da operação
    a, b = b, a + b 
fib(int(input("Digite o  número pra fazer fibonacci: "))) # input = ao valor que "n" vai receber, como se fosse scanf do C
