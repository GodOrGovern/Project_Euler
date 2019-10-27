''' If a player rolls three consecutive doubles, they proceed directly to jail.
At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
Community Chest (2/16 cards): GO, JAIL. Chance (10/16 cards): GO, JAIL, C1, E3,
H2, R1, next R (x2), next U, back 3. The heart of this problem concerns the
likelihood of visiting a particular square. We shall make no distinction
between "Just Visiting" and being in JAIL, and we shall also assume that they
pay to get out on their next turn. By starting at GO and numbering the squares
sequentially from 00 to 39 we can concatenate these two-digit numbers to
produce strings that correspond with sets of squares. If, instead of using two
6-sided dice, two 4-sided dice are used, find the six-digit modal string. '''

from random import shuffle, randint

def main():
    ''' Driver function '''
    chance = [0, [0, 5, 10, 11, 24, 39, 40, 40, 41, 42]+[-1 for _ in range(6)]]
    chest = [0, [0, 10]+[-1 for _ in range(14)]]
    shuffle(chance[1])
    shuffle(chest[1])

    board = fill_board(chance, chest, 200000)
    board_sort = sorted(board)
    result = ''
    for n in range(1, 4):
        result += str(board.index(board_sort[-n]))
    print(result)

def fill_board(chance, chest, turns):
    ''' Simulate moving around 'board' for 'turns'. Mark 'cur' location by
    incrementing counter in array by 1 '''
    board = [0 for _ in range(40)]
    cur, doubles = 0, 0
    for _ in range(turns):
        board[cur] += 1
        dice = [randint(1, 4), randint(1, 4)]
        if dice[0] == dice[1]:
            doubles += 1
        else:
            doubles = 0
        if doubles == 3:
            cur = 10
            doubles = 0
            continue

        cur = (dice[0]+dice[1]+cur) % 40
        if cur in {2, 17, 33}:
            cur = pick_card(chest, cur)
            chest[0] += 1
            continue
        if cur in {7, 22, 36}:
            cur = pick_card(chance, cur)
            chance[0] += 1
            continue
        if cur == 30:
            cur = 10
            continue
    board[0] -= 1
    return board

def pick_card(deck, cur):
    ''' Pick 'card' from the provided 'deck' and return new 'cur' '''
    if deck[0] == 16:
        deck[0] = 0
    card = deck[1][deck[0]]
    if card == -1:
        return cur
    if card == 40:
        return (15, 25, 5)[(cur > 7) + (cur > 22)]
    if card == 41:
        return (12, 28)[cur == 22]
    if card == 42:
        return cur - 3
    return card

if __name__ == "__main__":
    main()
