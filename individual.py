import pyrosim
from robot import ROBOT
import random as rd
import math


class INDIVIDUAL:

    def __init__(self):
        self.genome = rd.random() * 2 - 1
        self.fitness = 0

    def evaluate(self, eval_time=1000, play_blind = False):
        sim = pyrosim.Simulator(eval_time=eval_time, play_blind=play_blind)
        robot = ROBOT(sim, self.genome)

        sim.start()
        sim.wait_to_finish()

        self.fitness = sim.get_sensor_data( sensor_id = robot.P4 , svi = 1 )[-1]
        return self.fitness

    def mutate(self):
        self.genome = rd.gauss( self.genome , math.fabs(self.genome) )