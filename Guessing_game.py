from random import randint
guessNumber = int(input("Enter your guess number: "))
randomNumber = randint(1,10)
if guessNumber == randomNumber:
    print("You have won")
else:
    print("You have lost")
    print("Random number was:",randomNumber)
________________________________________
Enter your guess number: 4
You have lost
Random number was: 2

[Program finished]
