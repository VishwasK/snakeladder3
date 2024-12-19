```python
import random

def snake_and_ladder():
    board = {
        1: 1, 4: 25, 8: 13, 11: 6, 14: 30,
        16: 10, 19: 3, 22: 37, 24: 16,
        26: 12, 28: 43, 33: 2, 35: 17,
        39: 50, 41: 20, 46: 5, 48: 63,
        52: 81, 55: 18, 57: 59, 60: 32,
        62: 65, 64: 45, 67: 71, 73: 69,
        76: 44, 78: 54, 80: 99, 82: 89,
        84: 21, 87: 100, 91: 68, 93: 70,
        95: 23, 98: 79
    }

    player_pos = 1
    while player_pos < 100:
        dice = random.randint(1, 6)
        print(f"You rolled a {dice}")
        player_pos += dice

        if player_pos in board:
            player_pos = board[player_pos]
            if player_pos > dice:
                print("Yay! You climbed a ladder.")
            else:
               print("Oops! You encountered a snake")

        if player_pos > 100:
            player_pos -= dice
            print("You need to get to 100 to win, Try Again!")
        else:
            print(f"Your position is {player_pos}")

    print("Congratulations! You won!")

if __name__ == "__main__":
    snake_and_ladder()
```
