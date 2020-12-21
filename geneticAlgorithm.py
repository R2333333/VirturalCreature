from environments import ENVIRONMENTS
from population import POPULATION
import constants as C

envs = ENVIRONMENTS()

parents = POPULATION(C.popSize)
parents.evaluate(envs, True)
parents.print('  0')

for g in range(C.numGens):
    children = POPULATION(C.popSize, initialize=False)
    children.fill_from(parents)
    children.evaluate(envs, True)
    children.print('%3i' % (g + 1))
    parents = children

parents.evaluate(envs, best=True)
