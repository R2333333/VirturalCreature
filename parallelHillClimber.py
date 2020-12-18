from copy import deepcopy
from population import POPULATION

parents = POPULATION(10)
print('running...')
for g in range(1,201):
    # print(g, end=' ')
    children = deepcopy(parents)
    children.mutate()
    children.evaluate(play_blind=True)

    parents.replaceWith(children)
    # parents.print()
    print('.', end='', flush=True)

print()
parents.evaluate(best=True)

