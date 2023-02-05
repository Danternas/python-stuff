
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
    if houseorplayer == True: #True is house. False is player.
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

#Function to check any results
def checkcards(cardstocheck):
    #Define variables
    cardvalues = 0
    acefound = False

    #Sum up the values of all the cards in your hand.  Also check for an Ace.
    for n in cardstocheck:
        cardvalues += n[1]
        if n[1] == 11:
            acefound = True

    if cardvalues>21 and acefound:
        cardvalues = cardvalues-10

    return cardvalues

#Function to show the cards of player's or house's hand. True is house, false is player.
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

#Function to print card results, player or house
def printcardresults(houseorplayer): #True is house. False is player.

    #Show cards
    showcards(houseorplayer)

    #Check if blackjack, bust or print the value
    #House
    if houseorplayer == True: #True is house. False is player.
        
        #Get the value of house's cards
        cardvalues = checkcards(housecards)

        #Display blackjack rule outcome
        if cardvalues == 21:
            print ("House value is 21!")
            print ("HOUSE BLACKJACK!")
        elif cardvalues <= 21:
            print (f"House value is: {cardvalues}")
        else:
            print (f"House value is: {cardvalues}")
            print ("HOUSE IS BUST!")

    #Player
    else:

        #Get the value of player's cards
        cardvalues = checkcards(mycards)

        #Display blackjack rule outcome
        if cardvalues == 21:
            print ("Your value is 21!")
            print ("BLACKJACK!")
        elif cardvalues <= 21:
            print (f"Your value is: {cardvalues}")
        else:
            print (f"Your value is: {cardvalues}")
            print ("BUST!")

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

#Define play_again
play_again = "Y"

#Run the game while play_again is Y
while play_again == "Y":
    #initiate variables
    deck = []
    housecards = []
    mycards = []
    cardsused = 0
    current_session = True
    temp = [True,0]
    housefinalvalue = [True,0]
    playerfinalvalue = [True,0]

    #Sort the deck
    set_deck()

    #Give the house two cards
    cardsused = set_game(cardsused,True)
    cardsused = set_game(cardsused,True)

    #Give the player two cards
    cardsused = set_game(cardsused,False)
    cardsused = set_game(cardsused,False)

    #Show the cards of house and player
    printcardresults(True)
    printcardresults(False)

    #While the blackjack function returns true
    while current_session:

        #Ask if the player want another card
        if current_game_function(cardsused) == "H":
            
            #Give a card to the player
            cardsused = set_game(cardsused,False)

            #Get and show the cards for the player
            printcardresults(False) #True is house. False is player.

            #Spacer
            print ("- - -")

            #21 or over means either blackjack or bust, so end the game.
            if checkcards(mycards) >= 21:
                printcardresults(False)
                current_session = False

        #If they don't then process who wins
        else:
            #Get and show the cards for the house
            printcardresults(True) #True is house. False is player.

            #Spacer
            print ("- - -")

            #Get and show the cards for the player
            printcardresults(False) #True is house. False is player.

            #Spacer
            print ("- - -")

            #Check who won
            if checkcards(mycards) > checkcards(housecards):
                print ("You win!")
            else:
                print ("House wins!")

            #Set the session to end
            current_session = False
    
    #Check if the player wants to play again
    play_again = play_again_function()