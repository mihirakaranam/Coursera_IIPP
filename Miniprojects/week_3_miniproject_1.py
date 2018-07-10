# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math
     # initialize global variables used in your code here
num_range=100
remaining_guesses=0
secret_number=0

# helper function to start and restart the game
def new_game():
    global num_range,remaining_guesses,secret_number
    secret_number = random.randrange(0,num_range)
    remaining_guesses = int(math.ceil(math.log(num_range,2)))
    print "New game, Range is from 0 to", num_range
    print "No. of remaining guesses is", remaining_guesses
   
    

    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    global num_range
    num_range=100
    new_game()
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    

def range1000():
    global num_range
    num_range=1000
    new_game()
    # button that changes the range to [0,1000) and starts a new game     
    
    
    
def input_guess(guess):
    global remaining_guesses
    player_guess=int(guess)
    print "Guess is", player_guess
    remaining_guesses=remaining_guesses-1
    print "remaining guesses are:",remaining_guesses
    if remaining_guesses>0:
        if player_guess<secret_number:
            print "Higher"
        elif player_guess>secret_number:
            print "Lower"
        else:
            print "Correct"
            new_game()
    else:
        if player_guess==secret_number:
            print "Correct"
            new_game()
        else:
            print "Guesses completed.The no. is",secret_number
    
    # main game logic goes here	
    
    # remove this when you add your code
    

    
# create frame
frame=simplegui.create_frame("Guess the number",200,200)
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is[0,1000)",range1000,200)
frame.add_input("Guess number:",input_guess,200)
# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
