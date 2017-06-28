#Calculo del volumen de una n-esfera. Como parametro recibe el numero de dimensiones y de puntos a generar, como salida devuelve el volumen
def calc_n_sphere_sobol(n_dimensions, n_points):
 
    #numero de puntos dentro de la n-esfera
    hits = 0
    #inicializador de la secuencia sobol
    sout = random.randint(1,10000)
 
    for i in range(0, n_points):
        #generar punto n-dimensional
        p, sout = sobol_lib.i4_sobol ( n_dimensions, sout )
 
        #transforma el numero del intervalo [0,1] al intervalo [-1,1]
        p = (p*2)-1
        j = 0
        s = 0
 
        #sumar cuadrado de las componentes
        while (j<n_dimensions and s<=1):
            s+=p[j]**2
            j+=1
 
        #comprobar si el punto esta contenido en la n-esfera
        if (s<=1):
            hits += 1
    #devolver volumen de la n-esfera
    return  (2**n_dimensions)* float(hits) / n_points
