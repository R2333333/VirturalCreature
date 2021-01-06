from io import FileIO
import numpy as np
from individual import INDIVIDUAL
from copy import deepcopy
import random as rd
import constants as C

class POPULATION:

    def __init__(self, popSize=5, initialize=True):
        if initialize:
            self.p = [INDIVIDUAL(i) for i in range(popSize)]
        else:
            self.p = []
        
    def print(self, precede='', to: FileIO = None):
        if len(self.p) > 0: 
            print(precede, end=' ')   
            [p.print(to=to) for p in self.p]
        print()    
        
    def evaluate(self, envs=None, play_blind=False, best=False):
        if best:
            if envs is not None:
                [self.eval_best(envs.envs[i]) for i in envs.envs]
            else:
                self.eval_best(envs)

        elif envs is not None:
            for p in self.p:
                p.fitness = 0

            for e in envs.envs:
                [p.Start_Evaluation(envs.envs[e], play_blind=play_blind) for p in self.p]
                [p.Compute_Fitness() for p in self.p]

            for p in self.p:
                p.fitness /= len(envs.envs)

        else:
            [p.Start_Evaluation(play_blind=play_blind) for p in self.p]
            [p.Compute_Fitness() for p in self.p]

    def eval_best(self, envs):
        self.p[0].Start_Evaluation(envs)
        self.p[0].Compute_Fitness()

    def mutate(self):
        for i in range(C.m_rate):
            [p.mutate() for p in self.p]

    def replaceWith(self, other):
        for i in range(len(self.p)):
            self.p[i] = other.p[i] if other.p[i].fitness > self.p[i].fitness else self.p[i]

    def fill_from(self, other):
        self.copy_best_from(other)
        self.collect_children_from(other)
        index = np.argmin(list(map(lambda p: p.fitness, self.p)))
        self.p[index if index != 0 or len(self.p) == 1 else 1] = deepcopy(self.p[0]).mutate()

    def copy_best_from(self, other):
        self.p.append(deepcopy(max(other.p, key=lambda i: i.fitness)))

    def collect_children_from(self, other):
        for i in other.p[1:]:
            winner1 = deepcopy(self.winner_of_tournament_selection(other))
            winner2 = deepcopy(self.winner_of_tournament_selection(other))
            child1, child2 = self.crossover(winner1, winner2)
            winner = max(winner1, winner2, child1, child2, key=lambda p: p.fitness)
            self.p.append(winner if winner not in self.p else winner.mutate())

    def winner_of_tournament_selection(self, other):
        return max(rd.sample(other.p, k=C.t_size), key=lambda p: p.fitness)

    def crossover(self, parent1, parent2):
        for g in range(len(parent1.genome)):
            cross_amount = np.random.randint(parent1.genome[g].shape[0]*parent1.genome[g].shape[1]-1)
            row = np.random.randint(parent1.genome[g].shape[0], size=cross_amount)
            col = np.random.randint(parent1.genome[g].shape[1], size=cross_amount)

            child1 = deepcopy(parent1)
            child2 = deepcopy(parent2)
            
            child1.genome[g][row, col] = child2.genome[g][row, col]
            child2.genome[g][row, col] = child1.genome[g][row, col]

        return child1, child2
