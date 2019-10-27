/* If a player rolls three consecutive doubles, they proceed directly to jail.
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
6-sided dice, two 4-sided dice are used, find the six-digit modal string. */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct
{
    int cards[16];
    int picked;
} Deck;

int* bigThree(int* arr, int size);
int* fillBoard(Deck* chance, Deck* chest, int turns);
void pickCard(Deck* deck, int* cur);
void checkDoubles(int* roll, int* doubles);
void rollDice(int* dice, int sides);
void initDeck(Deck* deck, int* vals, int size);
void shuffle(int* deck);
void swap(int *a, int *b);

// Driver function
int main(void)
{
    srand(time(NULL));

    Deck chance, chest;
    int vals[10] = { 0, 5, 10, 11, 24, 39, 40, 40, 41, 42 };
    initDeck(&chance, vals, 10);
    vals[1] = 10;
    initDeck(&chest, vals, 2);

    int* board = fillBoard(&chance, &chest, 10000000);
    int* top = bigThree(board, 40);

    for (int i = 0; i < 3; i++)
        printf("%i", top[i]);
    printf("\n");

    return 0;
}

// Return 'indices' of the 3 largest elements in 'arr'
int* bigThree(int* arr, int size)
{
    int vals[3] = { 0 };
    static int indices[3] = { 0 };

    for (int i = 0; i < size; i++)
    {
        if (arr[i] > vals[0])
        {
            vals[2] = vals[1];
            vals[1] = vals[0];
            vals[0] = arr[i];
            indices[2] = indices[1];
            indices[1] = indices[0];
            indices[0] = i;
        }

        else if (arr[i] > vals[1])
        {
            vals[2] = vals[1];
            vals[1] = arr[i];
            indices[2] = indices[1];
            indices[1] = i;
        }

        else if (arr[i] > vals[2])
        {
            vals[2] = arr[i];
            indices[2] = i;
        }
    }

    return indices;
}
// Simulate moving around 'board' for 'turns'
int* fillBoard(Deck* chance, Deck* chest, int turns)
{
    static int board[40] = { 0 };
    int cur = 0, doubles = 0;
    int dice[2];

    for (int i = 0; i < turns; i++)
    {
        board[cur] += 1;

        rollDice(dice, 4);
        checkDoubles(dice, &doubles);
        if (doubles == 3)
        {
            cur = 10;
            doubles = 0;
            continue;
        }

        cur = (dice[0] + dice[1] + cur) % 40;

        switch (cur)
        {
            case 2:
            case 17:
            case 33:
                pickCard(chest, &cur);
                chest->picked += 1;
                continue;
            case 7:
            case 22:
            case 36:
                pickCard(chance, &cur);
                chance->picked += 1;
                continue;
            case 30:
                cur = 10;
                continue;
            default:
                continue;
        }
    }

    board[0] -= 1;
    return board;
}

// Return new 'cur' location after picking 'card' from 'deck'
void pickCard(Deck* deck, int* cur)
{
    if (deck->picked == 16)
        deck->picked = 0;

    int card = deck->cards[deck->picked];
    switch (card)
    {
        case -1:
            break;
        case 40:
            if (*cur == 7)
                *cur = 15;
            else if (*cur == 22)
                *cur = 25;
            else
                *cur = 5;
            break;
        case 41:
            if (*cur == 7 || *cur == 36)
                *cur = 12;
            else
                *cur = 28;
            break;
        case 42:
            *cur -= 3;
            break;
        default:
            *cur = card;
    }
}

// Update the number of consecutive 'doubles' based on 'roll'
void checkDoubles(int* roll, int* doubles)
{
    if (roll[1] == roll[0])
        *doubles += 1;
    else
        *doubles = 0;
}

// Simulate a dice roll
void rollDice(int* dice, int sides)
{
    dice[0] = (rand() % sides) + 1;
    dice[1] = (rand() % sides) + 1;
}

/* Initialize 'deck'. Out of a total of 16 'cards', 'size' spots are taken by the
numbers in 'vals' */
void initDeck(Deck* deck, int* vals, int size)
{
    deck->picked = 0;
    for (int i = 0; i < size; i++)
        deck->cards[i] = vals[i];
    for (int i = size; i < 16; i++)
        deck->cards[i] = -1;
    shuffle(deck->cards);
}

// Simulate shuffling 'deck'
void shuffle(int* deck)
{
	for (int i = 0; i < 16; i++)
    {
		int index = rand() % (16 - i) + i;
		swap(deck + i, deck + index);
	}
}

// Swap values of 'a' and 'b'
void swap(int *a, int *b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}
