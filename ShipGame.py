# Author: Freddie Main III
# GitHub Username: FMain89
# Date: 2/23/2022
# Description: This is a game of battleship between two players.

class ShipGame:
    """
    A class to represent the Battleship game.
    """

    def __init__(self):
        """
        Initializes the game with default values.
        """
        self._state = 'UNFINISHED'
        self._turn = 'first'
        self._ships = {'first': [], 'second': []}
        self._board_size = 10
        self._ship_coordinates = {'first': set(), 'second': set()}
        self._game_started = False
        self._hit_positions = {'first': set(), 'second': set()}
        self._fired_positions = {'first': set(), 'second': set()}

    def place_ship(self, player_id, length, coordinates, orientation):
        """
        Places a ship on the board for the given player.

        Parameters:
        - player_id (str): 'first' or 'second'
        - length (int): Length of the ship
        - coordinates (str): Starting coordinate (e.g., 'A1')
        - orientation (str): 'R' for row, 'C' for column

        Returns:
        - bool: True if ship placed successfully, False otherwise
        """
        if self._game_started:
            return False

        if length < 2 or orientation not in ['R', 'C']:
            return False

        row_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        try:
            start_row = row_list.index(coordinates[0])
        except ValueError:
            return False
        try:
            start_col = int(coordinates[1:]) - 1
        except ValueError:
            return False

        if start_row >= self._board_size or start_col >= self._board_size:
            return False

        if orientation == 'C':
            if start_row + length > self._board_size:
                return False
            ship_coords = {(start_row + i, start_col) for i in range(length)}
        else:
            if start_col + length > self._board_size:
                return False
            ship_coords = {(start_row, start_col + i) for i in range(length)}

        if self._is_overlap(player_id, ship_coords):
            return False

        self._ships[player_id].append(ship_coords)
        self._ship_coordinates[player_id].update(ship_coords)
        return True

    def _is_overlap(self, player_id, new_ship_coords):
        """
        Checks if a new ship overlaps with existing ships.

        Parameters:
        - player_id (str): 'first' or 'second'
        - new_ship_coords (set): Set of coordinates for the new ship

        Returns:
        - bool: True if there is an overlap, False otherwise
        """
        return any(coord in self._ship_coordinates[player_id] for coord in
                   new_ship_coords)

    def get_current_state(self):
        """
        Returns the current state of the game.

        Returns:
        - str: 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'
        """
        return self._state

    def fire_torpedo(self, player_id, target):
        """
        Fires a torpedo at the specified coordinates on the opponent's grid.

        Parameters:
        - player_id (str): 'first' or 'second'
        - target (str): Target coordinates (e.g., 'B7')

        Returns:
        - bool: True if the torpedo was fired successfully, False otherwise
        """
        if self._state != 'UNFINISHED' or self._turn != player_id:
            return False

        row_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        try:
            target_row = row_list.index(target[0])
        except ValueError:
            return False

        try:
            target_col = int(target[1:]) - 1
        except ValueError:
            return False

        if target_row >= self._board_size or target_col >= self._board_size:
            return False

        if (target_row, target_col) in self._fired_positions[player_id]:
            self._turn = 'second' if player_id == 'first' else 'first'
            return True

        self._fired_positions[player_id].add((target_row, target_col))

        opponent = 'second' if player_id == 'first' else 'first'
        hit = False
        for ship in self._ships[opponent]:
            if (target_row, target_col) in ship:
                ship.remove((target_row, target_col))
                self._ship_coordinates[opponent].remove((target_row,
                                                         target_col))
                if not ship:
                    self._ships[opponent].remove(ship)
                hit = True
                break

        if hit:
            self._hit_positions[player_id].add((target_row, target_col))

        if not self._ships[opponent]:
            self._state = 'FIRST_WON' if opponent == 'second' else 'SECOND_WON'

        if self._state == 'UNFINISHED':
            self._turn = opponent

        self._game_started = True
        return True

    def get_num_ships_remaining(self, player_id):
        """
        Returns the number of ships remaining for the specified player.

        Parameters:
        - player_id (str): 'first' or 'second'

        Returns:
        - int: Number of ships remaining for the specified player
        """
        return len(self._ships[player_id])


# Testing Code from Readme
def main():
    """
    Main function to test the ShipGame class.
    """
    game = ShipGame()
    print(game.place_ship('first', 5, 'B2', 'C'))  # Expected: True
    print(game.place_ship('first', 2, 'I8', 'R'))  # Expected: True
    print(game.place_ship('second', 3, 'H2', 'C'))  # Expected: True
    print(game.place_ship('second', 2, 'A1', 'C'))  # Expected: True
    print(game.fire_torpedo('first', 'H2'))  # Expected: True
    print(game.fire_torpedo('second', 'I8'))  # Expected: True
    print(game.fire_torpedo('first', 'I2'))  # Expected: True
    print(game.fire_torpedo('second', 'I9'))  # Expected: True
    print(game.get_current_state())  # Expected: UNFINISHED


if __name__ == '__main__':
    main()
