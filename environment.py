import constants as C
class ENVIRONMENT:
    def __init__(self, id) -> None:
        pos = ['up_stairs', 'maze', 'hurdle', 'down_stairs']
        self.ID = id
        self.l, self.w, self.h = [C.L] * 3
        getattr(self, f'{pos[id]}')()

    def up_stairs(self):        
        self.l1 = 5*C.L
        self.w1 = 300*C.L
        self.h1 = 0.3*C.L
        self.x1 = 0
        self.y1 = 10*C.L
        self.z1 = 0.3*C.L/2
        
        self.l2 = 5*C.L
        self.w2 = 300*C.L
        self.h2 = 0.6*C.L
        self.x2 = 0
        self.y2 = 15*C.L
        self.z2 = 0.6*C.L/2
        
        self.l3 = 5*C.L
        self.w3 = 300*C.L
        self.h3 = 0.9*C.L
        self.x3 = 0
        self.y3 = 20*C.L
        self.z3 = 0.9*C.L/2
        
        self.l4 = 5*C.L
        self.w4 = 300*C.L
        self.h4 = 1.2*C.L
        self.x4 = 0
        self.y4 = 25*C.L
        self.z4 = 1.2*C.L/2

    def maze(self):
        self.l1 = 0.5*C.L
        self.w1 = 300*C.L
        self.h1 = 10*C.L
        self.x1 = 145*C.L
        self.y1 = 5*C.L
        self.z1 = 10*C.L/2
        
        self.l2 = 0.5*C.L
        self.w2 = 300*C.L
        self.h2 = 10*C.L
        self.x2 = -140*C.L
        self.y2 = 15*C.L
        self.z2 = 10*C.L/2
        
        self.l3 = 0.5*C.L
        self.w3 = 300*C.L
        self.h3 = 10*C.L
        self.x3 = -170*C.L
        self.y3 = 25*C.L
        self.z3 = 10*C.L/2
        
        self.l4 = 0.5*C.L
        self.w4 = 300*C.L
        self.h4 = 10*C.L
        self.x4 = 140*C.L
        self.y4 = 25*C.L
        self.z4 = 10*C.L/2

    def hurdle(self):
        self.l1 = C.L
        self.w1 = 300*C.L
        self.h1 = 0.9*C.L
        self.x1 = 0
        self.y1 = 10*C.L
        self.z1 = 0.9*C.L/2
        
        self.l2 = C.L
        self.w2 = 300*C.L
        self.h2 = 0.9*C.L
        self.x2 = 0
        self.y2 = 15*C.L
        self.z2 = 0.9*C.L/2
        
        self.l3 = C.L
        self.w3 = 300*C.L
        self.h3 = 0.9*C.L
        self.x3 = 0
        self.y3 = 20*C.L
        self.z3 = 0.9*C.L/2
        
        self.l4 = C.L
        self.w4 = 300*C.L
        self.h4 = 0.9*C.L
        self.x4 = 0
        self.y4 = 25*C.L
        self.z4 = 0.9*C.L/2

    def down_stairs(self):
        self.l1 = 5*C.L
        self.w1 = 300*C.L
        self.h1 = 0.5*C.L
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0.5*C.L/2
        
        self.l2 = 5*C.L
        self.w2 = 300*C.L
        self.h2 = 1*C.L
        self.x2 = 0
        self.y2 = 5*C.L
        self.z2 = 1*C.L/2
        
        self.l3 = 5*C.L
        self.w3 = 300*C.L
        self.h3 = 0.7*C.L
        self.x3 = 0
        self.y3 = 10*C.L
        self.z3 = 0.7*C.L/2
        
        self.l4 = 5*C.L
        self.w4 = 300*C.L
        self.h4 = 0.3*C.L
        self.x4 = 0
        self.y4 = 15*C.L
        self.z4 = 0.3*C.L/2

    def send_to(self, sim):

        object1 = sim.send_box(x=self.x1, y=self.y1, z=self.z1, length=self.l1, width=self.w1, height=self.h1, mass = 100, collision_group = 'env')
        
        object2 = sim.send_box(x=self.x2, y=self.y2, z=self.z2, length=self.l2, width=self.w2, height=self.h2, mass = 100, collision_group = 'env')
        
        object3 = sim.send_box(x=self.x3, y=self.y3, z=self.z3, length=self.l3, width=self.w3, height=self.h3, mass = 100, collision_group = 'env')
        
        object4 = sim.send_box(x=self.x4, y=self.y4, z=self.z4, length=self.l4, width=self.w4, height=self.h4, mass = 100, collision_group = 'env')

        self.lightSource = sim.send_box(x=0, y=35*C.L, z=C.L/2, length=C.L, width=C.L, height=C.L)
        sim.send_light_source(body_id = self.lightSource)

        sim.assign_collision('robot', 'env')
        sim.assign_collision('env', 'robot')


        
