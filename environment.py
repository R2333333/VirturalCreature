import pyrosim
import constants as C
class ENVIRONMENT:
    def __init__(self, id) -> None:
        pos = ['empty', 'carry','hurdle', 'up_stairs']
        self.ID = id
        self.l, self.w, self.h = [C.L] * 3
        self.carry_box = False
        self.hasLight = False
        getattr(self, f'{pos[id]}')()

    #an empty environment
    def empty(self):
        pass

    def carry(self):
        self.l1 = 2 * C.L
        self.w1 = 2 * C.L
        self.h1 = 2 * C.R
        self.x1 = 0
        self.y1 = 0
        self.z1 = C.L + C.R + 2*C.R
        self.carry_box = True

    def hurdle(self):
        self.l1 = C.L
        self.w1 = 300 * C.L
        self.h1 = 0.9 * C.L
        self.x1 = 0
        self.y1 = 10 * C.L
        self.z1 = 0.9 * C.L/2

        self.l2 = C.L
        self.w2 = 300 * C.L
        self.h2 = 0.9 * C.L
        self.x2 = 0
        self.y2 = 15 * C.L
        self.z2 = 0.9 * C.L/2

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

        self.hasLight = True

    def up_stairs(self):
        self.l1 = 5 * C.L
        self.w1 = 300 * C.L
        self.h1 = 0.3 * C.L
        self.x1 = 0
        self.y1 = 10 * C.L
        self.z1 = 0.3 * C.L/2

        self.l2 = 5 * C.L
        self.w2 = 300 * C.L
        self.h2 = 0.6 * C.L
        self.x2 = 0
        self.y2 = 15 * C.L
        self.z2 = 0.6 * C.L/2

        self.l3 = 5 * C.L
        self.w3 = 300 * C.L
        self.h3 = 0.9 * C.L
        self.x3 = 0
        self.y3 = 20 * C.L
        self.z3 = 0.9 * C.L/2

        self.l4 = 5 * C.L
        self.w4 = 300 * C.L
        self.h4 = 1.2 * C.L
        self.x4 = 0
        self.y4 = 25 * C.L
        self.z4 = 1.2 * C.L/2

        self.hasLight = True

    def send_to(self, sim: pyrosim.pyrosim.Simulator):
        objects = {}
        if self.ID != 0:
            objects[0] = sim.send_box(x=self.x1, y=self.y1, z=self.z1, length=self.l1, width=self.w1, height=self.h1, mass = 0.5 if self.ID == 1 else 100, collision_group = 'env')
            
            if self.ID != 1:
                objects[1] = sim.send_box(x=self.x2, y=self.y2, z=self.z2, length=self.l2, width=self.w2, height=self.h2, mass = 100, collision_group = 'env')
                objects[2] = sim.send_box(x=self.x3, y=self.y3, z=self.z3, length=self.l3, width=self.w3, height=self.h3, mass = 100, collision_group = 'env')
                objects[3] = sim.send_box(x=self.x4, y=self.y4, z=self.z4, length=self.l4, width=self.w4, height=self.h4, mass = 100, collision_group = 'env')
                [sim.send_fixed_joint(objects[i], -1) for i in [1, 2, 3]]
                [sim.send_light_source(objects[i]) for i in objects]

            self.p_box = sim.send_position_sensor(body_id = objects[0])
