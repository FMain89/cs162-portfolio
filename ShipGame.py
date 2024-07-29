# Author: Freddie Main III
# GitHub Username: FMain89
# Date: 2/23/2022
# Description: This is a game of battleship between two players.

class ShipGame:
    """
    Description:
            This is the class that represents the game being played. It has several functions, place_ship,
            set_current_state, get_current_state, fire_torpedo, get_num_ships_remaining. This class will also
            utilize class objects from the Boat class. This class will hold the coordinate locations of the ships.
    """

    def __init__(self):
        """
        Description:
                This init function will initial all the baseline conditions for the start of the game
        Parameter:
                NONE
        Returns:
                NONE
        """
        self._state = 'UNFINISHED'  # Initialize state of the game
        self._turn = 'first'  # Initialize the first turn of the game.
        self._ships = {'first': [], 'second': []}  # Key will be player ID and Value will be the ship object.

    def place_ship(self, player_id, length, coordinates, orientation):
        """
        Description:
                Function for placing the ships at the user specified coordinates.
        Parameter:
                player_id(str): String value of the user placing the ship, either 'first' or 'second'
                length(int): integer representing the length of the ship
                coordinates(str): string value representing the uppermost left location of the ship being placed.
                orientation(str): string value of 'R' or 'C' for same row or column of the coordinate input.
        Returns:
                True: If the place ship was a valid move and could be placed.
                False: If the place ship is an invalid move, too small or a bad location.
        """
        if length >= 2 and (orientation.upper() == "C" or orientation.upper() == "R"):
            boat_obj = Boat(player_id, length, coordinates, orientation)
        else:
            return False

        if boat_obj.validate_ship_placement():
            if self.check_ship_placement_overlap(player_id, boat_obj):
                boat_list = self.get_ships(player_id)
                boat_list.append(boat_obj)
                self._ships.update({player_id: boat_list})  # adds to list.
                return True
            else:
                return False
        else:
            return False

    def set_current_state(self):
        """
        Description:
                sets the state of the game, First won, Second won, or unfinished
        Parameter:
                NONE
        Returns:
                NONE
        """

        if self.get_num_ships_remaining('first') == 0:
            self._state = 'SECOND_WON'
        if self.get_num_ships_remaining('second') == 0:
            self._state = 'FIRST_WON'

    def get_current_state(self):
        """
        Description:
                Returns the state of the game, First won, Second won, or unfinished
        Parameter:
                NONE
        Returns:
                self._state which is a docstring
        """
        return self._state

    def fire_torpedo(self, player_id, firing_coordinates):
        """
        Description:
                The function to play the game, this is the guess and fire function of the torpedoes of Battleship.
        Parameter:
                player_id(str): String value of the user firing the torpedo, either 'first' or 'second'
                coordinates(str): Coordinate to fire the torpedo.
        Returns:
                True: if the move was valid. (it was the players turn, and the game isn't over.)
                False: if the move was invalid. (game is over, or it wasn't that players turn)
        """
        row_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        fire_coord = firing_coordinates.upper()

        if fire_coord[0] in row_list:
            fire_coord_row = row_list.index(fire_coord[0]) + 1
        else:
            return False

        if int(fire_coord[1:]) <= 10:
            fire_coord_col = int(fire_coord[1:])
        else:
            return False

        torpedo_coord = [fire_coord_row, fire_coord_col]

        if player_id == self._turn and self._state == 'UNFINISHED':

            # Start the firing process.
            target_player_boats = []
            if player_id == 'first':
                target_player = 'second'
                target_player_boats = self.get_ships('second')
            else:
                target_player = 'first'
                target_player_boats = self.get_ships('first')

            current_boat_index = 0
            for target_boat in target_player_boats:

                if torpedo_coord in target_boat.get_list_coord():
                    hit_boat = target_player_boats[current_boat_index]
                    hit_boat.get_list_coord().remove(torpedo_coord)
                    target_player_boats[current_boat_index] = hit_boat
                    if len(hit_boat.get_list_coord()) == 0:
                        target_player_boats.remove(hit_boat)
                        self.set_current_state()
                # We already acknowledge the boat was hit. So we're done with the for-loop
                current_boat_index += 1

            # Change whose turn it is
            if player_id == 'first':
                self._turn = 'second'
            else:
                self._turn = 'first'
            return True
        else:
            return False

    def get_num_ships_remaining(self, player_id):
        """
        Description:
                This is the function to check to see if the game is over or not, it sees the number of ships the player
                has remaining.
        Parameter:
                player_id(str): String value of the user to see ships remaining, either 'first' or 'second'
        Returns:
              ship_remaining(int): Integer of how many ship the parameter user has remaining.
        """
        return len(self.get_ships(player_id))

    def get_ships(self, player_id):
        """
        Description:
                Get method for the ships in the dictionary
        Parameter:
                player_id(str): String identifier for the player.
        Returns:
                list of the ships based on the players_id.
        """
        return self._ships.get(player_id)

    def check_ship_placement_overlap(self, player_id, boat_being_placed):
        """
        Description:
                This is a method to test valid placement, specifically for the overlapping case.
        Parameter:
                player_id(str): String identifier for the player.
                boat_being_placed(obj): the boat object.
        Returns:
                True: if the boats don't overlap
                False: if the boats do overlap.
        """
        for current_boat_coords in boat_being_placed.get_list_coord():
            existing_ships = self.get_ships(player_id)
            if existing_ships is None or len(existing_ships) == 0:
                return True

            for existing_ship in existing_ships:
                if current_boat_coords in existing_ship.get_list_coord():
                    return False
        return True


