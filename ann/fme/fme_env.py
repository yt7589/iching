#
import numpy as np
import gym
from gym import spaces

class FmeEnv(gym.Env):

    def __init__(self):
        self.name = 'apps.fme.FmeEnv'
        self.current_step = 0
        self.step_left = 0

    def reset(self):
        pass

    def _reset_session(self):
        pass

    def _next_observation(self):
        pass

    def step(self, action):
        pass

    def _take_action(self, action):
        pass