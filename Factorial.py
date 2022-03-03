def factorial(numero):

    if numero > 1:
        numero=numero*factorial(numero-1)
    return numero

num=int(input("Introduce un numero: "))
if num==0:
    print("El factorial de 0 es 1")
else:
    print(factorial(num))
