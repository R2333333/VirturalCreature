from copy import deepcopy
from population import POPULATION

parents = POPULATION(10)
for g in range(1,201):
    print(g, end=' ')
    children = deepcopy(parents)
    children.mutate()
    children.evaluate(play_blind=True)

    parents.replaceWith(children)
    parents.print()

parents.evaluate(best=True)


# for i in range(10):
#     child = deepcopy(parent)
#     child.mutate()
#     print(f'[g: {i}] [pw: {parent.genome}] [p: {parent.fitness}] [c: {child.evaluate(play_blind=True)}]')

#     if ( child.fitness > parent.fitness ):
#         parent = child
        # f = open('robot.p','wb')
        # pickle.dump(parent , f )
        # f.close()
        # child.evaluate()