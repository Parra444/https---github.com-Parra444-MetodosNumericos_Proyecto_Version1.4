import numpy as np
import matplotlib.pyplot as plt

def errorPuntual(manalitica,MallaTemperatura, xmalla, ymalla):
    #Se inicializa la matriz para los errores llena de ceros
    err=np.zeros((len(xmalla),len(ymalla)))

    #Se instauran dos ciclos for para recorrer la matriz y poder comparar
    #cada valor de la matriz analitica y la numerica para calcular el error
    for i in range (len(xmalla)):
        for j in range (len(ymalla)):
            #Se hace un if para evitar la division por 0
            if(manalitica[i][j]==0):
                err[i][j]=0
            else:
                #Se calcula el error con la formula
                err[i][j]=abs(((manalitica[i][j]-MallaTemperatura[i][j])/(manalitica[i][j]))*100)
                
    #Se hace la gráfica 3D del error puntual
    figurita3d2=plt.figure("Figura número 5",figsize=(9.,5.5))
    EjeX=figurita3d2.gca(projection='3d')
    EjeX.plot_surface(xmalla, ymalla, err)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title("Error puntual: Solución Analítica vs Solución Numérica")
    plt.show()

    #Se imprime la matriz de errores puntuales
    print("ERROR PUNTUAL:\n",np.round(err,2))

def errorGlobal(manalitica, MallaTemperatura, N,Nx,Ny):

    #Se inicializan las variables
    errG = 0
    sumatoria = 0
    i = 1
    #Se recorre la matriz para calcular la sumatoria de las temperaturas
    for i in range (Nx):
        for j in range (Ny):
            for z in range (N):
                #Se calcula la sumatoria usando cada valor de las matrices
                sumatoria+=(manalitica[i][j]-MallaTemperatura[i][j])**2
    
    #Se calcula el error global
    errG = np.sqrt((1/N)*sumatoria)
    #Se imprime el error en consola
    print("El error global es: ",np.round(errG,3),"%\n")