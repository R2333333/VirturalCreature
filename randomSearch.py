import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL

#create objects
for i in range(10):
    individual = INDIVIDUAL()
    individual.evaluate()
    print(individual.fitness)

#plot sensor data
# f = plt.figure()
# panel = f.add_subplot(111)
# plt.plot(y)
# plt.show()