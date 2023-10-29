import random

while True:
    # Prompt the user to enter a choice between 'rock' 'scissors' and 'paper', and check the input validity
    # The input must be a number and the choice menu must be displayed as a list of propositions

    options = ['rock', 'scissors', 'paper']
    print("Enter a number to choose between the following options:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(options):
                print("Invalid choice. Please enter a number between 1 and", len(options))
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    selected_option = options[choice-1]
    print("You selected", selected_option)

    # Generate a random choice for the computer
    computer_choice = random.choice(options)
    print("The computer selected", computer_choice)

    # Confront the two choices to determine who wins the turn
    if selected_option == computer_choice:
        print("It's a tie!")
    elif selected_option == 'rock' and computer_choice == 'scissors' or \
         selected_option == 'scissors' and computer_choice == 'paper' or \
         selected_option == 'paper' and computer_choice == 'rock':
        print("You win!")
    else:
        print("The computer wins!")
    
    # Ask the user to play again or exit the application
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break

print("Thanks for playing!")
