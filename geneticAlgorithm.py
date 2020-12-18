from copy import deepcopy
from population import POPULATION

parents = POPULATION(10)
parents.evaluate(True)
parents.print('  0 ')


for g in range(1,201):
    children = POPULATION(initialize=False)
    children.fill_from(parents)
    children.evaluate(True)
    children.print('%3i' % g)
    parents = children

parents.evaluate(best=True)
