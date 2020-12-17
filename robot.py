class ROBOT:

    def __init__(self, sim, wts=[-1, -1, -1, -1]):
        whiteObject = sim.send_cylinder(x=0 , y=0 , z=0.6, length=1.0 , radius=0.1 )
        redObject = sim.send_cylinder( x=0, y=0.5, z=1.1, r1=0, r2=1, r3=0, r=1, g=0, b=0) 
       
        #add joints
        joint = sim.send_hinge_joint( 
            first_body_id = whiteObject , 
            second_body_id = redObject, 
            n1 = -1 , n2 = 0 , n3 = 0,
            x=0, y=0, z=1.1,
            lo=-3.14159/2 , hi=3.14159/2)

        #add motor neuron
        MN2 = sim.send_motor_neuron( joint_id = joint)
        motorNeurons = [MN2]

        #add sensors
        self.T0 = sim.send_touch_sensor( body_id = whiteObject )
        self.T1 = sim.send_touch_sensor( body_id = redObject )
        self.P2 = sim.send_proprioceptive_sensor( joint_id = joint )
        self.R3 = sim.send_ray_sensor( body_id = redObject , x = 0, y = 1, z = 1.1 , r1 = 0, r2 = 1, r3 = 0)
        self.P4 = sim.send_position_sensor( body_id = redObject )

        #add neurons
        self.SN0 = sim.send_sensor_neuron( sensor_id = self.T0 )
        self.SN1 = sim.send_sensor_neuron(sensor_id=self.T1)
        self.SN2 = sim.send_sensor_neuron(sensor_id=self.P2)
        self.SN3 = sim.send_sensor_neuron(sensor_id=self.R3)

        #add synapses
        for s in range(4):
            for m in motorNeurons:
                sim.send_synapse(source_neuron_id = eval("self.SN" + str(s)) , target_neuron_id = m, weight = wts[s] )
             
