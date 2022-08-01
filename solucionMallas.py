import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import math

def solucionNumerica(Nx,Ny,dx,dy,xmalla,ymalla,T_1,T_2,T_3,T_4):

    #Se grafica la matriz
    plt.scatter(xmalla, ymalla)
    plt.title("Malla de nodos")
    plt.show()

    #Cantidad total de nodos en la matriz
    N=Nx*Ny
    #Sistema de ecuaciones
    A=np.zeros((N,N))
    B=np.zeros(N)

    #Se hacen los for para calcular los valores de los nodos usando las diferencias finitas
    for i in range (Nx):
        for j in range(Ny):
            n=i+j*Nx
            #Primera esquina
            if i==0 and j==0:
                A[n][n]=1/dx**2+1/dy**2
                A[n][n+1]=-2/dx**2
                A[n][n+2]=1/dx**2
                A[n][n+Nx]=-2/dy**2
                A[n][n+2*Nx]=1/dy**2
            #Segunda esquina
            elif i==Nx-1 and j==0:
                A[n][n]=1/dx**2+1/dy**2
                A[n][n-1]=-2/dx**2
                A[n][n-2]=1/dx**2
                A[n][n+Nx]=-2/dy**2
                A[n][n+2*Nx]=1/dy**2
            #Tercera esquina
            elif i==Nx-1 and j==Ny-1:
                A[n][n]=1/dx**2+1/dy**2
                A[n][n-1]=-2/dx**2
                A[n][n-2]=1/dx**2
                A[n][n-Nx]=-2/dy**2
                A[n][n-2*Nx]=1/dy**2
            #Cuarta esquina
            elif i==0 and j==Ny-1:
                A[n][n]=1/dx**2+1/dy**2
                A[n][n+1]=-2/dx**2
                A[n][n+2]=1/dx**2
                A[n][n-Nx]=-2/dy**2
                A[n][n-2*Nx]=1/dy**2
            #Lado inferior
            elif 0<i<Nx-1 and j==0:
                A[n][n]=1.
                B[n]=T_1
            #Lado derecho
            elif i==Nx-1 and 0<j<Ny-1:
                A[n][n]=1.
                B[n]=T_2
            #Lado superior
            elif 0<i<Nx-1 and j==Ny-1:
                A[n][n]=1.
                B[n]=T_3
            #Lado izquierdo
            elif i==0 and 0<j<Ny-1:
                A[n][n]=1.
                B[n]=T_4
            #Nodos centrales
            else:
                A[n][n]=-2/dx**2-2/dy**2
                A[n][n+1]=1/dx**2
                A[n][n-1]=1/dx**2
                A[n][n+Nx]=1/dy**2
                A[n][n-Nx]=1/dy**2  

    #Se calcula la temperatura con la inversa de la matriz          
    T=np.dot(np.linalg.inv(A),B)

    MallaTemperatura=np.zeros((Nx, Ny))
    #Conversión de vector a malla
    for n in range(N):
        i=n%Nx
        j=n//Nx
        MallaTemperatura[i][j]=T[n]
    print('SOLUCIÓN NUMÉRICA: \n',np.round(MallaTemperatura,2))
    #Gráfica de calor
    plt.contourf(xmalla, ymalla, MallaTemperatura)
    plt.title('Gráfica de calor de la Solución Numérica')
    plt.show()

    tempmax=max(T)

    #Gráfica 3d de calor
    from mpl_toolkits.mplot3d import axes3d 
    figurita3d=plt.figure("Figura número 3",figsize=(9.,5.5))
    EjeX=figurita3d.gca(projection='3d')
    cf = EjeX.contourf(xmalla,ymalla,MallaTemperatura,350,cmap=cm.coolwarm)
    plt.colorbar(cf)
    EjeX.plot_surface(xmalla, ymalla, MallaTemperatura, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    EjeX.set_zlim(0,tempmax)
    EjeX.zaxis.set_major_locator(LinearLocator(5))
    EjeX.zaxis.set_major_formatter('{x:.02f}')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Solucion Numérica')
    plt.bar_label
    plt.show()

    return np.round(MallaTemperatura,4)


def solucionAnalitica(xmalla,ymalla):

    #Se inicializa la matriz donde se guardará la solución analítica
    matrizanalitica=np.zeros((len(xmalla),len(ymalla)))
    sol=0
    

    #Se recorren las matrices para usar los valores de las mallas X y Y
    for i in range (len(xmalla)):
        for j in range (len(ymalla)):
            #Se vuelve a hacer la solución 0 para que no se acumulen los valores anteriores
            sol=0
            for z in range(80):
                #Se calcula la solución de la sumatoria desde i (en nuestro caso, z) hasta 80
                sol += (((4)/((2*(z+1)-1)*math.pi*math.sinh((2*(z+1)-1)*math.pi)))*(math.sin((2*(z+1)-1)*math.pi*xmalla[i][j])*math.sinh((2*(z+1)-1)*math.pi*ymalla[i][j])))
            #Se guarda el valor en la matriz de la solución analitica
            matrizanalitica[i][j]=sol

    #Se imprime la solución analítica
    print('SOLUCION ANALÍTICA:\n',np.round(matrizanalitica,2))


    #Se hace la gráfica 3D de calor para la solución analítica
    figurita3d=plt.figure("Figura número 4",figsize=(9.,5.5))
    EjeX=figurita3d.gca(projection='3d')
    cf = EjeX.contourf(xmalla,ymalla,matrizanalitica,200,cmap=cm.coolwarm)
    EjeX.grid()
    plt.colorbar(cf)
    EjeX.plot_surface(xmalla, ymalla, matrizanalitica, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    EjeX.set_zlim(0,1)
    EjeX.zaxis.set_major_locator(LinearLocator(5))
    EjeX.zaxis.set_major_formatter('{x:.02f}')
    
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Solucion Analítica')
    plt.show()
    
    return np.round(matrizanalitica,4)

   