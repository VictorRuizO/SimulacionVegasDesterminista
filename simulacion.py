# -*- coding: utf-8 -*-
import random
import simpy
import numpy
from maestrovegas import *
from determinista import *

VEGAS = MaestroVegas(0)
DETERMINISTA = Profesor(0)

# Variabes de entrada
TIEMPO_SIMULACION = 8*60*60      # Tiempo de la simulacion en segundos
LLEGADA_ROBOTS = [10,30]
TAMAÑO_TABLERO = [4,5,6,8,10,12,15]
GANA_HUMANO = 30
BENEFICIO_ESTUDIANTE = 15
PIERDE_HUMANO = 10

# Variables estado
COLA = 0
ESPERA_ROBOTS = numpy.array([])

# Variables desempeño
MAX_COLA = 0
PROMEDIO_ESPERA = 0.0
TOTAL_INGRESOS=0.0
TOTAL_BENEFICIO_ESTUDIANTE=0.0
TOTAL_PERDIDA=0.0
TOTAL_ROBOTS = 0

class Simulacion:

    def llegadaRobot(self,env,servidor):
        i=1
        while env.now<TIEMPO_SIMULACION:
            print('%7.2f'%env.now,"Llega el robot ",i)
            process = self.accionRobot(env,servidor,i)
            env.process(process)
            nextRobot = random.uniform(LLEGADA_ROBOTS[0],LLEGADA_ROBOTS[1])
            yield env.timeout(nextRobot)
            i+=1



    def accionRobot(self,env,servidor,numero):
        global COLA
        global TOTAL_INGRESOS
        global  TOTAL_PERDIDA
        global  TOTAL_BENEFICIO_ESTUDIANTE
        global MAX_COLA
        global TOTAL_ROBOTS
        global ESPERA_ROBOTS
        llegada = env.now
        with servidor.request() as req:
            COLA+=1
            if COLA > MAX_COLA:
                MAX_COLA = COLA  # Seteo cola maxima
            r = yield req

            COLA-=1
            espera = env.now - llegada
            ESPERA_ROBOTS=np.append(ESPERA_ROBOTS,espera)
            i=random.uniform(0, len(TAMAÑO_TABLERO))
            i=int(i)
            n=TAMAÑO_TABLERO[i]
            VEGAS.setEne(n)
            DETERMINISTA.setEne(n)

            tiempo_robot=VEGAS.getTime()
            tiempo_profesor = DETERMINISTA.getTime()
            print(tiempo_profesor,VEGAS.getTime(),n)
            if tiempo_profesor>tiempo_robot:
                yield env.timeout(tiempo_robot)
                TOTAL_PERDIDA += PIERDE_HUMANO
                print(env.now, "Sale robot: ", numero, ". Gana robot ", "TP: ", tiempo_profesor, "TR: ", tiempo_robot)
            else:
                yield env.timeout(tiempo_profesor)
                TOTAL_INGRESOS += GANA_HUMANO
                TOTAL_BENEFICIO_ESTUDIANTE += BENEFICIO_ESTUDIANTE
                print(env.now, "Sale robot: ", numero, ". Gana humano ", "TP: ", tiempo_profesor, "TR: ", tiempo_robot)


            TOTAL_ROBOTS+=1




########################################################################################################################
# Inicio de la simulacion
    def __init__(self):
        env = simpy.Environment()

        # Inicio del proceso y ejecución
        servidor = simpy.Resource(env, capacity=1)
        env.process(self.llegadaRobot(env, servidor))
        env.run()
        PROMEDIO_ESPERA=np.mean(ESPERA_ROBOTS)
        print("Promedio espera ",PROMEDIO_ESPERA)
        print("Cola máxima ", MAX_COLA)
        print("Total ingresos ",TOTAL_INGRESOS)
        print("Total perdida ",TOTAL_PERDIDA)
        print("Total ganancia profesor ", TOTAL_INGRESOS-TOTAL_BENEFICIO_ESTUDIANTE)
        print("Total ganancia estudiante ", TOTAL_BENEFICIO_ESTUDIANTE - TOTAL_PERDIDA)
        print("Total robots ",TOTAL_ROBOTS)

