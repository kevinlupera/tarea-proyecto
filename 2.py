import random
import math
import xlwt
def funcionMontecarlo(landa,num_datos):
    for i in range(num_datos):
        r=random.random()
        x=-(math.log(r))/landa
        print(x)


def Inicio():
    print("Simulacion Montecarlo con distribucion exponencial")
    landa=int(input("Ingresar Landa: "))
    num_datos=int(input("Ingresar cantidad de datos a generar: "))
    funcionMontecarlo(landa,num_datos)

Inicio()
