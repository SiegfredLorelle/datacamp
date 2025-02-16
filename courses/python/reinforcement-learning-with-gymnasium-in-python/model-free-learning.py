"""Episode generation for Monte Carlo methods
Monte Carlo methods require episodes to be generated in order to derive the value function. Therefore, you'll now implement a function that generates episodes by selecting actions randomly until an episode terminates. In later exercises, you will call this function to apply Monte Carlo methods on the custom environment env pre-loaded for you.

The render() function is pre-loaded for you.

Instructions
Reset the environment using a seed of 42.
In the episode loop, select a random action at each iteration.
Once an iteration ends, update the episode data by adding the tuple (state, action, reward).
"""

def generate_episode():
    episode = []
    # Reset the environment
    state, info = env.reset(seed=42)
    terminated = False
    while not terminated:
      # Select a random action
      action = env.action_space.sample()
      next_state, reward, terminated, truncated, info = env.step(action)
      render()
      # Update episode data
      episode.append((state, action, reward))
      state = next_state
    return episode
print(generate_episode())



"""Implementing first-visit Monte Carlo
The goal of Monte Carlo algorithms is to estimate the Q-table in order to derive an optimal policy. In this exercise, you will implement the First-Visit Monte Carlo method to estimate the action-value function Q, and then compute the optimal policy to solve the custom environment you've seen in the previous exercise. Whenever computing the return, assume a discount factor of 1.

The numpy arrays Q, returns_sum, and returns_count, storing the Q-values, the cumulative sum of rewards, and the count of visits for each state-action pair, respectively, have been initialized and pre-loaded for you.

Instructions
Define the if condition that should be tested in the first-visit Monte Carlo algorithm.
Update the returns (returns_sum), their counts (returns_count) and the visited_states.
"""

for i in range(100):
  episode = generate_episode()
  visited_states = set()
  for j, (state, action, reward) in enumerate(episode):
    # Define the first-visit condition
    if (state, action) not in visited_states:
      # Update the returns, their counts and the visited states
      returns_sum[state, action] += sum([x[2] for x in episode[j:]])
      returns_count[state, action] += 1
      visited_states.add((state, action))

nonzero_counts = returns_count != 0

Q[nonzero_counts] = returns_sum[nonzero_counts] / returns_count[nonzero_counts]
render_policy(get_policy())




"""Implementing every-visit Monte Carlo
The Every-Visit Monte Carlo method differs from the First-Visit variant by updating values every time a state-action pair appears, rather than only on first encounters. While this approach provides a comprehensive evaluation of the policy by utilizing all the available information from the episodes, it may also introduce more variance in the value estimates because it includes all samples, regardless of when they occur in the episode. Your task is to complete the implementation of the every_visit_mc() function, which estimates the action-value function Q over num_episodes episodes.

The dictionaries returns_sum, and returns_count, with state-action pairs as keys have been initialized and pre-loaded for you along with the generate_episode() function.

Instructions
Generate an episode using the generate_episode() function.
Update the returns and their counts for each state-action pair within an episode.
Compute the estimated Q-values.
"""

Q = np.zeros((num_states, num_actions))
for i in range(100):
  # Generate an episode
  episode = generate_episode()
  # Update the returns and their counts
  for j, (state, action, reward) in enumerate(episode):
    returns_sum[(state,  action)] += sum(x[2] for x in episode[j:])
    returns_count[(state,  action)] += 1

# Update the Q-values for visited state-action pairs 
nonzero_counts = returns_count != 0
Q[nonzero_counts] = returns_sum[nonzero_counts] / returns_count[nonzero_counts]
    
render_policy(get_policy())




"""Implementing the SARSA update rule
SARSA is an on-policy algorithm in RL that updates the action-value function based on the action taken and the action selected in the next state. This method helps to learn the value of not just the current state-action pair but also the subsequent one, providing a way to learn policies that consider future actions. The SARSA update rule is below, and your task is to implement a function that updates a Q-table based on this rule.

The NumPy library has been imported to you as np.

Image showing the mathematical formula of the SARSA update rule.

Instructions
Retrieve the current Q-value for the given state-action pair.
Find the Q-value for the next state-action pair.
Update the Q-value for the current state-action pair using the SARSA formula.
Update the Q-table Q, given that an agent takes action 0 in state 0, receives a reward of 5, moves to state 1, and performs action 1.
"""

def update_q_table(state, action, reward, next_state, next_action):
  	# Get the old value of the current state-action pair
    old_value = Q[(state, action)]
    # Get the value of the next state-action pair
    next_value = Q[(next_state, next_action)]
    # Compute the new value of the current state-action pair
    Q[(state, action)] = (1 - alpha) * old_value + alpha * (reward + gamma * next_value)

alpha = 0.1
gamma  = 0.8
Q = np.array([[10,0],[0,20]], dtype='float32')
# Update the Q-table for the ('state1', 'action1') pair
update_q_table(0, 0, 5, 1, 1)
print(Q)



