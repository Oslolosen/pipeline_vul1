import random

def random_greeting():
    greetings = ["Hello", "Hi", "Hey", "Greetings", "Salutations"]
    return random.choice(greetings)

def random_number():
    return random.randint(1, 100)

def main():
    greeting = random_greeting()
    number = random_number()
    print(f"{greeting}! Your random number is: {number}")

main()

