"""Exploring state and action spaces
The Cliff Walking environment involves an agent crossing a grid world from start to goal while avoiding falling off a cliff. If the player moves to a cliff location it returns to the start location. The player makes moves until they reach the goal, which ends the episode. Your task is to explore the state and action spaces of this environment.

Image showing an animation for the cliff walking environment.

Instructions
Create an environment instance for Cliff Walking with with the environment ID CliffWalking.
Compute the size of the action space and store it in num_actions.
Compute the size of the state space and store it in num_states.
"""

# Create the Cliff Walking environment
env = gym.make("CliffWalking")

# Compute the size of the action space
num_actions = env.action_space.n

# Compute the size of the state space
num_states = env.observation_space.n

print("Number of actions:", num_actions)
print("Number of states:", num_states)


"""Transition probabilities and rewards
The Cliff Walking environment has 48 states, numbered from 0 to 47, line by line, from the upper left corner (0) to the lower right corner (47). Your goal is to investigate the structure of transition probabilities and rewards within this setup. Notably, all rewards, including the reward for reaching the goal, are negative in this environment. This design choice emphasizes minimizing the number of steps taken, as each step incurs a penalty, making efficiency a key aspect for designing effective learning algorithms.

The gymnasium library has been imported as gym and the environment as env. Also num_states and num_actions from the previous exercise have been imported.

Image showing the cliff walking environment.

Instructions
Choose the state located above the goal state.
For each action, extract the list of transition tuples for the chosen state and store it in transitions.
For each transition, extract the probability, next_state, reward, and done flag.
"""

# Choose the state
state = 35

# Extract transitions for each state-action pair
for action in range(num_actions):
    transitions = env.unwrapped.P[state][action]
    # Print details of each transition
    for transition in transitions:
        probability, next_state, reward, done = transition
        print(f"Probability: {probability}, Next State: {next_state}, Reward: {reward}, Done: {done}")



"""Defining a deterministic policy
In this exercise, you'll be working with a custom environment called MyGridWorld, the same one you've seen in the video. This environment is a grid world where the agent's goal is to reach the diamond as quickly as possible. Your task is to define a policy that guides the agent's behavior as specified in the figure below.

Image showing the policy:  states 0, 1, 6, 7 - action right.  states 2, 3 - action down.  states 4, 5 - action left.

Actions are represented as: (0 → left, 1 → down, 2 → right, 3 → up).

The gymnasium library has been imported for you as gym along with the render() function.

Instructions 1/2
Create an instance env for the environment using MyGridWorld as an environment ID and 'rgb_array' as render_mode.
Define the policy as shown in the figure as a Python dictionary.
Instructions 2/2
In the interaction loop, choose the agent's actions based on the policy.
Render the environment after every iteration.
"""

# Create the environment
env = gym.make("MyGridWorld", render_mode="rgb_array")
state, info = env.reset()

# Define the policy
policy = {
    0:2, 1:2, 2:1,
    3:1, 4:0, 5:0,
    6:2, 7:2
}



# Create the environment
env = gym.make('MyGridWorld', render_mode='rgb_array')
state, info = env.reset()

# Define the policy
policy = {0:2, 1:2, 2:1, 3:1, 4:0, 5:0, 6:2, 7:2}

terminated = False
while not terminated:
  # Select action based on policy 
  action = policy[state]
  state, reward, terminated, truncated, info = env.step(action)
  # Render the environment
  render()



"""Computing state-values for a policy
Using the same deterministic environment MyGridWorld, now you need to evaluate the effectiveness of the policy you defined in the previous exercise. You'll do this by computing the state value function for each state under this policy.

The environment has been imported as env along with the necessary variables needed (terminal_state, num_states, policy, gamma).

Instructions
Complete the function compute_state_value() to compute the value for each state under the given policy.
Create a state_values dictionary where each key is the state, and each value is the state value.
"""

# Complete the function
def compute_state_value(state):
    if state == terminal_state:
        return 0
    action = policy[state]
    _, next_state, reward, _ = env.unwrapped.P[state][action][0]
    return reward + gamma * compute_state_value(next_state)

# Compute all state values 
state_values = {state: compute_state_value(state) for state in range(env.observation_space.n)}

print(state_values)



"""Comparing policies
You are given two state value functions (value_function_1 and value_function_2) corresponding to two different policies in the MyGridWorld environment. Your task is to compare these state value functions on a state-by-state basis to determine which policy is more effective.

The variable num_states is available for you to use.

Instructions
Create a list one_is_better of boolean values, where each element checks if the state's value in value_function_1 is higher or equal than the state's value in value_function_2.
Create a list two_is_better of boolean values, where each element checks if the state's value in value_function_2 is higher or equal than the state's value in value_function_1.
"""

value_function_1 = {0: 1, 1: 2, 2: 3, 3: 7, 4: 6, 5: 4, 6: 8, 7: 10, 8: 0}
value_function_2 = {0: 7, 1: 8, 2: 9, 3: 7, 4: 9, 5: 10, 6: 8, 7: 10, 8: 0}

# Check for each value in policy 1 if it is better than policy 2
one_is_better = [value_function_1[state] >= value_function_2[state] for state in range(num_states)]

