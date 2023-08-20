# test_guess_game.py

# test_guess_game.py

import unittest
from unittest.mock import patch, call
from guess_game import game_loop

class TestGuessGame(unittest.TestCase):

    # ... (other test methods)

    @patch('builtins.input', side_effect=['1234', 'q'])
    @patch('builtins.print')
    @patch('guess_game.generate_random_number', return_value=1234)
    @patch('guess_game.check_guess', side_effect=['OOOO'])
    def test_game_loop(self, mock_check_guess, mock_generate_random_number, mock_print, mock_input):
        game_loop()

        expected_print_calls = [
            call("Enter your guess (or 'q' to quit): "),
            call("Hints: OOOO"),
            call("Enter your guess (or 'q' to quit): "),
            call("Thanks for playing!")
        ]

        actual_print_calls = [call(*args) for args, _ in mock_print.call_args_list]

        self.assertEqual(actual_print_calls, expected_print_calls)
        self.assertEqual(len(actual_print_calls), len(expected_print_calls))

if __name__ == '__main__':
    unittest.main()
