"""Expected SARSA update rule
In this exercise, you'll implement the Expected SARSA update rule, a temporal difference model-free RL algorithm. Expected SARSA estimates the expected value of the current policy by averaging over all possible actions, providing a more stable update target compared to SARSA. The formulas used in Expected SARSA can be found below.

Image showing the mathematical formula of the expected SARSA update rule.

The numpy library has been imported as np.

Instructions
Calculate the expected Q-value for the next_state.
Update the Q-value for the current state and action using the Expected SARSA formula.
Update the Q-table Q supposing that an agent takes action 1 in state 2 and moves to state 3, receiving a reward of 5.
"""

def update_q_table(state, action, next_state, reward):
  	# Calculate the expected Q-value for the next state
    expected_q = np.mean(Q[next_state])
    # Update the Q-value for the current state and action
    Q[state, action] = ((1 - alpha) * Q[state, action]) + (alpha * (reward + (gamma * expected_q)))
    
Q = np.random.rand(5, 2)
print("Old Q:\n", Q)
alpha = 0.1
gamma = 0.99

# Update the Q-table
update_q_table(2, 1, 3, 5)
print("Updated Q:\n", Q)



"""Applying Expected SARSA
Now you'll apply the Expected SARSA algorithm in a custom environment as shown below, where the goal is to let an agent navigate through a grid, aiming to reach a goal as quickly as possible. The same rules we had before apply: the agent receives a reward of +10 when reaching the diamond, -2 when passing through a mountain, and -1 for every other state.

new_cust_env.png

The environment has been imported as env.

Instructions
Initialize the Q-table Q with zeros for each state-action pair.
Update the Q-table using the update_q_table() function.
Extract the policy as a dictionary from the learned Q-table.
"""

# Initialize the Q-table with random values
Q = np.zeros((env.observation_space.n, env.action_space.n))
for i_episode in range(num_episodes):
    state, info = env.reset()    
    done = False    
    while not done: 
        action = env.action_space.sample()               
        next_state, reward, done, truncated, info = env.step(action)
        # Update the Q-table
        update_q_table(state, action, next_state, reward)
        state = next_state
# Derive policy from Q-table        
policy = {state: np.argmax(Q[state]) for state in range(env.observation_space.n)}
render_policy(policy)



"""Implementing double Q-learning update rule
Double Q-learning is an extension of the Q-learning algorithm that helps to reduce overestimation of action values by maintaining and updating two separate Q-tables. By decoupling the action selection from the action evaluation, Double Q-learning provides a more accurate estimation of the Q-values. This exercise guides you through implementing the Double Q-learning update rule. A list Q containing two Q-tables has been generated.

The numpy library has been imported as np, and gamma and alpha values have been pre-loaded. The update formulas are below:

Image showing the update rule of Q1.

Image showing the update rule of Q2.

Instructions
Randomly decide which Q-table within Q to update for the action value estimation by computing its index i.
Perform the necessary steps to update Q[i].
"""

Q = [np.random.rand(8,4), np.random.rand(8,4)] 
def update_q_tables(state, action, reward, next_state):
  	# Get the index of the table to update
    i = np.randint(0, 2)
    # Update Q[i]
    best_next_action = ((1 - alpha) * Q[i][state, action]) + alpha * (reward + gamma * Q[1-i][next_state, action])
    Q[i][state, action] = best_next_action


"""Applying double Q-learning
This exercise tasks you with applying the Double Q-learning algorithm in the same custom environment you solved with Expected SARSA to investigate the difference. Double Q-learning, by using two Q-tables, helps reduce the overestimation bias inherent in the traditional Q-learning algorithm and offers more stability in learning than other temporal difference methods. You'll use this method to navigate through the grid environment, aiming for the highest reward while avoiding mountains in order to reach the goal as quickly as possible.

new_cust_env.png

Instructions
Update the Q-tables using the update_q_tables() function you coded in the previous exercise.
Combine the Q-tables by summing them.
"""