"""Solving 8x8 Frozen Lake with SARSA
In this exercise, you will apply the SARSA algorithm, incorporating the update_q_table() function you previously implemented, to learn an optimal policy for the 8x8 Frozen Lake environment. This environment is identical to the classic 4x4 one, with the only difference of being bigger. You will use the SARSA algorithm to iteratively improve the agent's policy based on the rewards received from the environment.

A Q-table Q has been initialized and pre-loaded for you, along with the update_q_table() function from the previous exercise.

Instructions
For each episode in the training process execute the selected action.
Choose the next_action randomly.
Update the Q-table for the given state and action.
"""

for episode in range(num_episodes):
    state, info = env.reset()
    action = env.action_space.sample()
    terminated = False
    while not terminated:
      	# Execute the action
        next_state, reward, terminated, truncated, info = env.step(action)
        # Choose the next action randomly
        next_action = env.action_space.sample()
        # Update the Q-table
        update_q_table(state, action, reward, next_state, next_action)
        state, action = next_state, next_action   
render_policy(get_policy())




"""Implementing Q-learning update rule
Q-learning is an off-policy algorithm in reinforcement learning (RL) that seeks to find the best action to take given the current state. Unlike SARSA, which considers the actual next action taken, Q-learning updates its Q-values using the maximum future reward irrespective of the action taken. This distinction allows Q-learning to learn the optimal policy while following an exploratory or even a random policy. Here's the task to implement a function that updates a Q-table based on the Q-learning rule. The Q-learning update rule is below, and your task is to implement a function that updates a Q-table based on this rule.

The NumPy library has been imported to you as np.

Image showing the mathematical formula of the Q-learning update rule.

Instructions
Retrieve the current Q-value for the given state-action pair.
Determine the maximum Q-value for the next state across all possible actions in actions.
Update the Q-value for the current state-action pair using the Q-learning formula.
Update the Q-table Q, given that an agent takes action 0 in state 0, receives a reward of 5, and moves to state 1.
"""

actions = ['action1', 'action2'] 
def update_q_table(state, action, reward, next_state):
    # Get the old value of the current state-action pair
    old_value = Q[(state, action)]
    # Determine the maximum Q-value for the next state
    next_max = max(Q[next_state])
    # Compute the new value of the current state-action pair
    Q[state, action] = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)

alpha = 0.1
gamma = 0.95
Q = np.array([[10, 8], [20, 15]], dtype='float32')
# Update the Q-table
update_q_table(0, 0, 5, 1)
print(Q)



"""Solving 8x8 Frozen Lake with Q-learning
In this exercise, you'll apply the Q-learning algorithm to learn an optimal policy for navigating through the 8x8 Frozen Lake environment, this time with the "slippery" condition enabled. The challenge introduces stochastic transitions, making the agent's movement unpredictable and thus more closely simulating real-world scenarios.

A Q-table Q has been initialized and pre-loaded for you, along with the update_q_table() function from the previous exercise and an empty list rewards_per_episode that will contain the total reward accumulated through each episode.

Instructions
For each episode, execute the selected action and observe the reward and next state.
Update the Q-table.
Append the total_reward to the rewards_per_episode list.
"""

for episode in range(10000):
    state, info = env.reset()
    total_reward = 0
    terminated = False
    while not terminated:
        action = env.action_space.sample()
        # Execute the action
        next_state, reward, terminated, truncated, info = env.step(action)
        # Update the Q-table
        update_q_table(state, action, reward, next_state)
        state = next_state
        total_reward += reward
    # Append the total reward to the rewards list    
    rewards_per_episode.append(total_reward)
print("Average reward per random episode: ", np.mean(rewards_per_episode))




"""Evaluating policy on a slippery Frozen Lake
In a slippery Frozen Lake environment, merely deducing the policy from a learned Q-table isn't sufficient to gauge its effectiveness. To accurately assess the suitability of a learned policy, you must play multiple episodes, observing the average reward achieved. This exercise compares the effectiveness of the learned policy against a baseline established by following a random policy during training. Your task is to execute the learned policy over several episodes and analyze its performance based on the average rewards collected, contrasting it with the average rewards collected during the random policy phase.

The Q-table Q, num_states, num_actions, and avg_reward_per_random_episode have been pre-loaded for you. The NumPy library has been imported as np.

Instructions
In each iteration, select the best action to take based on learned Q-table Q.
Compute the average reward per learned episode avg_reward_per_learned_episode.
"""

for episode in range(10000):
    state, info = env.reset()
    terminated = False
    episode_reward = 0
    while not terminated:
        # Select the best action based on learned Q-table
        action = policy[state]
        new_state, reward, terminated, truncated, info = env.step(action)
        state = new_state
        episode_reward += reward
    reward_per_learned_episode.append(episode_reward)
# Compute and print the average reward per learned episode
avg_reward_per_learned_episode = np.mean(reward_per_learned_episode)
print("Average reward per learned episode: ", avg_reward_per_learned_episode)
print("Average reward per random episode: ", avg_reward_per_random_episode)