import pyrosim

sim = pyrosim.Simulator(play_paused=True, eval_time=100)
whiteObject = sim.send_cylinder(x=0 , y=0 , z=0.6, length=1.0 , radius=0.1 )
redObject = sim.send_cylinderredObject = sim.send_cylinder( x=0.5 , y=0, z=1.1, r1=1, r2=0, r3=0, r=1, g=0, b=0) 

joint = sim.send_hinge_joint( 
    first_body_id = whiteObject , 
    second_body_id = redObject, 
    n1 = 0 , n2 = 1 , n3 = 0,
    x=0, y=0, z=1.1,
    lo=-3.14159/2 , hi=3.14159/2)

sim.start()

sim.wait_to_finish()

