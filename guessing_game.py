"""
GUESSING GAME APPLICATION
=========================

This is a simple number guessing game where the player tries to guess
a randomly generated number between 1 and 5.

Author: Python Developer
Version: 1.0
Date: 2024
"""

import random
from datetime import datetime


class GuessingGame:
    """
    A class representing the Guessing Game functionality.
    
    This class handles the core game logic including number generation,
    user input validation, and game statistics tracking.
    """
    
    def __init__(self):
        """
        Initialize the GuessingGame with default values.
        
        Attributes:
            min_range (int): Minimum number in guessing range (1)
            max_range (int): Maximum number in guessing range (5)
            total_games (int): Counter for total games played
            wins (int): Counter for successful guesses
        """
        self.min_range = 1
        self.max_range = 5
        self.total_games = 0
        self.wins = 0
    
    def generate_random_number(self):
        """
        Generate a random number within the specified range.
        
        Returns:
            int: A random integer between min_range and max_range (inclusive)
        """
        return random.randint(self.min_range, self.max_range)
    
    def get_user_guess(self):
        """
        Prompt user for input and validate the guess.
        
        This method handles user input, validates that it's an integer
        within the acceptable range, and provides error messages for
        invalid inputs.
        
        Returns:
            int: Validated user guess between 1 and 5
        """
        while True:
            try:
                guess = int(input(f"Enter your guess ({self.min_range}-{self.max_range}): "))
                if self.min_range <= guess <= self.max_range:
                    return guess
                else:
                    print(f"Enter a number between {self.min_range} and {self.max_range}.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def check_guess(self, user_guess, secret_number):
        """
        Compare user's guess with the secret number.
        
        Args:
            user_guess (int): The number guessed by the user
            secret_number (int): The randomly generated target number
            
        Returns:
            bool: True if guess is correct, False otherwise
        """
        return user_guess == secret_number
    
    def play_round(self):
        """
        Execute a single round of the guessing game.
        
        This method orchestrates a complete game round including:
        - Number generation
        - User input collection
        - Guess validation
        - Result reporting
        """
        print("\n" + "="*40)
        print("NEW GAME ROUND")
        print("="*40)
        
        # Generate secret number
        secret_number = self.generate_random_number()
        print(f"Secret number generated! (It's between {self.min_range} and {self.max_range})")
        
        # Get user guess
        user_guess = self.get_user_guess()
        
        # Check result
        if self.check_guess(user_guess, secret_number):
            print(f"You win!")
            self.wins += 1
        else:
            print(f"You loose! The number was {secret_number}. Better luck next time!")
        
        self.total_games += 1
    
    def display_statistics(self):
        """
        Display game statistics to the user.
        
        Shows total games played, wins, losses, and win percentage.
        """
        print("\n" + "="*40)
        print("GAME STATISTICS")
        print("="*40)
        print(f"Total games played: {self.total_games}")
        print(f"Games won: {self.wins}")
        print(f"Games lost: {self.total_games - self.wins}")
        
        if self.total_games > 0:
            win_percentage = (self.wins / self.total_games) * 100
            print(f"Win percentage: {win_percentage:.1f}%")
        else:
            print("Win percentage: 0%")
    
    def show_menu(self):
        """
        Display the main game menu and handle user choices.
        
        Provides options to play a new game, view statistics, or exit.
        """
        while True:
            print("\n" + "="*40)
            print("GUESSING GAME MENU")
            print("="*40)
            print("1. New game")
            print("2. View statistics")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                self.play_round()
            elif choice == '2':
                self.display_statistics()
            elif choice == '3':
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")


def main():
    """
    Main function to initialize and run the guessing game.
    
    This function serves as the entry point for the application.
    It creates a game instance and starts the menu system.
    """
    print("Welcome to the Guessing Game!")
    print("Try to guess the secret number between 1 and 5!")
    
    game = GuessingGame()
    game.show_menu()


if __name__ == "__main__":
    # Application entry point
    main()