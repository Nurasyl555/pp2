from random import randint
number = randint(1, 20)
sum = 0
def Guess_the_number(number, name, sum):
    print("Take a guess.")
    gg = int(input())
    if gg == number:
        print(f"Good job, {name}! You guessed my number in {sum} guesses!")
        return 0
    elif gg < number:
        print("Your guess is too low")
        sum += 1
        Guess_the_number(number, name, sum)
    elif gg > number:
        print("Your guess is too upper")
        sum += 1
        Guess_the_number(number, name, sum)
    
print("Hello! What is your name?")
name = input()
print(name, "Well")
print(name, ", I am thinking of a number between 1 and 20.")
Guess_the_number(number, name, sum)