# Check for each value in policy 2 if it is better than policy 1
two_is_better = [value_function_2[state] >= value_function_1[state] for state in range(num_states)]

if all(one_is_better):
  print("Policy 1 is better.")
elif all(two_is_better):
  print("Policy 2 is better.")
else:
  print("Neither policy is uniformly better across all states.")



"""Computing Q-values
Your goal is to compute the action-values, also known as Q-values, for each state-action pair in the custom MyGridWorld environment when following the below policy. In RL, Q-values are essential because they represent the expected utility of executing a specific action in a given state, followed by adherence to the policy.

exercise_policy.png

The environment has been imported as env along with the compute_state_value() function and the necessary variables needed (terminal_state, num_states, num_actions, policy, gamma).

Instructions
Complete the compute_q_value() function to compute the action-value for a given state and action.
Create a dictionary Q where each key represents a state-action pair, and the corresponding value is the Q-value for that pair.
"""

# Complete the function to compute the action-value for a state-action pair
def compute_q_value(state, action):
    if state == terminal_state:
        return None   
    probability, next_state, reward, done = env.unwrapped.P[state][action][0]
    return reward + gamma * compute_state_value(next_state)

# Compute Q-values for each state-action pair
Q = {(state, action): compute_q_value(state, action) for state in range(num_states) for action in range(num_actions)}

print(Q)



"""Improving a policy
In the previous exercise, you computed the Q-values for each state-action pair in the MyGridWorld environment. Now, you'll use these Q-values to improve the existing policy. Policy improvement is a critical step in reinforcement learning, where you enhance the policy by choosing actions that maximize the expected utility (Q-value) in each state. After improving the policy, you will render the new movements according to this improved policy.

The environment has been imported as env, along with the Q-values as Q, and the render() function.

Instructions
Find the best action for each state based on Q-values.
Select the right action based on the improved_policy.
Execute the selected action to observe its outcome.
"""

improved_policy = {}

for state in range(num_states-1):
    # Find the best action for each state based on Q-values
    max_action = max(range(num_actions), key=lambda action: Q[(state, action)])
    improved_policy[state] = max_action

terminated = False
while not terminated:
  # Select action based on policy 
  action = improved_policy[state]
  # Execute the action
  state, reward, terminated, truncated, info = env.step(action)
  render()



"""Applying policy iteration for optimal policy
Policy iteration is a fundamental technique in RL for finding an optimal policy. It involves two main steps: policy evaluation, where you calculate the state-value function for a given policy, and policy improvement, where you update the policy based on these values. You'll apply these steps iteratively to converge to the optimal policy in the custom MyGridWorld environment.

The render_policy() function will be used to show the steps taken by an agent according to a policy.

The compute_state_value(state, policy) and compute_q_value(state, action, policy) have been preloaded for you.

Instructions 1/3
Complete the policy_evaluation() function to compute the state-value function V for a given policy.
Instructions 2/3
In the policy_improvement() function, compute Q, containing all state-action values.
Compute the improved_policy based on Q.
Instructions 3/3
Complete the policy_iteration() function using the functions previously built to improve the policy shown below.
"""

# Complete the policy evaluation function
def policy_evaluation(policy):
    V = {state: compute_state_value(state, policy) for state in range(env.observation_space.n)}
    return V



def policy_improvement(policy):
    improved_policy = {s: 0 for s in range(num_states-1)}
    
	# Compute the Q-value for each state-action pair
    Q = {(state, action): compute_q_value(state, action, policy) for state in range(num_states) for action in range(num_actions)}
            
    # Compute the new policy based on the Q-values
    for state in range(num_states-1):
        max_action = max(range(num_actions), key=lambda action: Q[(state, action)])
        improved_policy[state] = max_action
        
    return improved_policy



# Complete the policy iteration function
def policy_iteration():
    policy = {0:2, 1:2, 2:1, 3:1, 4:0, 5:0, 6:2, 7:2}
    while True:
        V = policy_evaluation(policy)
        improved_policy = policy_improvement(policy)
        if improved_policy == policy:
            break
        policy = improved_policy
    
    return policy, V

policy, V = policy_iteration()
render_policy(policy)



"""Implementing value iteration
Value iteration is a key method in RL for finding the optimal policy. It iteratively improves the value function for each state until it converges, resulting in the discovery of the optimal policy. You'll start with an initialized value function V and policy, both preloaded for you. Then, you'll update them in a loop until the value function converges and see the policy in action.

The get_max_action_and_value(state, V) function has been pre-loaded for you.

Instructions
For each state, find the action with the maximum Q-value (max_action) and its corresponding value (max_q_value).
Update the new_V dictionary and the policy based on max_action and max_q_value.
Check for convergence by checking if the difference between new_v and V for every state is less than threshold.
"""

threshold = 0.001
while True:
  new_V = {state: 0 for state in range(num_states)}
  for state in range(num_states-1):
    # Get action with maximum Q-value and its value 
    max_action, max_q_value = get_max_action_and_value(state, V)
    # Update the value function and policy
    new_V[state] = max_q_value
    policy[state] = max_action
  # Test if change in state values is negligeable
  if all(abs(new_V[state] - V[state]) < threshold for state in V):
    break
  V = new_V
render_policy(policy)