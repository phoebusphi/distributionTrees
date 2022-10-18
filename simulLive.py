import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math as mt

def poblacion(x, a=0.0000029, N=10000):
    return (-1 / (a * x * (N - x))) * mt.log(rnd.random())

def edad(y=1 / 30):
    return (-1 / y) * mt.log(rnd.random())

class Persona:
    anoDeMuerte = 0

totalPersonas = 1000
personas = []

for _ in range(totalPersonas):
    persona_ = Persona()
    persona_.anoDeMuerte = edad()
    personas.append(persona_)

def simulacion():
    t = 0
    T = [0]
    Y = [1000]
    crecimiento = []
    while t <= 500:
        nacimiento = poblacion(totalPersonas)
        t += nacimiento
        crecimiento.append(t)

        persona = Persona()
        persona.anoDeMuerte = t + edad()
        personas.append(persona)

        for persona in personas:
            if persona.anoDeMuerte <= t:  # ya se murió
                personas.remove(persona)
        T.append(t)
        Y.append(len(personas))
    return personas
l = []
m = []
for k in range(10):
    l.append(simulacion())
    m.append(k)
    print(k)
plt.plot(m, l)
plt.show()