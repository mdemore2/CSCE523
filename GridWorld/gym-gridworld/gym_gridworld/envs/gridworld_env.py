import math
import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.toy_text import discrete
from _collections import defaultdict


class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GridWorldEnv(discrete.DiscreteEnv):
    metadata = {'render.modes': ['human']}

    ACTION_UP = 0
    ACTION_DOWN = 1
    ACTION_LEFT = 2
    ACTION_RIGHT = 3

    def __init__(self):

        self.location = Position
        self.goal = Position

        self.mapfile = input('Enter map file name:\n')

        self.startpos = input('Enter agent start position (x y) or r to randomly assign start position:\n')

        self.nA = 4
        self.x_dim = 3
        self.y_dim = 3
        self.goal.x = 0
        self.goal.y = 0
        self.obstructed = []
        self.map_file = open(self.mapfile, 'r')
        self.map = self.read_in()

        # map is accessible [y][x]

        if self.startpos == 'r':
            self.location.x = np.random.randint(0, self.x_dim)
            self.location.y = np.random.randint(0, self.y_dim)
            while self.map[self.location.y][self.location.x] != "V":
                self.location.x = np.random.randint(0, self.x_dim)
                self.location.y = np.random.randint(0, self.y_dim)
        else:
            read_x, read_y = self.startpos.split()
            self.location.x = int(read_x)
            self.location.y = int(read_y)

        initial_states = np.zeros(self.nS)
        start_state = (self.location.y * self.x_dim) + self.location.x
        initial_states[start_state] = 1
        self.isd = initial_states

        self.P = self.gen_transitions()

        super(GridWorldEnv, self).__init__(self.nS, self.nA, self.P, self.isd)

    def read_in(self):
        dimensions = self.map_file.readline()  # read first line of mapfile
        dimensions_split = dimensions.split()  # break x and y vals for gridworld
        self.x_dim = int(dimensions_split[0])
        self.y_dim = int(dimensions_split[1])
        dict_x = defaultdict(dict)
        dict_y = defaultdict(list)
        for row in range(0, self.x_dim):  # read in each row
            new_row = self.map_file.readline()
            new_row_split = new_row.split()
            for col in range(0, self.y_dim):
                dict_x[col] = new_row[col]
                if new_row_split[col] == "O":
                    self.obstructed.append((col, row))
                elif new_row_split[col] == "G":
                    self.goal.x = col
                    self.goal.y = row
                    self.goal.state = (self.x_dim * row) + col
            dict_y[row] = dict_x
        self.nS = self.x_dim * self.y_dim
        return dict_y

    def gen_transitions(self):
        """
        :rtype: object
        """

        p = {s: {a: [] for a in range(self.nA)} for s in range(self.nS)}
        for state in range(0, self.nS):
            for action in range(0, 4):

                next_state7 = state

                # make moves and check if move valid
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
                    if (state % self.x_dim) == 0:
                        next_state3 = state
                else:  # action == GridWorldEnv.ACTION_LEFT
                    next_state90 = state - 1
                    next_state3 = state + 1
                    if (state % self.x_dim) == 0:
                        next_state90 = state
                    if (next_state3 % self.x_dim) == 0:
                        next_state3 = state

                # check if move is obstructed
                for obstacle in self.obstructed:
                    obstacle_state = (self.x_dim * obstacle[1]) + obstacle[0]
                    if state == obstacle_state:
                        next_state3 = state
                        next_state7 = state
                        next_state90 = state
                    if next_state3 == obstacle_state:
                        next_state3 = state
                    if next_state7 == obstacle_state:
                        next_state7 = state
                    if next_state90 == obstacle_state:
                        next_state90 = state

                if state == self.goal.state:
                    next_state90 = state
                    next_state7 = state
                    next_state3 = state

                # check for goal, build transition table
                if next_state90 == self.goal.state:
                    next_state90_list = (0.9, next_state90, 100, 1)
                else:
                    next_state90_list = (0.9, next_state90, -1, 0)
                if next_state7 == self.goal.state:
                    next_state7_list = (0.07, next_state7, 100, 1)
                else:
                    next_state7_list = (0.07, next_state7, -1, 0)
                if next_state3 == self.goal.state:
                    next_state3_list = (0.03, next_state3, 100, 1)
                else:
                    next_state3_list = (0.03, next_state3, -1, 0)

                p[state][action] = [next_state90_list, next_state7_list, next_state3_list]

        return p

    def render(self, mode='human'):
        print()

    # shouldn't need template below, implemented in super class

    '''def step(self, action):
        super

    def reset(self):
        ...

    def close(self):
        ...
    '''
