# Author: Freddie Main III
# GitHub Username: FMain89
# Date: 2/23/2022
# Description: This is my tester file for the Ship Game file

import unittest
from ShipGame import ShipGame


class ShipGameTester(unittest.TestCase):
    """
    Description:
            This class will hold all the unit tests for the ship game.
    """

    def test_1(self):
        """
        Description:
                Test of the place_ship method, correct use.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        self.assertIs(t1, True)
        t2 = game.place_ship('first', 2, 'I8', 'R')
        self.assertIs(t2, True)
        t3 = game.place_ship('second', 3, 'H2', 'C')
        self.assertIs(t3, True)
        t4 = game.place_ship('second', 2, 'A1', 'C')
        self.assertIs(t4, True)
        t5 = game.place_ship('first', 5, 'A2', 'C')
        self.assertIs(t5, False)

    def test_2(self):
        """
        Description:
                Test of the place_ship method, place on a border horizontal.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'H2', 'C')
        self.assertIs(t1, False)

    def test_3(self):
        """
        Description:
                Test of the place_ship method, place on a vertical boarder.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'J8', 'R')
        self.assertIs(t1, False)

    def test_4(self):
        """
        Description:
                Test of the place_ship method, place ships on top of one another
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'C1', 'R')
        self.assertIs(t2, False)

    def test_5(self):
        """
        Description:
                Test of the place_ship method, ship doesn't fit on the grid

        """
        game = ShipGame()
        t1 = game.place_ship('first', 11, 'B2', 'C')
        self.assertIs(t1, False)

    def test_6(self):
        """
        Description:
                Test of the place_ship method, a ship size of less than 2.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 1, 'B2', 'C')
        self.assertIs(t1, False)
        t2 = game.place_ship('first', 0, 'B2', 'C')
        self.assertIs(t2, False)
        t3 = game.place_ship('first', -1, 'B2', 'C')
        self.assertIs(t3, False)

    def test_7(self):
        """
        Description:
                Test of the get current state, state: FIRST_WON

        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        game.set_current_state()
        self.assertEqual(game.get_current_state(), "FIRST_WON")

    def test_8(self):
        """
        Description:
                Test of the get current state, state: SECOND_WON

        """
        game = ShipGame()
        t1 = game.place_ship('second', 5, 'B2', 'C')
        game.set_current_state()
        self.assertEqual(game.get_current_state(), "SECOND_WON")

    def test_9(self):
        """
        Description:
                Test of the get current state, state: UNFINISHED

        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        self.assertEqual(game.get_current_state(), "UNFINISHED")

    def test_10(self):
        """
        Description:
                Test fire torpedo, hit.
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        f1 = game.fire_torpedo('first', 'H2')
        self.assertIs(f1, True)

    def test_11(self):
        """
        Description:
                Test fire torpedo, miss.
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        f1 = game.fire_torpedo('first', 'H4')
        self.assertIs(f1, True)

    def test_12(self):
        """
        Description:
                Test fire torpedo, hit in same spot

        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        f1 = game.fire_torpedo('first', 'H2')
        self.assertIs(f1, True)
        f2 = game.fire_torpedo('second', 'B2')
        self.assertIs(f2, True)
        f3 = game.fire_torpedo('first', 'H2')
        self.assertIs(f3, True)

    def test_13(self):
        """
        Description:
                Test fire torpedo, miss in the same spot
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        f1 = game.fire_torpedo('first', 'H4')
        self.assertIs(f1, True)
        f2 = game.fire_torpedo('second', 'I8')
        self.assertIs(f2, True)
        f3 = game.fire_torpedo('first', 'H4')
        self.assertIs(f3, True)

    def test_14(self):
        """
        Description:
                Test fire torpedo, on a sunk ship
        """
        game = ShipGame()
        t1 = game.place_ship('first', 2, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        f1 = game.fire_torpedo('first', 'I8')
        self.assertIs(f1, True)
        f2 = game.fire_torpedo('second', 'B2')
        self.assertIs(f2, True)
        f3 = game.fire_torpedo('first', 'I9')
        self.assertIs(f3, True)
        f4 = game.fire_torpedo('second', 'C2')
        self.assertIs(f4, True)
        s1 = game.get_num_ships_remaining('first')
        self.assertEqual(s1, 1)
        f5 = game.fire_torpedo('first', 'I10')
        self.assertIs(f5, True)
        f6 = game.fire_torpedo('second', 'C2')
        self.assertIs(f6, True)

    def test_15(self):
        """
        Description:
                test player one get num ships remaining
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        s1 = game.get_num_ships_remaining('first')
        self.assertEqual(s1, 2)

    def test_16(self):
        """
        Description:
                test player two get num ships remaining
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        s1 = game.get_num_ships_remaining('second')
        self.assertEqual(s1, 2)

    def test_17(self):
        """
        Description:
                Test NEG length of ship during place_ship
        """
        game = ShipGame()
        t1 = game.place_ship('first', -5, 'B2', 'C')
        self.assertIs(t1, False)

    def test_18(self):
        """
        Description:
                Test invalid fire coordinates
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        f1 = game.fire_torpedo('first', 'K2')
        f2 = game.fire_torpedo('first', 'a15')
        self.assertIs(f1, False)
        self.assertIs(f2, False)

    def test_19(self):
        """
        Description:
                Test lower case coordinates
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'b2', 'C')
        t2 = game.place_ship('first', 2, 'i8', 'R')
        t3 = game.place_ship('second', 3, 'h2', 'C')
        t4 = game.place_ship('second', 2, 'a1', 'C')
        self.assertIs(t1, True)
        self.assertIs(t2, True)
        self.assertIs(t3, True)
        self.assertIs(t4, True)

    def test_20(self):
        """
        Description:
                Fire order needs to be maintained.
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        t2 = game.place_ship('first', 2, 'I8', 'R')
        t3 = game.place_ship('second', 3, 'H2', 'C')
        t4 = game.place_ship('second', 2, 'A1', 'C')
        f1 = game.fire_torpedo('first', 'H2')
        self.assertIs(f1, True)
        f2 = game.fire_torpedo('first', 'E2')
        self.assertIs(f2, False)

    def test_21(self):
        """
        Description:
                Test to see what happens if you fire torpedo then try and place a ship. You can assume ships won't be
                placed after fire torpedo has been called.
        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')
        f1 = game.fire_torpedo('first', 'H2')
        self.assertIs(f1, True)
        t2 = game.place_ship('first', 2, 'I8', 'R')
        self.assertIs(t2, True)

    def test_22(self):
        """
        Description:
                Full game where player one wins.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 2, 'B2', 'C')
        t2 = game.place_ship('second', 2, 'D3', 'R')
        f1 = game.fire_torpedo('first', 'D3')
        f2 = game.fire_torpedo('second', 'A3')
        f3 = game.fire_torpedo('first', 'D4')
        g1 = game.get_current_state()
        self.assertEqual(g1, 'FIRST_WON')

    def test_23(self):
        """
        Description:
                Full game where player two wins.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 2, 'B2', 'C')
        t2 = game.place_ship('second', 2, 'D3', 'R')
        f1 = game.fire_torpedo('first', 'D8')
        f2 = game.fire_torpedo('second', 'B2')
        f3 = game.fire_torpedo('first', 'D9')
        f4 = game.fire_torpedo('second', 'C2')
        g1 = game.get_current_state()
        self.assertEqual(g1, 'SECOND_WON')

    def test_24(self):
        """
        Description:
                Test a fire after winning has been met.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 2, 'B2', 'C')
        t2 = game.place_ship('second', 2, 'D3', 'R')
        f1 = game.fire_torpedo('first', 'D3')
        f2 = game.fire_torpedo('second', 'A3')
        f3 = game.fire_torpedo('first', 'D4')
        g1 = game.get_current_state()
        self.assertEqual(g1, 'FIRST_WON')
        f4 = game.fire_torpedo('second', 'A1')
        self.assertIs(f4, False)

    def test_25(self):
        """
        Description:
                Test a fire after winning has been met.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 2, 'B2', 'C')
        t2 = game.place_ship('second', 2, 'D3', 'R')
        f1 = game.fire_torpedo('first', 'D8')
        f2 = game.fire_torpedo('second', 'B2')
        f3 = game.fire_torpedo('first', 'D9')
        f4 = game.fire_torpedo('second', 'C2')
        g1 = game.get_current_state()
        self.assertEqual(g1, 'SECOND_WON')
        f5 = game.fire_torpedo('first', 'A1')
        self.assertIs(f5, False)

    def test_26(self):
        """
        Description:
               Longer game, player one winning.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')  # B2, C2, D2, E2, F2
        t2 = game.place_ship('first', 2, 'I8', 'R')  # I8, I9
        t3 = game.place_ship('second', 3, 'H2', 'C')  # H2, I2, J2
        t4 = game.place_ship('second', 2, 'A1', 'C')  # A1, B1
        f1 = game.fire_torpedo('first', 'H2')
        f2 = game.fire_torpedo('second', 'I8')
        f3 = game.fire_torpedo('first', 'I2')
        f4 = game.fire_torpedo('second', 'I9')  # Sinks a ship
        g1 = game.get_current_state()  # Unfinished
        s1 = game.get_num_ships_remaining('first')  # One left
        s2 = game.get_num_ships_remaining('second')  # Two left
        self.assertEqual(g1, 'UNFINISHED')
        self.assertEqual(s1, 1)
        self.assertEqual(s2, 2)
        f5 = game.fire_torpedo('first', 'J2')  # Sinks a ship
        s3 = game.get_num_ships_remaining('second')  # One left
        g2 = game.get_current_state()  # Unfinished
        self.assertEqual(s3, 1)
        f6 = game.fire_torpedo('second', 'A1')
        f7 = game.fire_torpedo('first', 'A1')
        f8 = game.fire_torpedo('second', 'B2')
        f9 = game.fire_torpedo('first', 'B1')  # Sinks a ship.
        g3 = game.get_current_state()  # Player one wins
        s4 = game.get_num_ships_remaining('first')  # One Left
        s5 = game.get_num_ships_remaining('second')  # 0 left
        self.assertEqual(g3, 'FIRST_WON')
        self.assertEqual(s4, 1)
        self.assertEqual(s5, 0)

    def test_27(self):
        """
        Description:
               Longer game, player one winning.

        """
        game = ShipGame()
        t1 = game.place_ship('first', 5, 'B2', 'C')  # B2, C2, D2, E2, F2
        t2 = game.place_ship('first', 2, 'I8', 'R')  # I8, I9
        t3 = game.place_ship('second', 3, 'H2', 'C')  # H2, I2, J2
        t4 = game.place_ship('second', 2, 'A1', 'C')  # A1, B1
        f1 = game.fire_torpedo('first', 'H2')
        f2 = game.fire_torpedo('second', 'I8')
        f3 = game.fire_torpedo('first', 'I2')
        f4 = game.fire_torpedo('second', 'I9')  # Sinks a ship
        g1 = game.get_current_state()  # Unfinished
        s1 = game.get_num_ships_remaining('first')  # One left
        s2 = game.get_num_ships_remaining('second')  # Two left
        self.assertEqual(g1, 'UNFINISHED')
        self.assertEqual(s1, 1)
        self.assertEqual(s2, 2)
        f5 = game.fire_torpedo('first', 'J2')  # Sinks a ship
        s3 = game.get_num_ships_remaining('second')  # One left
        g2 = game.get_current_state()  # Unfinished
        self.assertEqual(s3, 1)
        f6 = game.fire_torpedo('second', 'B2')
        f7 = game.fire_torpedo('first', 'D1')
        f8 = game.fire_torpedo('second', 'C2')
        f9 = game.fire_torpedo('first', 'E9')
        f10 = game.fire_torpedo('second', 'D2')
        f11 = game.fire_torpedo('first', 'G4')
        f12 = game.fire_torpedo('second', 'F2')
        f13 = game.fire_torpedo('first', 'A1')
        f14 = game.fire_torpedo('second', 'E2')  # Sinks Ship
        g3 = game.get_current_state()  # Player two wins
        s4 = game.get_num_ships_remaining('first')  # Zero Left
        s5 = game.get_num_ships_remaining('second')  # 1 left
        self.assertEqual(g3, 'SECOND_WON')
        self.assertEqual(s4, 0)
        self.assertEqual(s5, 1)


if __name__ == '__main__':
    unittest.main()
