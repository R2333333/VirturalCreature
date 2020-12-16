import pyrosim
from robot import ROBOT
from random import random


class INDIVIDUAL:

    def __init__(self):
        self.genome = random() * 2 - 1
        self.fitness = 0

    def evaluate(self):
        sim = pyrosim.Simulator(eval_time=1000)
        robot = ROBOT(sim, self.genome)

        sim.start()
        sim.wait_to_finish()

        self.fitness = sim.get_sensor_data( sensor_id = robot.P4 , svi = 1 )[-1]
