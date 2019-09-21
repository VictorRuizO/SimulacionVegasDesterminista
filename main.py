from determinista import *
from maestrovegas import *
from simulacion import *
from Escenario1 import *
from Escenario2 import *
from Escenario3 import *
import  time

"""
n=6
P = Profesor(n)
P.setEne(4)
v=np.array([])
for i in range(100):
    v=np.append(v,P.getTime())

print(np.mean(v))

M=MaestroVegas(0)
M.setEne(4)
v=np.array([])
for i in range(100):
    v=np.append(v,M.getTime())

print(np.mean(v))
"""
#GUI=Interfaz()

#GUI=Interfaz()
#Simulacion()
Escenario3()

""" Pruebas Intentos
m = MaestroVegas(12)
for i in range(0,100):
    fallos=0
    while not(m.columnas()):
        fallos+=1

    print(fallos)
    
"""

""" Pruebas Tiempo
m = MaestroVegas(15)
for i in range(0,100):
    inicio_de_tiempo = time.time()

    fallos=0
    while not(m.columnas()):
        fallos+=1

    tiempo_final = time.time()
    tiempo_transcurrido = tiempo_final - inicio_de_tiempo
    print(tiempo_transcurrido)
"""