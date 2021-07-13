from random import shuffle

#Define the cup list
cup_list = [" ","O"," "]

#Function to shuffle cup_list
def cup_shuffle(cup_list):
    
    cup_list = shuffle(cup_list)

    return cup_list

#Function to take the player's guess
def player_guess():

    guess = ""

    #Check if the input is 0, 1, or 2.
    while guess not in ["0","1","2"]:

        #Input the guess
        guess = input("Pick a number: 0, 1, or 2: ")

    #Return
    return int(guess)

#Function to check if the guess is correct
def check_guess(cup_list,guess):
    if cup_list[guess] == "O":
        print ("Correct!")
    else:
        print ("Wrong guess!")
        print ("The answer was:")
        print (cup_list)

#Function to ask if the player want to try again
def play_again_function():
    player_input = ""

        #Check if the input is 0, 1, or 2.
    while player_input not in ["Y","N"]:

        #Input the guess
        player_input = input("Play again? Y/N: ")

        #Correct if input is lower case
        player_input = player_input.upper()
    
    #Return
    return (player_input)

#Define play_again
play_again = "Y"

#Run the program while play again is Y
while play_again == "Y":
    #Run the functions to shuffle the list and then take the player's guess
    cup_shuffle(cup_list)
    myindex = player_guess()

    #Check if the guess is correct and give the answer
    check_guess(cup_list,myindex)

    #Check if the player wants to play again
    play_again = play_again_function()