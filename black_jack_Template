import random

# Dictionary to represent card values
card_values = {
    'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10
}

def ask():
    """
    Ask the player if they want to continue playing.
    
    Returns:
    bool: True if the player wants to stay, False if they want to quit.
    """
    pass

def deal_card():
    """
    Randomly select and return a card from the card_values dictionary.
    
    Returns:
    str: The name of the randomly selected card.
    """
    pass

def get_player_bet(money):
    """
    Get the player's bet amount.
    
    Args:
    money (int): The current amount of money the player has.
    
    Returns:
    int: The amount the player wants to bet.
    """
    pass

def get_player_guess():
    """
    Get the player's guess for whether the next card will be higher or lower.
    
    Returns:
    str: 'h' for higher or 'l' for lower.
    """
    pass

def final_check(money, target):
    """
    Check the final state of the game and print the appropriate message.
    
    Args:
    money (int): The final amount of money the player has.
    target (int): The target amount to win the game.
    """
    pass

def play_higher_lower():
    """
    Main game function that runs the Higher or Lower game.
    """
    money = 100
    target = 10000
    
    print("Welcome to Higher or Lower!")
    print(f"You start with ${money}. Your goal is to reach ${target}.")
    
    while True:
        print(f"\nYou have ${money}")
        
        # Deal the first card
        current_card = deal_card()
        print(f"The current card is: {current_card}")
        
        # Get player's bet
        bet = get_player_bet(money)
        
        # Get player's guess
        guess = get_player_guess()
        
        # Deal the next card
        next_card = deal_card()
        print(f"The next card is: {next_card}")
        
        # Determine if the guess was correct by comparing current_card and next_card
        # make sure you add and subtract from the total money if you win or lose
        
        # Casino makes you stop if you go broke or above target
        if money <= 0 or money >= target:
            break
        
        # Ask if they would like to stay
        if not ask():
            break    
    
    # Game over
    final_check(money, target)

# Run the game
play_higher_lower()
