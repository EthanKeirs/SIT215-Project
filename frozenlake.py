import gym

env = gym.make('FrozenLake-v0')

state = env.reset()
finish = False
while not finish:
    env.render()
    action = env.action_space.sample()
    nextState, reward, finish, info = env.step(action)
    state = nextState
