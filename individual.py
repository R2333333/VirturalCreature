from io import FileIO
from matplotlib import pyplot as plt
from numpy.core.defchararray import equal
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
        self.hasLight = False
        self.fitness = 0

    def Start_Evaluation(self, env=None, eval_time=C.evalTime, play_blind=False):
        self.sim = pyrosim.Simulator(eval_time=eval_time, play_blind=play_blind, play_paused=True)
        self.hasLight = env is not None
        self.carry_box = False

        if self.hasLight:
            env.send_to(self.sim)
            self.hasLight = env.hasLight
            self.carry_box = env.carry_box
            if self.carry_box:
                self.p_box = env.p_box

        self.robot = ROBOT(self.sim, self.hasLight, self.genome)

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
        gene_shape = [g.shape for g in self.genome] if self.hasLight \
            else     [g.shape - i for g, i in zip(self.genome, [1, [1,0]])]

        for g in [0,1]:
            curr_g = self.genome[g]
            row = rd.randint(gene_shape[g][0], size=m_rate)
            col = rd.randint(gene_shape[g][1], size=m_rate)
            curr_g[row, col] = rd.normal(curr_g[row,col] , np.abs(curr_g[row, col]))
        
            curr_g[curr_g > 1] = 1
            curr_g[curr_g < -1] = -1
        
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
        [graph.add_edge(BNs[0], HN, color='b') for HN in HNs]
        [graph.add_edge(BNs[1], MN, color='b') for MN in MNs]

        pos = {}
        for layer in range(3):
            pos.update((node, (layer, index)) for index, node in enumerate([SNs, HNs, MNs][layer]))

        pos.update({BNs[0]: (0.5, 7), BNs[1]: (1.5, 8)})
        colors = nx.get_edge_attributes(graph,'color').values()
        nx.draw(graph, with_labels=True, pos=pos, edge_color=colors)
        plt.show()

# INDIVIDUAL(0).draw_network()