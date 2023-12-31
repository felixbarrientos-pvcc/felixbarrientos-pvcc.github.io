# Name: Felix Barrientos
# Program Purpose: This program is magic ;0
# 8 Ball

import random
answers_8_ball = ("As I see it, Yes", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", 
"It is certain", "It is decidedly so", "Most likely", "My reply is No", "My sources say no", "Outlook good", "Outlook not so good",
"Reply hazy, try again", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes", "Definitely", "No")

def main():

    print("I am the MAGIC-8 BALL and can answer any YES or NO question")

    another_question = True
    while another_question:
        answer = random.choice(answers_8_ball)

        print("\nShake the MAGIC-8 BALL")
        print("....and now....")
        question = input("\nWhat is your YES or NO question?")
        print("The MAGIC-8 ball says... " + answer)

        askAgain = input("\nWould you like to ask me another question? (Y/N): ")
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

        print("\nCome back again when you have other important questions!")
        print("\n...Magic-8 Ball, out.")

main ()