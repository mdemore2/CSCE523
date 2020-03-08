import math
import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.toy_text import discrete


class GridWorldEnv(discrete.DiscreteEnv):
    metadata = {'render.modes': ['human']}
    ACTION = ["N", "S", "E", "W"]

    def __init__(self, mapfile, startpos):
        self.nA = 4
        self.xdim = 3
        self.ydim = 3
        self.mapfile = open(mapfile, 'r')
        self.map = self.readin(self)

        if startpos:
            self.location.x = startpos[0]
            self.location.y = startpos[1]
        else:
            self.location.x = np.random.randint(0, self.xdim)
            self.location.y = np.random.randint(0, self.ydim)
            while self.map[self.location.x][self.location.y] != "V":
                self.location.x = np.random.randint(0, self.xdim)
                self.location.y = np.random.randint(0, self.ydim)

        initial_states = np.zeroes(self.nS)
        startstate = int(str(self.location.x) + str(self.location.y))
        initial_states[startstate] = 1
        self.isd = initial_states

        self.P = self.genTransitions(self)

    def readin(self):
        dimensions = self.mapfile.readline()  # read first line of mapfile
        dimensions = dimensions.split()  # break x and y vals for gridworld
        self.xdim = int(dimensions[0])
        self.ydim = int(dimensions[1])
        dictx, dicty = {}
        for row in range(0, self.xdim - 1):  # read in each row
            newrow = self.mapfile.readline()
            newrow = newrow.split()
            for col in range(0, self.ydim - 1):
                dicty[col] = newrow[col]
            dictx[row] = dicty
        self.nS = self.xdim * self.ydim
        return dictx

#need to determine how to treat blocked squares

    def genTransitions(self):

    #shouldn't need template below, implemented in super class
    '''def step(self, action):
        ...

    def reset(self):
        ...

    def render(self, mode='human'):
        ...

    def close(self):
        ...
    '''