Q = [np.zeros((num_states, num_actions))] * 2
for episode in range(num_episodes):
    state, info = env.reset()
    terminated = False   
    while not terminated:
        action = np.random.choice(num_actions)
        next_state, reward, terminated, truncated, info = env.step(action)
        # Update the Q-tables
        update_q_tables(state, action, reward, next_state)
        state = next_state
# Combine the learned Q-tables        
Q = Q[0] + Q[1]
policy = {state: np.argmax(Q[state]) for state in range(num_states)}
render_policy(policy)



"""Defining epsilon-greedy function
In RL, the epsilon-greedy strategy is a balance between exploration and exploitation. This method chooses a random action with probability epsilon and the best-known action with probability 1-epsilon. Implementing the epsilon_greedy() function is crucial for algorithms like Q-learning and SARSA, facilitating the agent's learning process by ensuring both exploration of the environment and exploitation of known rewards, and this will be the goal of this exercise.

The numpy library has been imported as np.

Instructions
Inside the function, write the suitable condition for an agent to explore the environment.
Choose a random action when exploring.
Choose the best action according to the q_table when exploiting.
"""

epsilon = 0.2
env = gym.make('FrozenLake')
q_table = np.random.rand(env.observation_space.n, env.action_space.n)

def epsilon_greedy(state):
    # Implement the condition to explore
    if np.random.rand() < epsilon:
      	# Choose a random action
        action = env.action_space.sample()
    else:
      	# Choose the best action according to q_table
        action = np.argmax(q_table[state, :])
    return action



"""Solving CliffWalking with epsilon greedy strategy
The CliffWalking environment is a standard testbed for RL algorithms. It's a grid world where an agent must find a path from a start state to a goal state, avoiding cliffs along the way. Using the epsilon-greedy strategy allows the agent to explore the environment effectively while learning to avoid cliffs, maximizing the cumulative reward. Your task is to solve this environment using the epsilon-greedy strategy, compute the rewards attained in each training episode, and save them to the rewards_eps_greedy list.

Instructions
Within an episode, select an action using the epsilon_greedy() function.
Accumulate the received reward to the episode_reward.
After each episode, append the total episode_reward to the rewards_eps_greedy list for later analysis.
"""

rewards_eps_greedy = []
for episode in range(total_episodes):
    state, info = env.reset()
    episode_reward = 0
    for i in range(max_steps):
      	# Select action with epsilon-greedy strategy
        action = epsilon_greedy(state)
        next_state, reward, terminated, truncated, info = env.step(action)
        # Accumulate reward
        episode_reward += reward
        update_q_table(state, action, reward, next_state)
        state = next_state
    # Append the toal reward to the rewards list 
    rewards_eps_greedy.append(episode_reward)
print("Average reward per episode: ", np.mean(rewards_eps_greedy))



"""Solving CliffWalking with decayed epsilon-greedy strategy
Enhancing the epsilon-greedy strategy, a decay factor is introduced to gradually decrease the exploration rate, epsilon, as the agent learns more about the environment. This approach promotes exploration in the early stages of learning and exploitation of the learned knowledge as the agent becomes more familiar with the environment. Now, you'll apply this strategy to solve the CliffWalking environment.

The environment has been initialized, and can be accessed by the variable env. The variables epsilon, min_epsilon, and epsilon_decay have been pre-defined for you. The functions epsilon_greedy() and update_q_table() have been imported.

Instructions
Implement the full training loop by choosing an action, executing it, accumulating the reward received to episode_reward, updating the Q-table.
Decrease epsilon using the epsilon_decay rate, ensuring it does not fall below min_epsilon.
"""

rewards_decay_eps_greedy = []
for episode in range(total_episodes):
    state, info = env.reset()
    episode_reward = 0
    for i in range(max_steps):
      	# Implement the training loop
        action = epsilon_greedy(state)
        new_state, reward, terminated, truncated, info = env.step(action)
        episode_reward += reward
        update_q_table(state, action, reward, new_state)
        state = new_state
    rewards_decay_eps_greedy.append(episode_reward)
    # Update epsilon
    epsilon = max(min_epsilon, epsilon * epsilon_decay)
