import numpy as np
import  time

class Profesor:
    def __init__(self,n):
        self.N = n

    def getTime(self):
        inicio_de_tiempo = time.time()

        self.columnas(np.zeros(self.N),0)

        tiempo_final = time.time()
        tiempo_transcurrido = tiempo_final - inicio_de_tiempo
        return tiempo_transcurrido

    def columnas(self,solucion, etapa):
        if etapa >= self.N:
            return False
        exito = False

        while True:
            if solucion[etapa] < self.N:
                solucion[etapa] = solucion[etapa] + 1

            if self.valido(solucion,etapa):

                if etapa != self.N - 1:
                    exito = self.columnas(solucion,etapa+1)
                    if exito == False:
                        solucion[etapa + 1] = 0

                else:
                    exito = True
            if solucion[etapa] == self.N or exito == True:
                break

        print(solucion)
        return exito

    def diferencia(self,a, b):
        if a > b:
            return a - b
        else:
            return b - a


    def valido(self,solucion, etapa):
        for i in range(etapa):
            if solucion[i] == solucion[etapa] or self.diferencia(solucion[i], solucion[etapa]) == self.diferencia(i, etapa):
                return False

        return True


    def setEne(self, n):
        self.N = n


a=Profesor(4)
a.getTime()






