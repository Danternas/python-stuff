def coincounter(amount):
    
    #Define numberofcoins
    numberofcoins = 0
    
    #List for the different coin values. Each item is the value of the coin.
    coins = [500,100,25,10,5,1]

    #For every item in the list:
    for coinvalue in coins:
        #Add the amount of coins at each given value
        numberofcoins = numberofcoins + amount//coinvalue
    
        #Get the rest for the next run of the loop
        amount = amount%coinvalue

    #Return the result when done.
    return numberofcoins

coincounter(155874)












