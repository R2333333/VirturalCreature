# import matplotlib.pyplot as plt
# import pickle
# from robot import ROBOT
# from individual import INDIVIDUAL
from copy import deepcopy
from population import POPULATION

parents = POPULATION(5)
print(end='  ')
parents.evaluate(play_blind=True)
parents.print()


for g in range(1,100):
    print(g, end=' ')
    children = deepcopy(parents)
    children.mutate()
    children.evaluate(play_blind=True)

    parents.replaceWith(children)
    parents.print()

# for i in range(100):
#     child = deepcopy(parent)
#     child.mutate()
#     print(f'[g: {i}] [pw: {parent.genome}] [p: {parent.fitness}] [c: {child.evaluate(play_blind=True)}]')

#     if ( child.fitness > parent.fitness ):
#         parent = child
#         # f = open('robot.p','wb')
#         # pickle.dump(parent , f )
#         # f.close()
#         # child.evaluate()