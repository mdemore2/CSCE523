import math
import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.toy_text import discrete


class GridWorldEnv(discrete.DiscreteEnv):
    metadata = {'render.modes': ['human']}
    # ACTION = ["N", "S", "E", "W"]
    ACTION_UP = 0
    ACTION_DOWN = 1
    ACTION_LEFT = 2
    ACTION_RIGHT = 3

    def __init__(self, mapfile, startpos):

        self.location = None
        self.goal = None
        self.nA = 4
        self.x_dim = 3
        self.y_dim = 3
        self.goal.x = 0
        self.goal.y = 0
        self.obstructed = []
        self.map_file = open(mapfile, 'r')
        self.map = self.read_in()
        # map is accessible [y][x]
        if startpos:
            self.location.x = startpos[0]
            self.location.y = startpos[1]
        else:
            self.location.x = np.random.randint(0, self.x_dim)
            self.location.y = np.random.randint(0, self.y_dim)
            while self.map[self.location.x][self.location.y] != "V":
                self.location.x = np.random.randint(0, self.x_dim)
                self.location.y = np.random.randint(0, self.y_dim)

        initial_states = np.zeroes(self.nS)
        start_state = (self.location.y * self.x_dim) + self.location.x
        initial_states[start_state] = 1
        self.isd = initial_states

        self.P = self.gen_transitions(self)

        super().__init__(self.nS, self.nA, self.P, self.isd)

    def read_in(self):
        dimensions = self.map_file.readline()  # read first line of mapfile
        dimensions = dimensions.split()  # break x and y vals for gridworld
        self.x_dim = int(dimensions[0])
        self.y_dim = int(dimensions[1])
        dict_x, dict_y = None
        for row in range(0, self.x_dim - 1):  # read in each row
            new_row = self.map_file.readline()
            new_row = new_row.split()
            for col in range(0, self.y_dim - 1):
                dict_x[col] = new_row[col]
                if new_row[col] == "O":
                    self.obstructed.append((col, row))
                elif new_row[col] == "G":
                    self.goal.x = col
                    self.goal.y = row
                    self.goal.state = (self.x_dim * row) + col
            dict_y[row] = dict_x
        self.nS = self.x_dim * self.y_dim
        return dict_y

    # need to determine how to treat blocked squares
    def gen_transitions(self):
        """
        :rtype: object
        """
        p = None
        for state in range(0, self.nS - 1):
            for action in range(0, 3):
                next_state7 = state
                if action == GridWorldEnv.ACTION_UP:
                    next_state90 = state - self.x_dim
                    next_state3 = state + self.x_dim
                    if (next_state90 > self.nS - 1) or next_state90 < 0:
                        next_state90 = state
                    if (next_state3 > self.nS - 1) or next_state3 < 0:
                        next_state3 = state
                elif action == GridWorldEnv.ACTION_DOWN:
                    next_state90 = state + self.x_dim
                    next_state3 = state - self.x_dim
                    if (next_state90 > self.nS - 1) or next_state90 < 0:
                        next_state90 = state
                    if (next_state3 > self.nS - 1) or next_state3 < 0:
                        next_state3 = state
                elif action == GridWorldEnv.ACTION_RIGHT:
                    next_state90 = state + 1
                    next_state3 = state - 1
                    if (next_state90 % self.x_dim) == 0:
                        next_state90 = state
                    if (next_state3 % self.x_dim) == 0:
                        next_state3 = state
                else:  # action == GridWorldEnv.ACTION_LEFT
                    next_state90 = state - 1
                    next_state3 = state + 1
                    if (next_state90 % self.x_dim) == 0:
                        next_state90 = state
                    if (next_state3 % self.x_dim) == 0:
                        next_state3 = state
                if next_state90 == self.goal.state:
                    p[state][action] = [(0.9, next_state90, 100, 1), (0.07, next_state7, 0, 0), (0.03, next_state3, 0, 0)]
                elif next_state7 == self.goal.state:
                    p[state][action] = [(0.9, next_state90, 0, 0), (0.07, next_state7, 100, 1), (0.03, next_state3, 0, 0)]
                elif next_state3 == self.goal.state:
                    p[state][action] = [(0.9, next_state90, 0, 0), (0.07, next_state7, 0, 0), (0.03, next_state3, 100, 1)]
                else:
                    p[state][action] = [(0.9, next_state90, 0, 0), (0.07, next_state7, 0, 0), (0.03, next_state3, 0, 0)]
        return p

    # shouldn't need template below, implemented in super class
    '''def step(self, action):
        ...

    def reset(self):
        ...

    def render(self, mode='human'):
        ...

    def close(self):
        ...
    '''
