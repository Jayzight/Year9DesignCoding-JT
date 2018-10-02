play = 0
num = -1

while play == 0:

    print("Welcome to Hangman!")

    answer = ""

    print("")
    print("You have 8 attempts to guess the word.")
    choice = input("Would you like the computer to choose a word [1] or for you to input one [2]?:")
    import random
    words = ['GOHAR','FARIN','SHANE','NARUTO','JAYSON','DEVIN','BASKETBALL','LEBRON','KAGEYAMA','SASUKE',
             'ATAIM']
    answer = random.choice(words)
    #answer = input("Word:")
    tempo = ""
    guess = ""
    inguess = ""
    final = "---------------------------------"
    wrong = ""
    point = 0
    lives = 8

    #checking if the user has guessed all words or not
    while point < len(answer):
        #checking if the user still have lives
        if lives > 0:

            #setting variables repeated to "0"
            num = -1
            incorrect = 0
            double = 0
            
            print (" ")
            guess = input("Guess a letter:")

            #going through answer string, comparing with guessed letter
            
            for letter in answer:
                num = num + 1
                #If the guess is equal to the letter, add a number to the num
                if guess == letter:
                    tempo = tempo + guess
                    double = double + 1
                if guess is not letter:
                    incorrect = incorrect + 1
                    tempo = tempo + final[num]                   
            point = point + double
            #making final results
            final = tempo
            tempo = ""
            print(" ")
            print ("           ", final)
            print(" ")

            #checking if nothing is incorrect
            if incorrect == len(answer):
                wrong = wrong + guess + ","
                lives = lives - 1

            #printing lives left and incorrect guesses
            print ("Incorrect Guesses: ", wrong)
            print ("Lives Left: ", lives)
        #if user doesn't have any lives left
        else:
            point = len(answer) + 1
            print(" ")
            print("You ran out of lives! The answer was:", answer)

    print ("")
    print ("Good Job! You guessed it right! You Win!")
    print ("")
    play = int(input("Would you like to play again? YES [0] NO [1]:"))
else:
    exit

