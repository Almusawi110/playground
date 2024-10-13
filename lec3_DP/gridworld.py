#!/usr/bin/python3
import numpy as np

class GridWorld():
    def __init__(self, env_size):
        self.env_size = env_size
      
        self.terminal_state = (4, 4)

        # Gray state locations (non-favorable states)
        self.gray_states = [(0,4),(1, 2), (3, 0)]

        # Define the transition probabilities and rewards
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        self.action_description = ["Right", "Left", "Down", "Up"]

        # Assign a vector of rewards for each of the states
        self.reward = np.ones((self.env_size, self.env_size))*-1
        self.reward[self.terminal_state] = 10
        for state in self.gray_states:
            self.reward[state] = -5
    '''@brief Returns the next state given the chosen action and current state
    '''
    def step(self, action_index, i, j):
        # We are assuming a Transition Probability Matrix where
        # P(s'|s) = 1.0 for a single state and 0 otherwise
        action = self.actions[action_index]
        next_i, next_j = i + action[0], j + action[1]
        if not self.is_valid_state(next_i, next_j):
            next_i, next_j = i, j
        
        done = self.is_terminal_state(next_i, next_j)
        reward = self.reward[next_i, next_j]
        return next_i, next_j, reward, done
    
    '''@brief Checks if a state is within the acceptable bounds of the environment
    '''
    def is_valid_state(self, i, j):
        valid = 0 <= i < self.env_size and 0 <= j < self.env_size
        return valid
    
    '''@brief Returns True if the state is a terminal state
    '''
    def is_terminal_state(self, i, j):
        return (i, j) == self. terminal_state
    
    def get_size(self):
        return self.env_size

    def get_actions(self):
        return self.actions