import pyrosim
import constants as C
from random import random
from environments import ENVIRONMENTS
class ROBOT:

    def __init__(self, sim, light=False, wts=[]):
        self.light = light
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)

    def send_objects(self,sim):
        self.O0 = sim.send_box(x=0, y=0, z=C.L + C.R, length=C.L, width=C.L, height=2*C.R, r=0.5, g=0.5, b=0.5, collision_group = 'robot')
        self.O1 = sim.send_cylinder( x=0, y=C.L, z=C.L + C.R, length=C.L, radius=C.R, r1=0, r2=1, r3=0, r=1, g=0, b=0, collision_group = 'robot')
        self.O2 = sim.send_cylinder( x=C.L, y=0, z=C.L + C.R, length=C.L, radius=C.R, r1=1, r2=0, r3=0, r=0, g=1, b=0, collision_group = 'robot')
        self.O3 = sim.send_cylinder( x=0, y=-C.L, z=C.L + C.R, length=C.L, radius=C.R, r1=0, r2=1, r3=0, r=0, g=0, b=1, collision_group = 'robot')
        self.O4 = sim.send_cylinder( x=-C.L, y=0, z=C.L + C.R, length=C.L, radius=C.R, r1=1, r2=0, r3=0, r=0.5, g=0, b=0.5, collision_group = 'robot')
        self.O5 = sim.send_cylinder( x=0, y=1.5*C.L, z=C.L/2 + C.R, length=C.L, radius=C.R, r=1, g=0, b=0, collision_group = 'robot')
        self.O6 = sim.send_cylinder( x=1.5*C.L, y=0, z=C.L/2 + C.R, length=C.L, radius=C.R, r=0, g=1, b=0, collision_group = 'robot')
        self.O7 = sim.send_cylinder( x=0, y=-1.5*C.L, z=C.L/2 + C.R, length=C.L, radius=C.R, r=0, g=0, b=1, collision_group = 'robot')
        self.O8 = sim.send_cylinder( x=-1.5*C.L, y=0, z=C.L/2 + C.R, length=C.L, radius=C.R, r=0.5, g=0, b=0.5, collision_group = 'robot')

    def send_joints(self,sim):
        #add joints
        self.J0 = sim.send_hinge_joint(
            first_body_id = self.O0,
            second_body_id = self.O1,
            n1 = -1 , n2 = 0 , n3 = 0,
            x=0, y=C.L/2, z=C.L + C.R)

        self.J1 = sim.send_hinge_joint(
            first_body_id = self.O1,
            second_body_id = self.O5,
            n1 = -1 , n2 = 0 , n3 = 0,
            x=0, y=C.L*1.5, z=C.L + C.R)

        self.J2 = sim.send_hinge_joint(
            first_body_id = self.O0,
            second_body_id = self.O2,
            n1 = 0 , n2 = 1 , n3 = 0,
            x=C.L/2, y=0, z=C.L + C.R)

        self.J3 = sim.send_hinge_joint(
            first_body_id = self.O2,
            second_body_id = self.O6,
            n1 = 0 , n2 = 1 , n3 = 0,
            x=1.5*C.L, y=0, z=C.L + C.R)

        self.J4 = sim.send_hinge_joint(
            first_body_id = self.O0,
            second_body_id = self.O3,
            n1 = 1 , n2 = 0 , n3 = 0,
            x=0, y=-C.L/2, z=C.L + C.R)

        self.J5 = sim.send_hinge_joint(
            first_body_id = self.O3,
            second_body_id = self.O7,
            n1 = 1 , n2 = 0 , n3 = 0,
            x=0, y=-C.L*1.5, z=C.L + C.R)

        self.J6 = sim.send_hinge_joint(
            first_body_id = self.O0,
            second_body_id = self.O4,
            n1 = 0 , n2 = -1 , n3 = 0,
            x=-C.L/2, y=0, z=C.L + C.R)

        self.J7 = sim.send_hinge_joint(
            first_body_id = self.O4,
            second_body_id = self.O8,
            n1 = 0 , n2 = -1 , n3 = 0,
            x=-C.L*1.5, y=0, z=C.L + C.R)


    def send_sensors(self,sim):
        #add position sensor
        self.P4 = sim.send_position_sensor( body_id = self.O0 )
        #add light sensor
        if self.light:
            self.L4 = sim.send_light_sensor( body_id = self.O0 )
        #add touch sensor
        [setattr(self, f'T{i - 5}', sim.send_touch_sensor( body_id = getattr(self, f'O{i}'))) for i in range(5,9)]
        #delete temporary objects

    def send_neurons(self,sim):
        #add sensor neurons
        [setattr(self, f'SN{i}', sim.send_sensor_neuron( sensor_id = getattr(self, f'T{i}'))) for i in range(4)]
        if self.light :
            self.SN4 = sim.send_sensor_neuron(sensor_id=self.L4)
        #add motor neuron
        [setattr(self, f'MN{i + 4}', sim.send_motor_neuron( joint_id = getattr(self,f'J{i}'), tau=C.tau)) for i in range(8)]

        #add bias neurons
        [setattr(self, f'B{i}', sim.send_bias_neuron()) for i in range(2)]

        #add hidden neurons
        [setattr(self, f'H{i + 4}', sim.send_hidden_neuron()) for i in range(7 if self.light else 6)]

    def send_synapses(self,sim: pyrosim.Simulator,wts):
        # add synapses: sensors --> hidden layer --> motor
        neuron_num = 5 if self.light else 4
        for i in range(neuron_num):
            for j in range(neuron_num + 2):
                sim.send_synapse(getattr(self, f'SN{i}'), getattr(self, f'H{j+4}'), wts[0][i,j])

        for i in range(neuron_num + 2):
            for j in range(4, 12):
                sim.send_synapse(getattr(self, f'H{i+4}'), getattr(self, f'MN{j}'), wts[1][i,j-4])

        # add synapses for bias into hidden and motor neuron/output layerlayer
        for i in range(neuron_num + 2):
            sim.send_synapse(getattr(self, f'B{0}'), getattr(self, f'H{i+4}'), 1 / (neuron_num + 2))

        for i in range(4,12):
            sim.send_synapse(getattr(self, f'B{1}'), getattr(self, f'MN{i}'), 1 / 8)
