# test_guess_game.py

import unittest
from guess_game import generate_random_number
from guess_game import check_guess

class TestGuessGame(unittest.TestCase):

    def test_generate_random_number(self):
        number = generate_random_number()
        self.assertTrue(1000 <= number <= 9999, "Random number should have four digits")
    def test_check_guess(self):
        secret_number = "1234"
        self.assertEqual(check_guess(secret_number, "1234"), "OOOO")
        self.assertEqual(check_guess(secret_number, "1243"), "OOXX")
        self.assertEqual(check_guess(secret_number, "4321"), "XXXX")
        self.assertEqual(check_guess(secret_number, "5678"), "")
if __name__ == '__main__':
    unittest.main()
