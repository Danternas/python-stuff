
#Function to set up the deck of 8 decks with all the cards.
def set_deck():
    #set the counter
    i = 0
    
    #8 decks and 4 colurs means 32 cards of each kind
    while i != 32:

        #Make all the cards
        deck.append(["Ace",11,i])
        deck.append(["2",2,i])
        deck.append(["3",3,i])
        deck.append(["4",4,i])
        deck.append(["5",5,i])
        deck.append(["6",6,i])
        deck.append(["7",7,i])
        deck.append(["8",8,i])
        deck.append(["9",9,i])
        deck.append(["10",10,i])
        deck.append(["Jack",10,i])
        deck.append(["Queen",10,i])
        deck.append(["King",10,i])

        #Counter
        i += 1

#Function to give a random card
def set_game(cardsused,houseorplayer):
    #import random
    from random import randint

    #Get the random card. 13 different cards, 4 different colours and 8 decks means 416 cards in total.
    randomcard = randint(0,415-cardsused)

    #Check who gets the card. House gets if true, else player
    if houseorplayer == True:
        #Give the player the random card
        housecards.append(deck[randomcard])
    else:
        #Give the player the random card
        mycards.append(deck[randomcard])

    #Remove the random card from the main deck
    deck.pop(randomcard)

    #Update the counter
    cardsused += 1

    #return the counter
    return cardsused

#Function to show the cards of players hand, or the house. True is house, false is player.
def showcards(houseorplayer):
    #Define variable
    showcards = ""

    if houseorplayer == True:
        #Get and show the cards in housecards.
        for i in housecards:
            showcards += i[0] + " "
        print ("The house's cards are:")
        print (showcards)
    else:
        #Get and show the cards in mycards.
        for i in mycards:
            showcards += i[0] + " "
        print ("Your cards are:")
        print (showcards)

#Function to check results and return if the game should end or not.
def blackjack(houseorplayer):
    #Get and show the cards for the player, or the house
    showcards(houseorplayer)

    #Choose function depending on if it is the player or house
    if houseorplayer == True:
        return checkhouse()
    else:
        return checkplayer()

#Function to check the player's results
def checkhouse():
    #Define variables
    cardvalues = 0
    acefound = False

    #Sum up the values of all the cards in your hand.  Also check for an Ace.
    for n in housecards:
        cardvalues += n[1]
        if n[1] == 11:
            acefound = True

    #Check if blackjack, bust or print the value
    if cardvalues == 21:
        print ("Your value is 21!")
        print ("BLACKJACK!")
        return False, cardvalues
    elif cardvalues <= 21:
        print (f"Your value is: {cardvalues}")
        return True, cardvalues
    elif cardvalues<=31 and acefound:
        print (f"Your value is: {cardvalues-10}")
        return True, cardvalues
    elif cardvalues>31 and acefound:
        print (f"Your value is: {cardvalues-10}")
    else:
        print (f"Your value is: {cardvalues}")
        print ("BUST!")
        return False, cardvalues

#Function to check the house's results
def checkplayer():
    #Define variables
    cardvalues = 0
    acefound = False

    #Sum up the values of all the cards in your hand.  Also check for an Ace.
    for n in mycards:
        cardvalues += n[1]
        if n[1] == 11:
            acefound = True

    #Check if blackjack, bust or print the value
    if cardvalues == 21:
        print ("Your value is 21!")
        print ("BLACKJACK!")
        return False, cardvalues
    elif cardvalues <= 21:
        print (f"Your value is: {cardvalues}")
        return True, cardvalues
    elif cardvalues<=31 and acefound:
        print (f"Your value is: {cardvalues-10}")
        return True, cardvalues
    elif cardvalues>31 and acefound:
        print (f"Your value is: {cardvalues-10}")
        print ("BUST!")
        return False, cardvalues
    else:
        print (f"Your value is: {cardvalues}")
        print ("BUST!")
        return False, cardvalues

#Function to ask if the player want to try again
def play_again_function():
    playerinput = ""

        #Check if the input is 0, 1, or 2.
    while playerinput not in ["Y","N"]:

        #Input the guess
        playerinput = input("Play again? Y/N: ")

        #Correct if input is lower case
        playerinput = playerinput.upper()
    
    print ("- - -")

    #Return
    return (playerinput)

#Function to ask if the player want to hit or stand
def current_game_function(cardsused):
    playerinput = ""

        #Check if the input is 0, 1, or 2.
    while playerinput not in ["H","S"]:

        #Input the guess
        playerinput = input("Hit or Stand? H/S: ")
        
        #Correct if input is lower case
        playerinput = playerinput.upper()

    #Print a line
    print ("- - -")

    #Return H or S
    return playerinput

#Define play_again and current_game
play_again = "Y"

#Run the program while play again is Y
while play_again == "Y":
    #initiate variables
    deck = []
    housecards = []
    mycards = []
    cardsused = 0
    current_session = [True,0]
    temp = [True,0]

    #Sort the deck
    set_deck()

    #Give the house two cards
    cardsused = set_game(cardsused,True)
    cardsused = set_game(cardsused,True)

    #Give the player two cards
    cardsused = set_game(cardsused,False)
    cardsused = set_game(cardsused,False)

    #Show the cards of house
    showcards(True)

    #Reveal result of cards
    current_session[0], _ = blackjack(False)

    #While the blackjack function returns true
    while current_session[0]:

        #Ask if the player want another card
        if current_game_function(cardsused) == "H":
            
            #Give a card to the player
            cardsused = set_game(cardsused,False)

            #Reveal result of cards. Set the session to end depedning on result
            current_session[0], _ = blackjack(False)

        else:
            #Reveal result of cards
            blackjack(False)

            #Set the session to end
            current_session[0] = False
    
    #Check who won

    #Check if the player wants to play again
    play_again = play_again_function()