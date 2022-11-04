import numpy as np
from copy import deepcopy

# Omega es la probabilidad de cruza
# Mu es la probabilidad de mutation
# la población es una matriz que tiene 
# la forma 
# arboles ->      | d_{1_{a_1}} ... d_{1_{a_1}}
# delegaciones ^  |         .....
#                 | d_{20_{a_1}} ... d_{20_{a_1}}


class reReforestation:
    def __int__(self, pop_size=100, mu=0.1, omega=0.9, gen_max=1000) -> None:
        self.cols = 20
        self.rows = 16
        self.pop_size = pop_size
        self.mu = mu
        self.omega = omega
        self.gen_max = gen_max

    def count_tree(self, trees):
        return np.sum(trees.reshape(16, 10), axis=0)

    def population(self) -> np.ndarray:
        return np.random.randint(500,1000,(self.pop_size, self.cols, self.rows))

    def mutation(self, pop):
        pop_tmp = pop.copy()
        for ind in range(self.pop_size):
            if np.random.random() < self.mu:
                town, tree = [np.random.randint(0, self.cols), np.random.randint(0, self.rows)]
                pop_tmp[ind][town][tree] = np.random.randint(0, 1000)
        return pop_tmp

    def sumArea(self, trees_tmp) -> np.ndarray:
        trees_area = trees_tmp.copy()
        area = np.array([np.random.uniform(1, 3) for _ in range(10)])
        for town in range(self.rows):
            trees_area[town, :] = area * trees_area[town, :]
        return np.sum(trees_area)


    def tournament(self, pop) -> list:
        pop_tmp = pop.copy()
        result = []
        for _ in range(25):
            roundT = 0
            winner = 0
            p1 = np.random.randint(0, len(pop_tmp))
            p2 = np.random.randint(0, len(pop_tmp))
            player1 = pop_tmp[p1]
            player2 = pop_tmp[p2]
            while roundT < 8:
                if np.sum(player1) > np.sum(player2):
                    winner = player1
                    p2 = np.random.randint(0, len(pop_tmp))
                    player2 = pop_tmp[p2]
                elif np.sum(player1) == np.sum(player2):
                    winner = player2
                    p1 = np.random.randint(0, len(pop_tmp))
                    player1 = pop_tmp[p1]
                else:
                    winner = player1
                    p1 = np.random.randint(0, len(pop_tmp))
                    player1 = pop_tmp[p1]
                    p2 = np.random.randint(0, len(pop_tmp))
                    player2 = pop_tmp[p2]
                roundT += 1
            result.append(winner)
        return result


    def cross(self, father, mother) -> tuple:
        row, col = father.shape
        childO = np.zeros((row, col))
        childT = np.zeros((row, col))
        for r in range(self.rows):
            childO[r, 0:self.cols // 2] = father[r, 0:col // 2]
            childO[r, self.cols // 2:self.cols] = mother[r, self.col // 2:col]
            childT[r, 0:self.cols // 2] = mother[r, 0:self.cols // 2]
            childT[r, self.cols // 2:self.cols] = father[r, self.cols // 2:self.cols]
        return childO, childT


    def selection(self, pop, best):
        pop_cross = pop.copy()
        cross_tmp = np.zeros((self.pop_size, self.rows, self.cols))
        cross_tmp[0] = best
        father = tournament(pop_cross)
        mother = tournament(pop_cross)
        index = 1

        for i in range(self.pop_size // 4):
            if np.random.random() < self.omega:
                chil1, child2 = cross(father[i], mother[i])
                cross_tmp[index] = chil1
                cross_tmp[index+1] = chil2
            else:
                cross_tmp[index] = father[i]
                cross_tmp[index+1] = mother[i]
            index += 2
        while len(cross_tmp) > 100:
            cross_tmp.pop()
        return cross_tmp


def penalty(pop, epsilon):
    n = len(pop)
    area = np.zeros(n)
    for i in range(n):
        ic(type(pop[i]))
        area[i] = sumArea(pop[i])
    area[area > epsilon] = area[area > epsilon] * (np.random.uniform(0.5, 0.7))
    return area


def best(areaTree):
    return (np.max(areaTree), np.argmax(areaTree))


def main(epsilon=100000):
    indBest = {}
    poP = population()
    for i in range(100):
        print('generacion ', i)
        popPenalty = penalty(poP, epsilon)
        bestInd = best(popPenalty)
        indBest[bestInd[0]] = popPenalty[bestInd[1]]
        crossPop = selection(poP, poP[bestInd[1]])
        poP = mutation(crossPop)
