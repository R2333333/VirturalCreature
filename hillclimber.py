import matplotlib.pyplot as plt
import pickle
from robot import ROBOT
from individual import INDIVIDUAL
from copy import deepcopy

#create objects
parent = INDIVIDUAL()
print(parent.evaluate(play_blind=True))

for i in range(100):
    child = deepcopy(parent)
    child.mutate()
    print(f'[g: {i}] [pw: {parent.genome}] [p: {parent.fitness}] [c: {child.evaluate(play_blind=True)}]')

    if ( child.fitness > parent.fitness ):
        parent = child
        # f = open('robot.p','wb')
        # pickle.dump(parent , f )
        # f.close()
        # child.evaluate()