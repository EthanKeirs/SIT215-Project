import gym
import numpy as np

env = gym.make('CartPole-v1')

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for i in range(200):
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

        
bestparams = None
bestreward = 0
for i in range(10000):
    parameters = np.random.rand(4) * 2 - 1
    reward = run_episode(env,parameters)
    if reward > bestreward:
        bestreward = reward
        bestparams = parameters
        if reward == 200:
            break
