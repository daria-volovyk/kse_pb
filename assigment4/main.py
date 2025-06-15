import functions

words = ['apple', 'bread','candy', 'dream','eagle','flame','grape','house','input','joker']

print("Welcome to Wordle!")
print("Guess the word. If letter shows up like [L] - letter is correct and in the right place. \nElse if (l) - letter should be in another place.") #виправлення 5 -letter на 5-letter")

while True:
    secret_word = functions.word_generation(words) 
    tries = 6
    length_of_secret_word = len(secret_word)
    print()
    print(f"Guess the {length_of_secret_word}-letter word. You have {tries} tries.")
    guesses=[]
    while tries!=0:
        guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
        if functions.the_result_of_game(secret_word, guess)==True:
            break
        if functions.checks_of_guess(guess, length_of_secret_word, words, guesses)==True:
            continue
        guesses.append(guess)

        functions.correct_letters(length_of_secret_word, guess, secret_word)   
        tries-=1
    if guess=="stop":
        break
    elif tries==0:
        print("You lose! The word was:", secret_word)
