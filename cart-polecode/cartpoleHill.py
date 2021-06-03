import gym
import numpy as np

env = gym.make('CartPole-v1')

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for i in range(200):
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        env.render()
        if done:
            break
    


bestparams = None
bestreward = 0
noise_scaling = 0.1
parameters = np.random.rand(4) * 2 - 1
bestreward = 0
for i in range(10000):
    newparams = parameters + (np.random.rand(4) * 2 - 1)*noise_scaling
    reward = 0
    run = run_episode(env,newparams)
    if reward > bestreward:
        bestreward = reward
        parameters = newparams
        if reward == 200:
            break

