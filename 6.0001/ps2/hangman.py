# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = ""
    for i in secret_word:
        if i in letters_guessed or i == " ":
            guess += i
        else:
            guess += "_"
    return guess

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = "abcdefghijklmnopqrstuvwxyz"
    available = ""
    for i in letters:
        if i not in letters_guessed:
            available += i
    
    return available

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    print("the secret word is {} letters long".format(len(secret_word)))
    
    letters_guessed = []
    guesses = 10
    warnings = 3
    
    end = False
    
    while not end:
        valid = False
        while not valid and guesses > 0:
            #Display guesses and
            print("you have {} guesses left".format(guesses))
            print("Available letters: " + get_available_letters(letters_guessed),end = "")    
        
            if warnings > 0:  
                #Use lower funciton to check if input is a letter if not it will return an error
                try: 
                    g = str(input("your guess (one letter): ")).lower()
                    #If letter check that is it is valid
                    if g in get_available_letters(letters_guessed) and len(g) == 1:
                        valid = True
                    else:
                        warnings -= 1
                        print("please pick a valid letter, you have {} warnings left".format(warnings))
                except KeyboardInterrupt:
                    raise KeyError()
                except:
                    print("please input a letter, you have {} warnings left".format(warnings))
                    warnings -= 1  
            else: 
                print("you have no warnings left so you lose 1 guess")
                guesses -= 1
                warnings = 3    
            
        #add lower case guess
        letters_guessed.append(g)
        
        if g in secret_word:
            print("good guess: ", end = "")
        else:
            print("Oops! that letter is not in my word: ", end = "")
            if g in "aeiou":
                guesses -= 2
            else:
                guesses -= 1
        
        print(get_guessed_word(secret_word, letters_guessed))
           
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations!, you won")
            end = True
            #Add score
        elif guesses <= 0: #Catches -1 if you guess a vowel
            print("Sorry, you ran out of guesses. the word was " + secret_word)
            end = True
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------f------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #Spaces and stuff interfere with this
    
    #test if same length (maybe a more clever way to do this)
    
    if len(my_word) != len(other_word):
        return False
    
    # for i,x in enumerate(my_word):
    #     if x != "_":
    #         if x != other_word[i] :
    #             return False
    ####Must check against hidden values...
    
    for i,x in enumerate(my_word):
        if x == "_":
            if other_word[i] in my_word:
                return False
        else:
            if x != other_word[i]:
                return False
    return True
        
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for word in wordlist:
        if match_with_gaps(my_word,word):
            print(word + " ",end = "")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("the secret word is {} letters long".format(len(secret_word)))
    
    letters_guessed = []
    guesses = 10
    warnings = 3
    
    end = False
    
    while not end:
        valid = False
        while not valid and guesses > 0:
            #Display guesses and
            print("you have {} guesses left".format(guesses))
            print("Available letters: " + get_available_letters(letters_guessed),end = "")    
        
            if warnings > 0:  
                g = str(input("your guess (one letter): ")).lower()
                #If letter check that is it is valid
                if g in get_available_letters(letters_guessed) or g == "*" and len(g) == 1:
                    valid = True
                elif g in "abcdefghijklmnopqrstuvwxyz*":
                    warnings -= 1
                    print("you have already picked that letter, you have {} warnings left".format(warnings))
                else:
                    warnings -= 1
                    print("please pick a valid letter, you have {} warnings left".format(warnings))
                    
            else: 
                print("you have no warnings left so you lose 1 guess")
                guesses -= 1
                warnings = 3    
            
        #add lower case guess
        letters_guessed.append(g)
        
        if g == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif g in secret_word:
            print("good guess: ", end = "")
        else:
            print("Oops! that letter is not in my word: ", end = "")
            if g in "aeiou":
                guesses -= 2
            else:
                guesses -= 1
        
        print(get_guessed_word(secret_word, letters_guessed))
           
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations!, you won")
            end = True
            #Add score
        elif guesses <= 0: #Catches -1 if you guess a vowel
            print("Sorry, you ran out of guesses. the word was " + secret_word)
            end = True
    

# a = ["h","e","l"]
# print(get_available_letters(a))

# my_word = "hell_"
# other_word = "hello"
# print(match_with_gaps(my_word, other_word))
# show_possible_matches("t__t")

#hangman("hello")
#hangman_with_hints()

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
      # secret_word = choose_word(wordlist)
      # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
