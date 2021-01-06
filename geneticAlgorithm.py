from io import FileIO
from environments import ENVIRONMENTS
from population import POPULATION
import constants as C
import pickle

def genetic_algorithm(pop_size=C.popSize, playback=None, play_result=True, store_fitness: FileIO = None):
    parents = POPULATION(pop_size)
    parents.evaluate(envs, True)
    parents.print('  0')

    for g in range(C.numGens):
        children = POPULATION(pop_size, initialize=False)
        children.fill_from(parents)
        children.evaluate(envs, True)
        children.print('%3i' % (g + 1))
        parents = children

    if playback is not None:
        pickle.dump(parents.p[0], open(playback, 'wb'))

    if play_result:
        parents.evaluate(envs, best=True)

    if store_fitness is not None:
        parents.p[0].print(to=store_fitness)
    

def test_loop(pop_range: list, t_fraction: float, m_fraction: float):
    with open('data_out.csv', 'w') as output: 
        output.write('pop_size,t_size,m_rate,score')

        for pop_size in range(*pop_range):
            
            for t_size in range(1, int(t_fraction * pop_size) + 1, int(pop_size/10)):
                C.set_cons('t_size', t_size)
                
                for m_rate in range(1, int(m_fraction * pop_size) + 1, int(pop_size/10)):

                    C.set_cons('m_rate', m_rate)
                    output.write(f'\n{pop_size},{t_size},{m_rate}')
                    genetic_algorithm(pop_size, f'p{pop_size}t{t_size}m{m_rate}', False, output)


envs = ENVIRONMENTS() if C.numEnvs > 0 else None
test_loop([10, 25, 5], 0.7, 0.5)