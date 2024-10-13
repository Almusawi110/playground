import numpy as np
import matplotlib.pyplot as plt

# Define the gridworld policy
policy = [
    ['Right|Down', 'Right|Down', 'Right', 'Down', 'Down'],
    ['Right|Down', 'Down', 'Right|Down', 'Right|Down', 'Down'],
    ['Right', 'Right|Down', 'Right|Down', 'Right|Down', 'Down'],
    ['Right|Down', 'Right|Down', 'Right|Down', 'Right|Down', 'Down'],
    ['Right', 'Right', 'Right', 'Right', 'X']
]

def draw_gridworld(policy):
    fig, ax = plt.subplots()
    size = len(policy)
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_xticks(np.arange(0, size+1, 1))
    ax.set_yticks(np.arange(0, size+1, 1))
    ax.grid(True)

    for i in range(size):
        for j in range(size):
            action = policy[i][j]

            # Draw the terminal state
            if action == 'X':
                ax.text(j + 0.5, size - i - 0.5, 'Goal', va='center', ha='center', fontsize=12, color='red')
            else:
                # Draw arrows based on the action
                if 'Right' in action:
                    ax.arrow(j + 0.2, size - i - 0.5, 0.6, 0, head_width=0.1, head_length=0.1, fc='blue', ec='blue')
                if 'Down' in action:
                    ax.arrow(j + 0.5, size - i - 0.2, 0, -0.6, head_width=0.1, head_length=0.1, fc='green', ec='green')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Draw the gridworld with the policy
draw_gridworld(policy)