print("Average reward per episode: ", np.mean(rewards_decay_eps_greedy))



"""Creating a multi-armed bandit
A multi-armed bandit problem is a classic example used in reinforcement learning to describe a scenario where an agent must choose between multiple actions (or "arms") without knowing the expected reward of each. Over time, the agent learns which arm yields the highest reward by exploring each option. This exercise involves setting up the foundational structure for simulating a multi-armed bandit problem.

The numpy library has been imported as np.

Instructions
Generate an array true_bandit_probs with random probabilities representing the true underlying success rate for each bandit.
Initialize two arrays, counts and values, with zeros; counts tracks the number of times each bandit has been chosen, and values represents the estimated winning probability of each bandit.
Create rewards and selected_arms arrays, to store the rewards obtained and the arms selected in each iteration.
"""

def create_multi_armed_bandit(n_bandits):
    # Generate the true bandits probabilities
    true_bandit_probs = np.random.rand(n_bandits)
    # Create arrays that store the count and value for each bandit
    counts = np.zeros(n_bandits)
    values = np.zeros(n_bandits)
    # Create arrays that store the rewards and selected arms each episode
    rewards = np.zeros(n_iterations)
    selected_arms = np.zeros(n_iterations, dtype=int)
    return true_bandit_probs, counts, values, rewards, selected_arms



"""Solving a multi-armed bandit
This exercise involves implementing an epsilon-greedy strategy to solve a 10-armed bandit problem, where the epsilon value decays over time to shift from exploration to exploitation.

epsilon, min_epsilon, and epsilon_decay have been pre-defined for you. The epsilon_greedy() function has been imported as well.

Instructions
Use the create_multi_armed_bandit() function to initialize a 10-armed bandit problem, which will return true_bandit_probs, counts, values, rewards, and selected_arms.
Select an arm to pull using the epsilon_greedy() function.
Simulate the reward based on the true bandit probabilities.
Decay the epsilon value ensuring that it does not fall below the min_epsilon value.
"""

# Create a 10-armed bandit
true_bandit_probs, counts, values, rewards, selected_arms = create_multi_armed_bandit(10)

for i in range(n_iterations): 
    # Select an arm
    arm = epsilon_greedy()
    # Compute the received reward
    reward = np.random.rand() < true_bandit_probs[arm]
    rewards[i] = reward
    selected_arms[i] = arm
    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]
    # Update epsilon
    epsilon = max(min_epsilon, epsilon * epsilon_decay)



"""Assessing convergence in a multi-armed bandit
Evaluating the performance and convergence of strategies in a multi-armed bandit problem is crucial for understanding their effectiveness. By analyzing how frequently each arm is selected over time, we can infer the learning process and the strategy's ability to identify and exploit the best arm. This exercise involves visualizing the selection percentages of each arm over iterations to assess the convergence of an epsilon-greedy strategy.

The selected_arms array that shows which arm has been pulled in each iteration has been pre-loaded for you.

Instructions
Initialize an array selections_percentage with zeros, with dimensions to track the selection percentage of each bandit over time.
Get the selections_percentage over time by calculating the cumulative sum of selections for each bandit over iterations, and dividing by the iteration number.
Plot the cumulative selection percentages for each bandit, to visualize how often each bandit is chosen over iterations.
"""

# Initialize the selection percentages with zeros
selections_percentage = np.zeros((n_iterations, n_bandits))
for i in range(n_iterations):
    selections_percentage[i, selected_arms[i]] = 1
# Compute the cumulative selection percentages 
selections_percentage = np.cumsum(selections_percentage, axis=0) / np.arange(1, n_iterations + 1).reshape(-1, 1)
for arm in range(n_bandits):
    # Plot the cumulative selection percentage for each arm
    plt.plot(selections_percentage[:, arm], label=f'Bandit #{arm+1}')
plt.xlabel('Iteration Number')
plt.ylabel('Percentage of Bandit Selections (%)')
plt.legend()
plt.show()
for i, prob in enumerate(true_bandit_probs, 1):
    print(f"Bandit #{i} -> {prob:.2f}")