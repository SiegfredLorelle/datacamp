"""Calculating discounted returns for agent strategies
Discounted returns help in evaluating the total amount of rewards an agent can expect to accumulate over time, taking into account that future rewards are less valuable than immediate rewards. You are given the expected rewards for two different strategies (exp_rewards_strategy_1 and exp_rewards_strategy_2) of an RL agent. Your task is to calculate the discounted return for each strategy and determine which one yields the higher return.

The numpy library has been imported for you as np.

Instructions 1/2
Compute the array of discounts discounts_strategy_1 for the first strategy.
Compute the discounted_return_strategy_1.

Instructions 2/2
Compute the array of discounts discounts_strategy_2 for the second strategy.
Compute the discounted_return_strategy_2.
"""

exp_rewards_strategy_1 = np.array([3, 2, -1, 5])

discount_factor = 0.9

# Compute discounts
discounts_strategy_1 = np.array([0.9 ** i for i in range(len(exp_rewards_strategy_1))])

# Compute the discounted return
discounted_return_strategy_1 = np.sum(discounts_strategy_1 * exp_rewards_strategy_1)

print(f"The discounted return of the first strategy is {discounted_return_strategy_1}")




exp_rewards_strategy_2 = np.array([6, -5, -3, -2])

discount_factor = 0.9

# Compute discounts
discounts_strategy_2 = np.array([discount_factor ** i for i in range(len(exp_rewards_strategy_2))])

# Compute the discounted return
discounted_return_strategy_2 = np.sum(discounts_strategy_2 * exp_rewards_strategy_2)

print(f"The discounted return of the second strategy is {discounted_return_strategy_2}")



"""Setting up a Mountain Car environment
One of the most common Gym environments is Mountain Car, where the goal is to drive an underpowered car up a steep hill. The car's engine isn't strong enough to climb the hill in a single pass, so the car needs to build up momentum by driving back and forth. Your task is to create and set up this environment.



Instructions
Import the gymnasium library as gym.
Create a Mountain Car environment using the Gym library setting the environment ID as MountainCar and the render_mode as 'rgb_array'.
Reset the environment using a seed of 42 and get the initial_state which contains two values: the position and velocity of the car.
"""

# Import the gymnasium library
import gymnasium as gym

# Create the environment
env = gym.make("MountainCar", render_mode="rgb_array")

# Get the initial state
initial_state, info = env.reset(seed=42)

position = initial_state[0]
velocity = initial_state[1]

print(f"The position of the car along the x-axis is {position} (m)")
print(f"The velocity of the car is {velocity} (m/s)")




"""Visualizing the Mountain Car Environment
Now, you'll take a step further in your exploration of the Mountain Car environment. Visualization is a key aspect of understanding the dynamics of RL environments. You'll write a function render() that displays the current state of the environment. This function will be used later on for any environment you want to visualize.

matplotlib.pyplot and gymnasium have been imported as plt and gym.

Instructions
Complete the render() function to visualize the environment, obtaining the environment state_image and plotting it.
Call the render() function to display the current state of the environment.
"""

env = gym.make('MountainCar', render_mode='rgb_array')
initial_state, _ = env.reset()

# Complete the render function
def render():
    state_image = env.render()
    plt.imshow(state_image)
    plt.show()

# Call the render function
render()


"""Interacting with the Frozen Lake environment
Now you'll navigate the Frozen Lake environment, a grid-based world where actions move an agent in specific directions. Your task is to carefully look at the environment, and manually define a list of actions that will navigate the agent from the start (top left) to the goal (bottom right) without falling into any holes. In the Frozen Lake environment, actions are typically represented as:

0: left
1: down
2: right
3: up
After running your code, be sure to navigate through your plots to see the path taken by using the 'Previous Plot' and 'Next Plot' buttons. This will help you understand the sequence of actions and their outcomes.

gym and plt have been imported along with the render() function and the env variable.

Instructions
Observe the agent's position on the right and define a list of actions to navigate the agent across the lake to the goal.
Execute each action in the list through the for loop.
Render the environment after each action to observe the agent's path.
"""

# Define the sequence of actions
actions = [2, 2, 1, 1, 1, 2]

for action in actions:
  # Execute each action
  state, reward, terminated, _, _ = env.step(action)
  # Render the environment
  render()
  if terminated:
  	print("You reached the goal!")