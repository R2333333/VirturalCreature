from individual import INDIVIDUAL
from copy import deepcopy
import random as rd
# import numpy as np

class POPULATION:

    def __init__(self, popSize=5, initialize=True):
        # self.popSize = popSize
        if initialize:
            self.p = [INDIVIDUAL(i) for i in range(popSize)]
        else:
            self.p = []
        
    def print(self, precede=''):
        if len(self.p) > 0:    
            [p.print(precede) for p in self.p]
        print()    
        
    def evaluate(self, play_blind=False, best=False):
        if best:
            self.eval_best()
        else:
            [p.Start_Evaluation(play_blind=play_blind) for p in self.p]
            [p.Compute_Fitness() for p in self.p]

    def eval_best(self):
        best = max(self.p, key=lambda i: i.fitness)
        best.Start_Evaluation()
        best.Compute_Fitness()
        
    def mutate(self):
        [p.mutate() for p in self.p]

    def replaceWith(self, other):
        for i in range(len(self.p)):
            self.p[i] = other.p[i] if other.p[i].fitness > self.p[i].fitness else self.p[i]

    def fill_from(self, other):
        self.copy_best_from(other)
        self.collect_children_from(other)

    def copy_best_from(self, other):
        self.p.append(deepcopy(max(other.p, key=lambda i: i.fitness)))

    def collect_children_from(self, other):
        for i in other.p[1:]:
            winner = deepcopy(self.winner_of_tournament_selection(other))
            self.p.append(winner if not winner in self.p else winner.mutate())

    def winner_of_tournament_selection(self, other):
        p1, p2 = 0, 0
        while p1 == p2:
            p1, p2 = [other.p[rd.randint(0, len(other.p) - 1)] for i in [1,2]]

        return max(p1, p2, key=lambda p: p.fitness)
