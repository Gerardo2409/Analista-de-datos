def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
        '''
    ]
    return stages[tries]

def hangman():
    word = "hangman"
    guessed_letters = []
    tries = 6
    
    print("Welcome to Hangman!")
    
    while True:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(display_hangman(tries))
        print(display_word)
        
        if display_word == word:
            print("Congratulations! You guessed the word.")
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess not in word:
                tries -= 1
                print(f"Wrong guess! You have {tries} tries left.")
                if tries == 0:
                    print("Sorry, you're out of tries. The word was", word)
                    break

hangman()