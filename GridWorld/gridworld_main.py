import gym
# import gym-gridworld
from gym import envs
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


def lookahead(env, state, V, gamma):
    A = np.zeros(env.nA)
    for act in range(env.nA):
        for prob, next_state, reward, done in env.P[state][act]:
            A[act] += prob * (gamma * V[next_state])
    return A


def value_iteration(env, theta=0.001, gamma=0.85):
    V = np.zeros(env.nS)
    while True:
        delta = 0 #change in val for states
        for state in range(env.nS):
            if state == goal_state:
                V[state] = 100
            else:
                act_values = lookahead(env, state, V, gamma)
                best_act_value = np.max(act_values)  # get best action value
                delta = max(delta, np.abs(best_act_value - V[state]))  # find max delta across states
                V[state] = best_act_value  # update value to best action value
        if delta < theta:  # if max improvement less than threshold
            break
    policy = np.zeros([env.nS, env.nA])
    for state in range(env.nS):  # create  policy
        act_val = lookahead(env, state, V, gamma)
        best_action = np.argmax(act_val)
        policy[state][best_action] = 1

    return policy, V


def TDlambda(policy, env, num_eps=100, alpha=.3, lamb=.6, gamma=.85):
    V = np.zeros(env.nS)
    e = np.zeros(env.nS)
    Vtarg = V
    step_its = list()
    steps = 0
    observation = env.reset()
    start = observation
    for episode in range(0, num_eps):

        observation = env.reset()
        steps = 0
        observation = env.observation_space.sample()
        #observation = start

        while observation != goal_state:
            prev_state = observation
            act_vals = lookahead(env, observation, Vtarg, gamma)
            act_max = np.max(act_vals)
            max_val_count = 0
            for action in range(env.nA):
                if act_max == act_vals[action]:
                    max_val_count += 1
                    take_action = action
                if max_val_count > 1:
                    take_action = env.action_space.sample()
                    break

            '''for action in range(env.nA):
                if policy[observation][action] == 1:
                    break'''
            observation, reward, done, info = env.step(take_action)
            steps += 1
            delta = reward + (gamma * Vtarg[observation]) - Vtarg[prev_state]
            e[prev_state] += 1

            for state in range(0, env.nS):
                '''if state == goal_state:
                    Vtarg[state] = 100
                else:'''
                Vtarg[state] = Vtarg[state] + (alpha * delta * e[state])
                e[state] = lamb * gamma * e[state]
            if done:
                break
        step_its.append(steps)

    #Vtarg[goal_state] = 100
    return Vtarg, step_its


if __name__ == '__main__':
    env = gym.make('gym_gridworld:gridworld-v0')

    for state in range(env.nS):
        for act in range(env.nA):
            for prob, next_state, reward, done in env.P[state][act]:
                if reward > 0:
                    goal_state = next_state
                    break

    policy, V = value_iteration(env)
    print(V)

    tdV, steps = TDlambda(policy, env)
    print(tdV)

    plt.plot(steps)
    plt.show()

    env.close()
