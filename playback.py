from environments import ENVIRONMENTS
from individual import INDIVIDUAL
import pyrosim
import pickle

f = open ( 'playbacks/p25t15m15' , 'br')
best = pickle.load(f)
f.close()

# sim = pyrosim.Simulator(eval_time=1000, play_blind=False, play_paused=True)
envs = ENVIRONMENTS()
for env in envs.envs:
    best.Start_Evaluation(envs.envs[env], play_blind=False)
    best.sim.wait_to_finish()
print(best.fitness)