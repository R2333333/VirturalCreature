import pyrosim
from robot import ROBOT
import numpy as np
from numpy import random as rd
import constants as C

class INDIVIDUAL:

    def __init__(self, i):
        self.ID = i
        self.genome = [(rd.random((4,8)) * 2 - 1) , (rd.random((8,8)) * 2 - 1)]
        self.fitness = 0

    def Start_Evaluation(self, env=None, eval_time=C.evalTime, play_blind=False):
        self.sim = pyrosim.Simulator(eval_time=eval_time, play_blind=play_blind, play_paused=True)
        self.hasEnv = env is not None
        self.carry_box = False
        self.robot = ROBOT(self.sim, self.hasEnv, self.genome)

        if self.hasEnv:
            env.send_to(self.sim)
            self.carry_box = env.carry_box
            if self.carry_box:
                self.p_box = env.p_box

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

    def print(self, precede=''):
        print(f'{precede}[%i %8.5f]' % (self.ID, self.fitness), end=' ')

    def  __eq__(self, other):
        return self.fitness == other.fitness
