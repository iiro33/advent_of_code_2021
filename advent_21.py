# advent of code
# anonymous user #1879507


def main():
    player_1_pos = 4 - 1  # grid starts from 1 => pos 0 = 1 grid value
    player_2_pos = 1 - 1
    player_1_score, player_2_score = 0, 0
    rolls = 0
    grid = list(range(1, 11))
    deterministic_die = list(range(1, 101))
    turn = 1

    while True:
        turn_roll_sum = 0  # calculate turn sum to separate variable
        if player_1_score >= 1000 or player_2_score >= 1000:
            break  # only way to exit loop
        for _ in range(3):  # roll three times
            die_pos = rolls % len(deterministic_die)  # e.g. 100 rolls = 100%100 = 0 => die value of 1
            value = deterministic_die[die_pos]
            turn_roll_sum += value
            rolls += 1
        if turn == 1:  # player 1's turn
            player_1_pos = (player_1_pos + turn_roll_sum) % len(grid)  # update position on grid by
            player_1_score += grid[player_1_pos]
        else:  # otherwise, player 2's turn
            player_2_pos = (player_2_pos + turn_roll_sum) % len(grid)
            player_2_score += grid[player_2_pos]
        turn = -turn  # swap turn

    print('losing player score: %s ' % min(player_1_score, player_2_score))
    print('winning player score: %s ' % max(player_1_score, player_2_score))
    print('rolls: %s' % rolls)
    print('multiplied: %s' % (min(player_1_score, player_2_score) * rolls))


if __name__ == '__main__':
    main()
