import random
secret_number = random.randint(1, 10)
user_guess = int(raw_input("Guess a number between 1 and 10!" ))
user_attempts = 1
while user_guess != secret_number and user_attempts < 5:
    print "Nope! Try again!"
    if user_guess < secret_number:
        print "Your guess is too low..."
    else:
        print "Your guess is too high..."
    user_guess = int(raw_input("Try another number!"))
    user_attempts += 1
if user_attempts >= 5:
    print "Too many guesses! You lose! Guesses:", str(user_attempts)
else:
    print "You win! It took you", str(user_attempts), "guesses!"
