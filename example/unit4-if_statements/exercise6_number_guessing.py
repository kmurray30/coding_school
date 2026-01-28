# Let's put it all together with a simple number guessing game!

# Let's assign a secret number for the user to guess
secret_number = 7

# Ask the user to guess the number.
# Give them hints if they're wrong!

user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == secret_number:
    print("Correct! You win!")
elif user_guess < secret_number:
    print("Too low! The answer was", secret_number)
else:
    print("Too high! The answer was", secret_number)

# Now modify this to not give the number away, but also give more specific hints:
# - Mention if they are too high or too low (like above)
# - If they're within 1 of the answer, say "Very close!"
# - If they're within 3 of the answer, say "Close!"
# - Otherwise, say "Way off!"

# For extra fun, have a friend type in a number and change windows before running the program
#   so you can play your own guessing game!

...



# READ ONLY AFTER RUNNING THIS CODE
# --------------------------------
# Congrats! You've learned if statements! In the next unit, we'll learn about loops
# which will let us repeat code and make even better games.
