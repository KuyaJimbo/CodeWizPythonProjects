import random

# Dictionary to represent card values
card_values = {
    'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10
}
def ask():
    stay = input("Do you want to stay? (Y/N): ")
    while stay not in ["Y", "N"]:
        stay = input("Do you want to stay? (Please choose Y/N): ")

    if stay == "Y":
        return True
    else:
        return False

def deal_card():
    return random.choice(list(card_values.keys()))

def get_player_bet(money):
    while True:
        bet = int(input(f"How much do you want to bet? (1-{money}): "))
        if 1 <= bet <= money:
            break
        else:
            print(f"Please enter a bet between 1 and {money}.")
    return bet

def get_player_guess():
    guess = input("Do you think the next card will be higher or lower? (h/l): ")
    while guess not in ['h', 'l']:
        guess = input("Please enter 'h' for higher or 'l' for lower: ")
    return guess

def final_check(money, target):
    if money >= target:
        print(f"\nYou win with ${money}!")
    elif money == 0:
        print(f"\nYou lose.")
    else:
        print(f"\nYou now have ${money} left.")

def play_higher_lower():
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
        
        # Determine if the guess was correct
        if (guess == 'h' and card_values[next_card] > card_values[current_card]) or \
           (guess == 'l' and card_values[next_card] < card_values[current_card]):
            money += bet
            print(f"Correct! You win ${bet}")
        elif card_values[next_card] == card_values[current_card]:
            print("It's a tie! You keep your bet.")
        else:
            money -= bet
            print(f"Wrong! You lose ${bet}")

        # Casino makes you stop if you go broke or above target
        if money < 0 and money > target:
            break

        # Ask if they would like to stay?
        stay = ask()
        if not stay:
            break    
    
    # Game over
    final_check(money, target)

# Run the game
play_higher_lower()
