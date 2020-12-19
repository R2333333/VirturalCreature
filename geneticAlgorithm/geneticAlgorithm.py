from copy import deepcopy
from environments import ENVIRONMENTS
from geneticAlgorithm import population as p
import constants as C

envs = ENVIRONMENTS()

parents = p.POPULATION(10)
parents.evaluate(True)
parents.print('  0')


for g in range(C.numGens):
    children = p.POPULATION(initialize=False)
    children.fill_from(parents)
    children.evaluate(True)
    children.print('%3i' % (g+1))
    parents = children

parents.evaluate(best=True)
