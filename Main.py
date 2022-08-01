# Mayo 27/2022

# ======================================================================

# Jesus Jair Parra
# Juan Esteban Echeverri
# Juan Pablo Londoño
# Métodos Numéricos (506)

# ======================================================================
# ======================================================================
# DESCRIPCIÓN DEL PROYECTO
# =======================

# Diferencias Finitas

# Con el siguiente codigo se busca utilizar la ecuación diferencial de Laplace
# para calcular la temperatura de los nodos de una malla cuadrada de longitud unitaria
# por medio de Diferencias Finitas. Las mallas utilizadas son, una malla 5x5, una 11x11
# y otra 31x31

# ======================================================================

#Importación de librerias
#Para que funcione el código se debe instalar las librerias de pip y matplot
#introduciendo los siguientes comandos en el cmd:
#python -m pip install -U pip
#python -m pip install -U matplotlib

#También, debe instalar la libreria numpy con el siguiente comando en el cmd:
#pip install numpy



import numpy as np
import errores
import solucionMallas

option = 0
while(int(option)<=3):

    option = input("Elija el caso que desea ver:\n1. Malla 5x5\n2. Malla 11x11\n3. Malla 31x31\n->")

    if (int(option) == 1):
        Nx=5 #Cantidad de nodos de la matriz en el eje X
        dx=1/(Nx-1) #Distancia entre cada nodo del eje X
        x=np.linspace(0,1,Nx)#Se genera el vector para X

        Ny=5 #Cantidad de nodos de la matriz en el eje Y
        dy=1/(Ny-1) #Distancia entre cada nodo del eje Y
        y=np.linspace(1,0,Ny) #Se genera el vector para Y

        N = Nx*Ny #Número total de nodos

        #Valores en frontera
        print("Ahora, debe ingresar los valores en frontera...\n\nSi ingresa la temperatura del caso a) se mostrará la solución numérica, analítica y los errores puntual y global\nEn caso contrario, solo se mostrará la solución numérica")
        T_4=float(input("Temperatura del lado superior:\n->")) #Temperatura lado superior
        T_3=float(input("Temperatura del lado derecho:\n->")) #Temperatura lado derecho
        T_2=float(input("Temperatura del lado inferior:\n->")) #Temperatura lado inferior
        T_1=float(input("Temperatura del lado izquierdo:\n->")) #Temperatura lado izquierdo
        
        #Se generan las matrices a partir de los vectores X y Y, con un identificador i,j
        xmalla,ymalla=np.meshgrid(x,y,indexing='ij')
        ymalla=np.transpose(ymalla)
        xmalla=np.transpose(xmalla)

        if(int(T_4)==1 and int(T_3)==0 and int(T_2)==0 and int(T_1)==0):
            mnumerica=solucionMallas.solucionNumerica(Nx,Ny,dx,dy,xmalla,ymalla,T_1,T_2,T_3,T_4)
            manalitica=solucionMallas.solucionAnalitica(xmalla,ymalla)
            errores.errorPuntual(manalitica,mnumerica,xmalla,ymalla)
            errores.errorGlobal(manalitica,mnumerica,N,Nx,Ny)
        else:
            mnumerica=solucionMallas.solucionNumerica(Nx,Ny,dx,dy,xmalla,ymalla,T_1,T_2,T_3,T_4)

    elif (int(option) == 2):
        Nx=11 #Cantidad de nodos de la matriz en el eje X
        dx=1/(Nx-1) #Distancia entre cada nodo del eje X
        x=np.linspace(0,1,Nx)#Se genera el vector para X

        Ny=11 #Cantidad de nodos de la matriz en el eje Y
        dy=1/(Ny-1) #Distancia entre cada nodo del eje Y
        y=np.linspace(1,0,Ny) #Se genera el vector para Y

        N = Nx*Ny #Número total de nodos

        #Valores en frontera
        T_4=float(input("Temperatura del lado superior:\n->")) #Temperatura lado superior
        T_3=float(input("Temperatura del lado derecho:\n->")) #Temperatura lado derecho
        T_2=float(input("Temperatura del lado inferior:\n->")) #Temperatura lado inferior
        T_1=float(input("Temperatura del lado izquierdo:\n->")) #Temperatura lado izquierdo
        
        #Se generan las matrices a partir de los vectores X y Y, con un identificador i,j
        xmalla,ymalla=np.meshgrid(x,y,indexing='ij')
        ymalla=np.transpose(ymalla)
        xmalla=np.transpose(xmalla)

        if(int(T_4)==1 and int(T_3)==0 and int(T_2)==0 and int(T_1)==0):
            mnumerica=solucionMallas.solucionNumerica(Nx,Ny,dx,dy,xmalla,ymalla,T_1,T_2,T_3,T_4)
            manalitica=solucionMallas.solucionAnalitica(xmalla,ymalla)
            errores.errorPuntual(manalitica,mnumerica,xmalla,ymalla)
            errores.errorGlobal(manalitica,mnumerica,N,Nx,Ny)
        else:
            mnumerica=solucionMallas.solucionNumerica(Nx,Ny,dx,dy,xmalla,ymalla,T_1,T_2,T_3,T_4)

    elif (int(option) == 3):
        Nx=31 #Cantidad de nodos de la matriz en el eje X
        dx=1/(Nx-1) #Distancia entre cada nodo del eje X
        x=np.linspace(0,1,Nx)#Se genera el vector para X

        Ny=31 #Cantidad de nodos de la matriz en el eje Y
        dy=1/(Ny-1) #Distancia entre cada nodo del eje Y
        y=np.linspace(1,0,Ny) #Se genera el vector para Y

        N = Nx*Ny #Número total de nodos

        #Valores en frontera
        T_4=float(input("Temperatura del lado superior:\n->")) #Temperatura lado superior
        T_3=float(input("Temperatura del lado derecho:\n->")) #Temperatura lado derecho
        T_2=float(input("Temperatura del lado inferior:\n->")) #Temperatura lado inferior
        T_1=float(input("Temperatura del lado izquierdo:\n->")) #Temperatura lado izquierdo
        
        #Se generan las matrices a partir de los vectores X y Y, con un identificador i,j
        xmalla,ymalla=np.meshgrid(x,y,indexing='ij')
        ymalla=np.transpose(ymalla)
        xmalla=np.transpose(xmalla)

        if(int(T_4)==1 and int(T_3)==0 and int(T_2)==0 and int(T_1)==0):
            mnumerica=solucionMallas.solucionNumerica(Nx,Ny,dx,dy,xmalla,ymalla,T_1,T_2,T_3,T_4)
            manalitica=solucionMallas.solucionAnalitica(xmalla,ymalla)
            errores.errorPuntual(manalitica,mnumerica,xmalla,ymalla)
            errores.errorGlobal(manalitica,mnumerica,N,Nx,Ny)
        else:
            mnumerica=solucionMallas.solucionNumerica(Nx,Ny,dx,dy,xmalla,ymalla,T_1,T_2,T_3,T_4)

print("Se ingresó una opción inválida")