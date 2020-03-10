import gym
#import gym-gridworld
from gym import envs

if __name__ == '__main__':
    env = gym.make('gym_gridworld:gridworld-v0')
    for episode in range(100):
        observation = env.reset()
        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break
    env.close()