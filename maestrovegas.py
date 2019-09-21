import numpy as np
import random
import  time

class MaestroVegas:
    def __init__(self,n):
        self.n=n

    def getTime(self):
        inicio_de_tiempo = time.time()

        fallos = 0
        while not (self.columnas()):
            fallos += 1

        #print("Fallos: ", fallos)

        tiempo_final = time.time()
        tiempo_transcurrido = tiempo_final - inicio_de_tiempo

        return tiempo_transcurrido

    def columnas(self):
        self.tablero = np.zeros((self.n, self.n))
        col=np.zeros(self.n)-1
        columnasSeleccionadas=np.zeros(self.n)
        i=self.n-1
        while i>=0:
            j=int(random.uniform(0,self.n))

            if j in col:
                columnasSeleccionadas[j] = -1
                if self.filaComprobada(columnasSeleccionadas):
                    return False
            elif self.comprobar(i,j):
                self.tablero[i][j]=1
                col[i]=j
                i-=1
                columnasSeleccionadas = np.zeros(self.n)
            else:
                columnasSeleccionadas[j] = -1
                if self.filaComprobada(columnasSeleccionadas):
                    return False


        return True

    def filaComprobada(self,fila):
        for j in fila:
            if j==0:
                return False

        return True


    def comprobar(self,i,j):
        #Diagonal \
        for k in range(1, self.n):
            if (i + k < self.n and j+k < self.n and self.tablero[i+k][j+k] != 0):
                return False
        for k in range(1, self.n):
            if (i + k < self.n and j-k >= 0 and self.tablero[i+k][j-k] != 0):
                return False


        return True


    def setEne(self,n):
        self.n = n

