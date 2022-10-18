# En este programa realizaremos la simulación de la vida de un arbol
# suponiendo que los arboles siguen una distribución de vida similar
# que los seres humanos ya que son seres multicelulares.
#
# Tomaremos el tiempo total de vida por día y vamos hacer que
#
# Las condiciones que tiene el arbol deben de variar dependiendo de cada
# la tabla llevara los siguientes elementos
#
# __ Una suposición importante es que se va a suponer que todos los
# arboles van a tener la misma cantidad de agua y cuidados.
# Claves
# id
# fechaPlantacion
# tipoArbol
# tiempoVidaPromedio
# tiempoRiegoPromedio
# CantidadTotalPM10
# CantidadAgua
#

# Lo que vamos hacer es dado la cantidad de arboles que generamos 
# vamos hacer la siguiente prueba como se cuales arboles correspoden a cada 
# arbol y por delegación vamos hacer la simulación


import numpy as np
from random import random
from math import log


class Tree:
    yearDead = 0


class SimLiveTree:
    def __init__(self, tree_, count_trees):
        self.count_trees = count_trees
        self.type_trees = {'uno': 1}
        self.tree_ = tree_

    def trees_population(self, x, a=0.0000095, pop_max=2000):
        return (-1 / (a * x * (pop_max - x))) * log(random())

    def tree_age(self):
        return self.tree_ * log(random())

    def sim_live_tree(self):
        pop = []
        for tree in range(self.count_trees):
            tree = Tree()
            tree.yearDead = self.tree_age()
            print(dir(tree))
            input()
            pop.append(tree)
        return pop

    def simulation(self):
        pop = self.sim_live_tree()
        T = [0]
        Y = [1000]
        t = 0
        tree_live = self.count_trees
        increase = []
        while t <= 365:
            birth = self.trees_population(self.count_trees)
            t += birth
            increase.append(t)
            tree = Tree()
            tree.yearDead = t + self.tree_age()
            pop.append(tree)
            i = 0
            for tree in pop:
                if tree.yearDead <= t:
                    pop.remove(tree)
                i += 1
            T.append(t)
            Y.append(len(pop))
            tree_live = len(pop)
        return T, Y
