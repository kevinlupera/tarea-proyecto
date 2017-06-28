import random
import math
#----------------------------------------------------------------------
def funcionMontecarlo(landa,a,b,num_datos):
    arrayR=[]
    arrayX=[]

    for i in range(num_datos):
        r=random.random()
        arrayR.append(r)
        x=-(math.log(r))/landa
        #print(r)

    for i in range(num_datos):
        x=-(math.log(arrayR[i]))/landa
        xUniforme=(arrayR[i]*(b-a))+a
        #print(x)
        #print(xUniforme)


def main():
    print("Simulacion Montecarlo con distribucion exponencial")
    landa=int(input("Ingresar Landa: "))
    a=int(input("Ingresar a: "))
    b=int(input("Ingresar b: "))
    num_datos=int(input("Ingresar cantidad de datos a generar: "))
    funcionMontecarlo(landa,a,b,num_datos)
    

#----------------------------------------------------------------------
if __name__ == "__main__":
    main()
