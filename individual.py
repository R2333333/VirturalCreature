from io import FileIO
from matplotlib import pyplot as plt
# from networkx.algorithms.bipartite.basic import color
import pyrosim
from robot import ROBOT
import numpy as np
from numpy import random as rd
import constants as C
import networkx as nx

class INDIVIDUAL:

    def __init__(self, i):
        self.ID = i
        self.genome = [(rd.random((5,7)) * 2 - 1) , (rd.random((7,8)) * 2 - 1)]
        self.fitness = 0

    def Start_Evaluation(self, env=None, eval_time=C.evalTime, play_blind=False):
        self.sim = pyrosim.Simulator(eval_time=eval_time, play_blind=play_blind, play_paused=True)
        hasLight = env is not None
        self.carry_box = False

        if hasLight:
            env.send_to(self.sim)
            hasLight = env.hasLight
            self.carry_box = env.carry_box
            if self.carry_box:
                self.p_box = env.p_box

        self.robot = ROBOT(self.sim, hasLight, self.genome)

        self.sim.assign_collision('robot', 'env')
        self.sim.assign_collision('env', 'robot')
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        pos = self.sim.get_sensor_data( sensor_id = self.robot.P4 , svi = 1 )[-1]
        self.fitness += pos if not self.carry_box else (pos + self.sim.get_sensor_data(self.p_box, svi=1)[-1]) / 2

        del(self.sim)
        return self.fitness

    def mutate(self, max_rate=C.m_rate):
        m_rate = rd.randint(max_rate - 1) + 1

        for g in self.genome:
            row = rd.randint(g.shape[0], size=m_rate)
            col = rd.randint(g.shape[1], size=m_rate)
            g[row, col] = rd.normal(g[row,col] , np.abs(g[row, col]))
            g[g > 1] = 1
            g[g< -1] = -1
        
        return self

    def print(self, precede='', to: FileIO = None):
        if to is not None:
            to.write('%8.5f' % self.fitness)
        print(f'{precede}[%i %8.5f]' % (self.ID, self.fitness), end=' ')

    def  __eq__(self, other):
        return self.fitness == other.fitness

    def draw_network(self):
        SNs = [f'SN{i}' for i in range(5)]
        HNs = [f'HN{i}' for i in range(4, 11)]
        MNs = [f'MN{i}' for i in range(4, 12)]
        BNs = ['BN0', 'BN1']

        graph = nx.Graph()
        [graph.add_edge(SN, HN, color='r') for SN in SNs for HN in HNs] 
        [graph.add_edge(HN, MN, color='g') for HN in HNs for MN in MNs]
        [graph.add_edge(BN, HN, color='b') for BN in BNs for HN in HNs]

        pos = {}
        for layer in range(3):
            pos.update((node, (layer, index)) for index, node in enumerate([SNs, HNs, MNs][layer]))

        pos.update({BNs[0]: (0.5, 7), BNs[1]: (0.5, 8)})
        colors = nx.get_edge_attributes(graph,'color').values()
        nx.draw(graph, with_labels=True, pos=pos, edge_color=colors)
        plt.show()

# INDIVIDUAL(0).draw_network()