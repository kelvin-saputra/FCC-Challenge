def player(prev_play, opponent_history=[]):
    # DICTIONARY to mapping counter of each RPS State
    moves_counter = {
        'R': 'P', 'P': 'S', 'S': 'R'
    }

    #Reset when begin with the new Opponent
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()

    # From the RPS_GAME.py we know that mostly when player doesn't have any history, the bot wil detect as [R]ock. So the bot will Counter with [P]aper.
    # We will Counter Back the Counter of the Bot
    move_decision = moves_counter[moves_counter['R']]

    # Make Decision for counter the opponent move
    if len(opponent_history) >= 4:
        potential_plays = ["".join(opponent_history[-3:] + [move]) for move in "SRP"]
        # print(potential_plays)
        
        four_move_sequences = ["".join(opponent_history[x:x+4]) for x in range(len(opponent_history)-3)]
        # print(four_move_sequences)

        play_counts = {play: four_move_sequences.count(play) for play in potential_plays}
        # print(play_counts)

        predicted_opponent_move = max(play_counts, key=play_counts.get)[-1]
        # print(predicted_opponent_move)

        move_decision = moves_counter[predicted_opponent_move]
    return move_decision