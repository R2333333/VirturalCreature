import pyrosim
from robot import ROBOT
import random as rd
import math
from numpy import random
import constants as C

class INDIVIDUAL:

    def __init__(self, i):
        self.ID = i
        self.genome = random.random((5,8)) * 2 - 1
        self.fitness = 0

    def Start_Evaluation(self, env, eval_time=C.evalTime, play_blind=False):
        self.sim = pyrosim.Simulator(eval_time=eval_time, play_blind=play_blind, play_paused=True)
        self.robot = ROBOT(self.sim, self.genome)
        env.send_to(self.sim)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        self.fitness += self.sim.get_sensor_data( sensor_id = self.robot.L4 )[-1]
        del(self.sim)
        return self.fitness

    def mutate(self):
        row = rd.randint(0,len(self.genome) - 1)
        col = rd.randint(0, len(self.genome[0]) - 1)
        mutatedVal = rd.gauss(self.genome[row][col] , math.fabs(self.genome[row][col]))
        self.genome[row][col] = 1 if mutatedVal > 1 else (-1 if mutatedVal < -1 else mutatedVal)
        return self

    def print(self, precede=''):
        print(f'{precede}[%i %8.5f]' % (self.ID, self.fitness), end=' ')

    def  __eq__(self, other):
        return self.fitness == other.fitness