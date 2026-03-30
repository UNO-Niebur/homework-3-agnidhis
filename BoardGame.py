# Homework 3 - Board Game System
# Name: Nidhi Agarwal
# Date: 3/30/2026

def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)

def main():
    filename = "events.txt"   
    gameData = loadGameData(filename)
    displayGame(gameData)

    # Example interaction
    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        movePlayer(gameData)


def load_game_data(filename):
    players = {}      
    events = {}       
    turn = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("Turn:"):
                turn = line.split(":")[1].strip()

            else:
                parts = line.split(":")
                position = int(parts[0])
                value = parts[1].strip()

                if value.startswith("Player"):
                    players[value] = position
                else:
                    events[position] = value

    return players, events, turn


def display_board(players, events, board_size=25):
    print("\n--- GAME BOARD ---")

    for i in range(board_size):
        space = f"{i}"

        # Check for player
        for player, pos in players.items():
            if pos == i:
                space += f"[{player}]"

        # Check for event
        if i in events:
            space += f"({events[i]})"

        print(space, end=" | ")

    print("\n")


def move_player(players, current_player):
    steps = int(input(f"{current_player}, enter steps to move: "))
    players[current_player] += steps
    print(f"{current_player} moved to position {players[current_player]}")


def check_event(players, current_player, events):
    position = players[current_player]

    if position in events:
        print(f"Event triggered: {events[position]}!")

        # Simple example effect
        if events[position] == "Troll":
            print("Oh no! Move back 2 spaces.")
            players[current_player] -= 2

        elif events[position] == "Hotel":
            print("Nice! Stay here and rest.")


def switch_turn(players, current_player):
    player_list = list(players.keys())
    index = player_list.index(current_player)

    next_index = (index + 1) % len(player_list)
    return player_list[next_index]


def main():
    players, events, current_player = load_game_data("events.txt")

    while True:
        display_board(players, events)

        print(f"\nCurrent Turn: {current_player}")

        move_player(players, current_player)
        check_event(players, current_player, events)

        # Switch turn
        current_player = switch_turn(players, current_player)

        # Simple exit option
        choice = input("Continue? (y/n): ")
        if choice.lower() != "y":
            print("Game ended.")
            break



main()


if __name__ == "__main__":
    main()
