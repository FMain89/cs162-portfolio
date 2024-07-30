# Author: Freddie Main III
# GitHub Username: FMain89
# Date: 2/23/2022
# Description: This is the unit testing program for various cases.
import unittest
from ShipGame import ShipGame


class TestShipGame(unittest.TestCase):
    def test_place_ship_valid(self):
        """
        Test placing valid ships on the board for both players.
        """
        game = ShipGame()
        self.assertTrue(game.place_ship('first', 5, 'B2', 'C'))
        self.assertTrue(game.place_ship('first', 2, 'I8', 'R'))
        self.assertTrue(game.place_ship('second', 3, 'H2', 'C'))
        self.assertTrue(game.place_ship('second', 2, 'A1', 'C'))

    def test_place_ship_invalid_length(self):
        """
        Test placing ships with invalid length (less than 2).
        """
        game = ShipGame()
        self.assertFalse(game.place_ship('first', 1, 'A1', 'R'))
        self.assertFalse(game.place_ship('second', 1, 'J10', 'C'))

    def test_place_ship_out_of_bounds(self):
        """
        Test placing ships out of the board bounds.
        """
        game = ShipGame()
        self.assertFalse(game.place_ship('first', 5, 'J7', 'R'))
        self.assertFalse(game.place_ship('second', 4, 'H10', 'C'))

    def test_place_ship_overlap(self):
        """
        Test placing overlapping ships on the board.
        """
        game = ShipGame()
        self.assertTrue(game.place_ship('first', 4, 'B2', 'C'))
        self.assertFalse(game.place_ship('first', 3, 'C2', 'R'))

    def test_place_ship_after_game_start(self):
        """
        Test attempting to place a ship after the game has started.
        """
        game = ShipGame()
        game.place_ship('first', 4, 'B2', 'C')
        game.place_ship('second', 4, 'D5', 'R')
        game.fire_torpedo('first', 'D5')
        self.assertFalse(game.place_ship('first', 3, 'A1', 'R'))

    def test_fire_torpedo_valid(self):
        """
        Test firing valid torpedoes and updating the game state.
        """
        game = ShipGame()
        game.place_ship('first', 3, 'B2', 'R')
        game.place_ship('second', 2, 'D4', 'C')
        self.assertTrue(game.fire_torpedo('first', 'D4'))
        self.assertTrue(game.fire_torpedo('second', 'B2'))

    def test_fire_torpedo_invalid_turn(self):
        """
        Test firing torpedoes out of turn.
        """
        game = ShipGame()
        game.place_ship('first', 3, 'B2', 'R')
        game.place_ship('second', 2, 'D4', 'C')
        self.assertTrue(game.fire_torpedo('first', 'D4'))
        self.assertFalse(game.fire_torpedo('first', 'B2'))

    def test_fire_torpedo_repeated(self):
        """
        Test firing torpedoes at the same coordinates repeatedly.
        """
        game = ShipGame()
        game.place_ship('first', 3, 'B2', 'R')
        game.place_ship('second', 2, 'D4', 'C')
        self.assertTrue(game.fire_torpedo('first', 'D4'))
        self.assertTrue(game.fire_torpedo('second', 'B2'))
        self.assertTrue(game.fire_torpedo('first', 'D4'))  # Wastes a turn

    def test_fire_torpedo_out_of_bounds(self):
        """
        Test firing a torpedo out of the board's bounds.
        """
        game = ShipGame()
        game.place_ship('first', 3, 'B2', 'R')
        game.place_ship('second', 2, 'D4', 'C')
        self.assertFalse(game.fire_torpedo('first', 'K11'))
        self.assertFalse(game.fire_torpedo('second', 'Z9'))

    def test_game_state_first_wins(self):
        """
        Test the game state when the first player wins.
        """
        game = ShipGame()
        game.place_ship('first', 2, 'B2', 'R')
        game.place_ship('second', 2, 'D4', 'C')
        game.fire_torpedo('first', 'D4')
        game.fire_torpedo('second', 'B2')
        game.fire_torpedo('first', 'E4')
        game.fire_torpedo('second', 'B3')
        game.fire_torpedo('first', 'D5')
        self.assertEqual(game.get_current_state(), 'FIRST_WON')

    def test_game_state_second_wins(self):
        """
        Test the game state when the second player wins.
        """
        game = ShipGame()
        game.place_ship('first', 2, 'B2', 'R')
        game.place_ship('second', 3, 'D4', 'C')
        game.fire_torpedo('first', 'D4')
        game.fire_torpedo('second', 'B2')
        game.fire_torpedo('first', 'E4')
        game.fire_torpedo('second', 'B3')
        self.assertEqual(game.get_current_state(), 'SECOND_WON')

    def test_get_num_ships_remaining(self):
        """
        Test getting the number of ships remaining for each player.
        """
        game = ShipGame()
        game.place_ship('first', 3, 'B2', 'R')
        game.place_ship('second', 2, 'D4', 'C')
        game.fire_torpedo('first', 'D4')
        game.fire_torpedo('second', 'B2')
        self.assertEqual(game.get_num_ships_remaining('first'), 1)
        self.assertEqual(game.get_num_ships_remaining('second'), 1)

    def test_game_unfinished_state(self):
        """
        Test that the game remains unfinished until all ships of a player are
        sunk.
        """
        game = ShipGame()
        game.place_ship('first', 3, 'B2', 'R')
        game.place_ship('second', 3, 'D4', 'C')
        game.fire_torpedo('first', 'D4')
        game.fire_torpedo('second', 'B2')
        game.fire_torpedo('first', 'E4')
        self.assertEqual(game.get_current_state(), 'UNFINISHED')

    def test_full_game(self):
        """
        Test a full game played from start to finish with both players
        alternating turns.
        """
        game = ShipGame()
        game.place_ship('first', 3, 'A1', 'R')
        game.place_ship('first', 2, 'C1', 'C')
        game.place_ship('second', 3, 'E1', 'R')
        game.place_ship('second', 2, 'G1', 'C')

        game.fire_torpedo('first', 'E1')
        game.fire_torpedo('second', 'A1')
        game.fire_torpedo('first', 'E2')
        game.fire_torpedo('second', 'A2')
        game.fire_torpedo('first', 'E3')   # Sinks Ship
        game.fire_torpedo('second', 'A3')   # Sinks Ship
        game.fire_torpedo('first', 'G1')
        game.fire_torpedo('second', 'C1')
        self.assertEqual(game.get_current_state(), 'UNFINISHED')
        self.assertEqual(game.get_num_ships_remaining('first'), 1)
        self.assertEqual(game.get_num_ships_remaining('second'), 1)
        game.fire_torpedo('first', 'H1')   # Sinks Ship
        self.assertFalse(game.fire_torpedo('second', 'C2'))
        self.assertEqual(game.get_current_state(), 'FIRST_WON')


if __name__ == '__main__':
    unittest.main()
