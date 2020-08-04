import random
import numpy
import math

class node:
    def __init__(self, para_list_queens):
        self.list_queens = para_list_queens
        self.cost = 0

    def check_cost(self):
        for i in range(len(self.list_queens)):
            for j in range(i + 1, len(self.list_queens)):
                if self.list_queens[i] == self.list_queens[j]:
                    self.cost += 1
                elif abs(self.list_queens[i] - self.list_queens[j]) == j - i:
                    self.cost += 1

    def move_random(self):
        no_of_queens = len(self.list_queens)
        index = random.randint(0, no_of_queens - 1)
        if self.list_queens[index] == no_of_queens - 1:
            self.list_queens[index] = random.randint(0, no_of_queens - 2)
        elif self.list_queens[index] == 0:
            self.list_queens[index] = random.randint(1, no_of_queens - 1)
        else:
            f = random.randint(0, 1)
            if f == 0:
                self.list_queens[index] = random.randint(self.list_queens[index] + 1, no_of_queens - 1)
            else:
                self.list_queens[index] = random.randint(0, self.list_queens[index] - 1)

#schedule
def schedule(T, k):
    return T / math.log(k+1)

def probability(delta, T):
    p = numpy.exp(delta/T)
    p *= 100
    p = int(p)
    i = random.randint(0, 100)
    if i < p:
        return 1
    else:
        return 0

def simulated_annealing(no_of_queens):
    while 1:
        list_queens = []
        for i in range(no_of_queens):
            list_queens.append(random.randint(0, no_of_queens - 1))
        current = node(list_queens)
        current.check_cost()
        t = 1
        T = 100000
        while (True):
            t += 1
            T = schedule(T,t)
            if T == 0: break

            next_list = current.list_queens[:]
            next_current = node(next_list)
            next_current.move_random()
            next_current.check_cost()

            deltaE = current.cost - next_current.cost

            if deltaE > 0:
                current = next_current
            else:
                if (probability(deltaE, T) == 1):
                    current = next_current

        if current.cost == 0:
            return current

        print(list_queens)
