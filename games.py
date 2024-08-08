import random

def player(prev_play, opponent_history=[]):
    if prev_play in ['R', 'P', 'S']:
        opponent_history.append(prev_play)

    # Analyze opponent history
    if len(opponent_history) > 1:
        last_move = opponent_history[-1]
        counter = {'R': 'P', 'P': 'S', 'S': 'R'}
        return counter[last_move]
    
    # Start with a random choice
    return random.choice(['R', 'P', 'S'])
