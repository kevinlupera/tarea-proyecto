import random
import math
import xlwt
 
#----------------------------------------------------------------------
def funcionMontecarlo(landa,a,b,num_datos):
    arrayR=[]
    arrayX=[]
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("Hoja1")
    cols = ["R", "X", "UNIFORME"]
    row = sheet1.row(0)
    for i in range(len(cols)):
        row.write(i, cols[i])
    for i in range(num_datos):
        r=random.random()
        arrayR.append(r)
        x=-(math.log(r))/landa
        #print(r)
        row = sheet1.row(i+1)
        row.write(0, arrayR[i])
    for i in range(num_datos):
        x=-(math.log(arrayR[i]))/landa
        xUniforme=(arrayR[i]*(b-a))+a
        #print(x)
        #print(xUniforme)
        row = sheet1.row(i+1)
        row.write(1, x)
        row.write(2, xUniforme)
    #EXCEL
    book.save("test.xls")


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
