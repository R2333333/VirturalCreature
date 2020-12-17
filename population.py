from individual import INDIVIDUAL
# import numpy as np

class POPULATION:

    def __init__(self, popSize=5):
        self.p = [INDIVIDUAL(i) for i in range(popSize)]
        
    def print(self):    
        [p.print() for p in self.p]
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