class Boat:
    """
    This class will take the information given by place_ship and store the information as a class object.
    """

    def __init__(self, player_id, length, coordinates, orientation):
        """
        Description:
                The init method for this class.
        Parameter:
                player_id(str): String value of the user placing the ship, either 'first' or 'second'
                length(int): integer representing the length of the ship
                coordinates(str): string value representing the uppermost left location of the ship being placed.
                orientation(str): string value of 'R' or 'C' for same row or column of the coordinate input.
        Returns:
                None
        """
        self._player_id = player_id
        self._orientation = orientation.upper()
        self._length = length
        self._coord = coordinates.upper()
        self._list_coord = []

    def validate_ship_placement(self):
        """
        Description:
                This method is to perform all the checks on a ship to make sure its location is valid.

        Parameter:
                None.
        Returns:
                True: This is a valid placement.
                False: This is an invalid placement.
        """
        row_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        column_size = 10
        boat_length = self.get_length()
        boat_starting_coord = self.get_coord()
        boat_orientation = self.get_orientation()
        boat_starting_row = boat_starting_coord[0]
        boat_starting_col = int(boat_starting_coord[1:])
        row_value = row_list.index(boat_starting_row) + 1
        width = 1
        height = 1

        # Set the boat orientation and add its coordinates
        if boat_orientation == 'C':
            height = boat_length
            # up and down
            for current_boat_coord in range(boat_length):
                self._list_coord.append([current_boat_coord + row_value, boat_starting_col])
        else:
            width = boat_length
            # left and right
            for current_boat_coord in range(boat_length):
                self._list_coord.append([row_value, current_boat_coord + boat_starting_col])

        # First check row values.
        if boat_starting_row not in row_list or (row_value + height) - 1 > len(row_list):
            return False

        # Next check column values.
        if boat_starting_col > column_size or (boat_starting_col + width) - 1 > column_size:
            return False

        # All checks have passed.
        return True

    def get_coord(self):
        """
        Description:
                This is a method to return the coordinates as a list.
        Parameter:
                None.
        Returns:
                self._coord(list): returns a list of coordinates the ship object sits on.
        """
        return self._coord

    def get_length(self):
        """
        Description:
                This is a method to return the length of the Boat object.
        Parameter:
                None.
        Returns:
                self._length(int): length of the ship as an integer.
        """
        return self._length

    def get_orientation(self):
        """
        Description:
                This is a method to return the orientation of the Boat object.
        Parameter:
                None
        Returns:
                self._orientation(str): String value of either "C" for column, or "R" for row.
        """
        return self._orientation

    def get_list_coord(self):
        """
        Description:
                get method for the coordinates in a list.
        Parameter:
                None:
        Returns:
                list_coord: this is a list of coordinates.
        """
        return self._list_coord

    def get_player_id(self):
        """
        Description:
                get method for the player id
        Parameter:
                None.
        Returns:
                player_id(str): returns the player ID as a string.
        """
        return self._player_id


# Testing Code from Readme
def main():
    game = ShipGame()
    game.place_ship('first', 5, 'B2', 'C')
    game.place_ship('first', 2, 'I8', 'R')
    game.place_ship('second', 3, 'H2', 'C')
    game.place_ship('second', 2, 'A1', 'C')
    game.place_ship('first', 8, 'H2', 'R')
    game.fire_torpedo('first', 'H3')
    game.fire_torpedo('second', 'A1')
    print(game.get_current_state())


if __name__ == '__main__':
    main()
