import constants as C
class ENVIRONMENT:
    def __init__(self, id) -> None:
        pos = ['front', 'right', 'back', 'left']
        self.ID = id
        self.l, self.w, self.h = [C.L] * 3
        getattr(self, f'place_light_source_to_the_{pos[id]}')()

    def place_light_source_to_the_front(self):
        self.x, self.y, self.z = 0, 30 * C.L, 0

    def place_light_source_to_the_right(self):
        self.x, self.y, self.z = 30 * C.L, 0, 0

    def place_light_source_to_the_back(self):
        self.x, self.y, self.z = 0, -30 * C.L, 0

    def place_light_source_to_the_left(self):
        self.x, self.y, self.z = -30 * C.L, 0, 0

    def send_to(self, sim):
        self.light_source = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h)
        sim.send_light_source( body_id = self.light_source )