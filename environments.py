import constants as C
from environment import ENVIRONMENT

class ENVIRONMENTS:
    def __init__(self):
        self.envs = {i:ENVIRONMENT(i) for i in range(C.numEnvs)}