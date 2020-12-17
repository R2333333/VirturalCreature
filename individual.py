import pyrosim
from robot import ROBOT
import random as rd
import math
import numpy as np

class INDIVIDUAL:

    def __init__(self, i):
        self.ID = i
        self.genome = np.random.random(4) * 2 - 1
        self.fitness = 0

    def Start_Evaluation(self, eval_time=1000, play_blind=False):
        self.sim = pyrosim.Simulator(eval_time=eval_time, play_blind=play_blind)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        self.fitness = self.sim.get_sensor_data( sensor_id = self.robot.P4 , svi = 1 )[-1]
        del(self.sim)
        return self.fitness

    def mutate(self):
        num = rd.randint(0,3)
        self.genome[num] = rd.gauss( self.genome[num] , math.fabs(self.genome[num]) )

    def print(self):
        print(f'[%i %8.5f]' % (self.ID, self.fitness), end=' ')