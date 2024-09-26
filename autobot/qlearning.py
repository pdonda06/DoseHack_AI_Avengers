import numpy as np
import random
import numpy as np
import random


class QLearningAgent:
    def __init__(self, actions, grid_size, alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decay=0.99):
        self.actions = actions
        self.q_table = np.zeros(grid_size + (len(actions),))
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.epsilon_decay = epsilon_decay  # Decay rate for epsilon
        self.epsilon_min = 0.01  # Minimum exploration rate

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)  # Explore
        else:
            return self.actions[np.argmax(self.q_table[state])]  # Exploit

    def learn(self, state, action, reward, next_state):
        action_index = self.actions.index(action)
        q_predict = self.q_table[state][action_index]
        q_target = reward + self.gamma * np.max(self.q_table[next_state])  # Bellman equation
        self.q_table[state][action_index] += self.alpha * (q_target - q_predict)

        # Decay epsilon to reduce exploration over time
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def reset_epsilon(self):
        """ Reset epsilon for a new training session or testing phase """
        self.epsilon = 1.0
