import pyrosim
import matplotlib.pyplot as plt
from robot import ROBOT
from random import random


#create objects
for i in range(10):
    sim = pyrosim.Simulator(eval_time=200)
    robot = ROBOT(sim, random()*2 - 1)

    sim.start()
    sim.wait_to_finish()

#collect and print sensor data
sensorData = sim.get_sensor_data( sensor_id = robot.P2 )
print(sensorData)

#plot sensor data
f = plt.figure()
panel = f.add_subplot(111)
plt.plot(sensorData)
plt.show()