import gym
# import gym-gridworld
from gym import envs
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


def value_iteration(env, theta=0.001, discount_factor=0.85):
    """
    Value Iteration Algorithm.

    Args:
        env: OpenAI env. env.P represents the transition probabilities of the environment.
            env.P[s][a] is a list of transition tuples (prob, next_state, reward, done).
            env.nS is a number of states in the environment.
            env.nA is a number of actions in the environment.
        theta: We stop evaluation once our value function change is less than theta for all states.
        discount_factor: Gamma discount factor.

    Returns:
        A tuple (policy, V) of the optimal policy and the optimal value function.
    """

    def one_step_lookahead(state, V):
        """
        Helper function to calculate the value for all action in a given state.

        Args:
            state: The state to consider (int)
            V: The value to use as an estimator, Vector of length env.nS

        Returns:
            A vector of length env.nA containing the expected value of each action.
        """

        A = np.zeros(env.nA)
        for act in range(env.nA):
            for prob, next_state, reward, done in env.P[state][act]:
                A[act] += prob * (discount_factor * V[next_state])
        return A

    V = np.zeros(env.nS)
    while True:
        delta = 0  # checker for improvements across states
        for state in range(env.nS):
            if state == goal_state:
                V[state] = 100
            else:
                act_values = one_step_lookahead(state, V)  # lookahead one step
                best_act_value = np.max(act_values)  # get best action value
                delta = max(delta, np.abs(best_act_value - V[state]))  # find max delta across all states
                V[state] = best_act_value  # update value to best action value
        if delta < theta:  # if max improvement less than threshold
            break
    policy = np.zeros([env.nS, env.nA])
    for state in range(env.nS):  # for all states, create deterministic policy
        act_val = one_step_lookahead(state, V)
        best_action = np.argmax(act_val)
        policy[state][best_action] = 1
    # Implement!
    return policy, V


def TDlambda(policy, env, num_eps=1000, alpha=.3, lamb=.6, gamma=.85):
    V = np.zeros(env.nS)
    e = np.zeros(env.nS)
    #prev_v = V
    Vtarg = V
    for episode in range(0, num_eps):
        #e = np.zeros(env.nS)
        #V = prev_v

        observation = env.reset()
        observation = env.observation_space.sample()
        while observation != goal_state:
            prev_state = observation
            for action in range(env.nA):
                if policy[observation][action] == 1:
                    break
            observation, reward, done, info = env.step(action)
            delta = reward + (gamma * V[observation]) - V[prev_state]
            e[prev_state] += 1

            for state in range(0, env.nS):
                '''if state == goal_state:
                    Vtarg[state] = 100
                else:'''
                Vtarg[state] = V[state] + (alpha * delta * e[state])
                e[state] = lamb * gamma * e[state]

        #prev_v = V
    Vtarg[goal_state] = 100
    return Vtarg


if __name__ == '__main__':
    env = gym.make('gym_gridworld:gridworld-v0')
    '''for episode in range(100):
        observation = env.reset()
        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break'''
    for state in range(env.nS):
        for act in range(env.nA):
            for prob, next_state, reward, done in env.P[state][act]:
                if reward > 0:
                    goal_state = next_state
                    break

    policy, V = value_iteration(env)
    print(V)

    tdV = TDlambda(policy, env)
    print(tdV)

    env.close()
