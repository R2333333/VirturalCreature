import pyrosim
from robot import ROBOT
import numpy as np
from numpy import random as rd
import constants as C

class INDIVIDUAL:

    def __init__(self, i):
        self.ID = i
        self.genome = rd.random((5,8)) * 2 - 1
        self.fitness = 0

    def Start_Evaluation(self, env=None, eval_time=C.evalTime, play_blind=False):
        self.sim = pyrosim.Simulator(eval_time=eval_time, play_blind=play_blind, play_paused=True)
        self.hasEnv = env is not None
        self.robot = ROBOT(self.sim, self.hasEnv, self.genome)

        if self.hasEnv:
            env.send_to(self.sim)

        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()

        self.fitness = self.sim.get_sensor_data( sensor_id = self.robot.P4 , svi = 1 )[-1]

        del(self.sim)
        return self.fitness

    def mutate(self, max_rate=C.m_rate):
        m_rate = rd.randint(max_rate) + 1
        row = rd.randint(len(self.genome), size=m_rate)
        col = rd.randint(len(self.genome[0]), size=m_rate)
        self.genome[row, col] = rd.normal(self.genome[row,col] , np.abs(self.genome[row, col]))
        self.genome[self.genome > 1] = 1
        self.genome[self.genome < -1] = -1
        return self

    def print(self, precede=''):
        print(f'{precede}[%i %8.5f]' % (self.ID, self.fitness), end=' ')

    def  __eq__(self, other):
        return self.fitness == other.fitness
