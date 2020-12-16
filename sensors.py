import pyrosim
import matplotlib.pyplot as plt

#create objects
sim = pyrosim.Simulator()
whiteObject = sim.send_cylinder(x=0 , y=0 , z=0.6, length=1.0 , radius=0.1 )
redObject = sim.send_cylinder( x=0, y=0.5, z=1.1, r1=0, r2=1, r3=0, r=1, g=0, b=0) 

#add joints
joint = sim.send_hinge_joint( 
    first_body_id = whiteObject , 
    second_body_id = redObject, 
    n1 = 1 , n2 = 0 , n3 = 0,
    x=0, y=0, z=1.1,
    lo=-3.14159/2 , hi=3.14159/2)

#add sensors
T0 = sim.send_touch_sensor( body_id = whiteObject )
T1 = sim.send_touch_sensor( body_id = redObject )
P2 = sim.send_proprioceptive_sensor( joint_id = joint )
R3 = sim.send_ray_sensor( body_id = redObject , x = 0, y = 1, z = 1.1 , r1 = 0, r2 = 1, r3 = 0)

#start simulation
sim.start()
sim.wait_to_finish()

#collect and print sensor data
# sensorData = sim.get_sensor_data( sensor_id = T1 )
# sensorData = sim.get_sensor_data( sensor_id = P2 )
sensorData = sim.get_sensor_data( sensor_id = R3 )
print(sensorData)

#plot sensor data
f = plt.figure()
panel = f.add_subplot(111)
plt.plot(sensorData)
plt.show()