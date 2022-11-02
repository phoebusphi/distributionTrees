import numpy as np


# Omega es la probabilidad de cruza
# Mu es la probabilidad de mutation
#
class reReforestation:
    def __int__(self, pop_size=100, mu=0.1, omega=0.9, gen_max=1000) -> None:
        self.pop_size = pop_size
        self.mu = mu
        self.omega = omega
        self.gen_max = gen_max

    def count_tree(self, trees):
        return np.sum(trees.reshape(16, 10), axis=0)

    def population(self):
        return [np.random.randint(900, 1000, (16, 10)) for _ in range(self.pop_size)]


def sumArea(trees_tmp):
    np.random.seed(1)
    trees_area = deepcopy(trees_tmp)
    ic(type(trees_area))
    towns = trees_area.shape[0]
    area = np.array([np.random.uniform(1, 3) for _ in range(10)])
    for town in range(towns):
        trees_area[town, :] = area * trees_area[town, :]

    return np.sum(trees_area)


def mutation(pop, pMut=0.1):
    pop_tmp = deepcopy(pop)
    n = len(pop_tmp)
    for ind in range(n):
        if np.random.random() < pMut:
            town = np.random.randint(0, 16)
            tree = np.random.randint(0, 10)
            pop_tmp[ind][town][tree] = np.random.randint(0, 1000)
    return pop_tmp


def tournament(pop):
    pop_tmp = deepcopy(pop)
    result = []
    for _ in range(25):
        roundT = 0
        p1 = np.random.randint(0, len(pop_tmp))
        p2 = np.random.randint(0, len(pop_tmp))
        player1 = pop_tmp[p1]
        player2 = pop_tmp[p2]
        winner = 0
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
        # print(result)
        # input()
    return result


def cross(father, mother):
    row, col = father.shape
    childO = np.zeros((row, col))
    childT = np.zeros((row, col))
    for r in range(row):
        childO[r, 0:col // 2] = father[r, 0:col // 2]
        childO[r, col // 2:col] = mother[r, col // 2:col]
        childT[r, 0:col // 2] = mother[r, 0:col // 2]
        childT[r, col // 2:col] = father[r, col // 2:col]
    return [childO, childT]


def selection(pop, best, pCross=0.9):
    pop_cross = deepcopy(pop)
    n = len(pop_cross)
    cross_tmp = []
    cross_tmp.append(best)
    father = tournament(pop_cross)
    mother = tournament(pop_cross)
    for i in range(n // 4):
        if np.random.random() < pCross:
            children = cross(father[i], mother[i])
            cross_tmp.extend(children)
        else:
            cross_tmp.append(father[i])
            cross_tmp.append(mother[i])
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
