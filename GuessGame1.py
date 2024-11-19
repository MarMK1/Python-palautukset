#Tehtävä 1

correct_name = "Marius"


guess = input("Guess the name: ")

# Check if the guess is correct
if guess == correct_name:
    print("Congratulations!")
else:
    print("Incorrect guess. Try again!")
    
    
    #Tehtävä 2
    

correct = "Marius"

guess_count = 0

while True:
    guess = input("Guess the name: ")
    
    guess_count += 1
    
    if guess == correct:
        print(f"Congratulations! You guessed the name in {guess_count + 1 } tries.")
        break  
    else:
        print("Incorrect guess. Try again!")



#Tehtävä 3

correct_name = "Marius"

guess_count = 0

while True:

    guess = input("Guess the name: ")
    
    guess_count += 1
    
    if guess == correct_name:
        print(f"Congratulations! You guessed the name in {guess_count} tries.")
        break 
    else:
    
        reveal_letter = correct_name[:guess_count] 
        print(f"Incorrect guess. Here are the first {guess_count} letters of the name: {reveal_letter}")
      
        continue_game = input("Would you like to try again? (y/n): ")
        if continue_game.lower() != 'y':
            print("Thanks for playing!")
            break 
