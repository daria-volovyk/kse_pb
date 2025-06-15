import random
def word_generation(list_of_words):
    return(random.choice(list_of_words))

def checks_of_guess(guess, length_of_word, words, guesses):
    if len(guess)!=length_of_word:
        print("Wrong length. Expected", length_of_word, "letters")
        return True
    if not guess.isalpha():
        print("The word consists only of letters")
        return True
    if guess not in words:
        print("The list doesn`t contain this word")
        return True
    if guess in guesses:
        print("You already tried this one")
        return True
            
def the_result_of_game(secret_word, guess):
    if(secret_word==guess):
        print("You win!!!")
        return True
    if(guess=="stop"):
        print("The end of the game")
        return True
def correct_letters(length_of_secret_word, guess, secret_word):
    result=[]; i=0
    while i<length_of_secret_word :
        letter = guess[i]
        if letter==secret_word[i]:
            result.append("["+letter.upper()+"]")
        elif letter in secret_word:
            result.append("("+letter+")")
        else:
            result.append(" "+letter+" ")
        i+=1
    print("Result:", ' '.join(result))
    
    
    