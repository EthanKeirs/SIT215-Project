import gym
import numpy as np
import matplotlib.pyplot as plt

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    counter = 0
    for i in range(200):


        
        action = 0 if np.matmul(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        counter += 1
        if done:
            break
    return totalreward

def train(submit):
    env = gym.make('CartPole-v1')
    if submit:
        env.monitor.start('cartpole-hill/', force=True)

    episodes_per_update = 5
    noise_scaling = 0.1
    parameters = np.random.rand(4) * 2 - 1
    bestreward = 0
    counter = 0

    for i in range(2000):
        counter += 1
        newparams = parameters + (np.random.rand(4) * 2 - 1)*noise_scaling
        reward = run_episode(env,newparams)
        if reward > bestreward:
            bestreward = reward
            parameters = newparams
            if reward == 200:
                break

    if submit:
        for i in range(100):
            run_episode(env,parameters)
        env.monitor.close()
    return counter


hill = train(submit=False)
print(hill)
