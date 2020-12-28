from environments import ENVIRONMENTS
from population import POPULATION
import constants as C
import pickle

envs = ENVIRONMENTS() if C.numEnvs > 0 else None

parents = POPULATION(C.popSize)
parents.evaluate(envs, True)
parents.print('  0')

for g in range(C.numGens):
    children = POPULATION(C.popSize, initialize=False)
    children.fill_from(parents)
    children.evaluate(envs, True)
    children.print('%3i' % (g + 1))
    parents = children

pickle.dump(parents.p[0], open("out3", 'wb'))
parents.evaluate(envs, best=True)

