# Function to generate a new nonogramrow
def generatenonogram(inputlength):
    from random import randint

    # Inititate other variables
    lengthcount = 1
    gennonogramrow = []

    # Generate the random row
    while lengthcount <= inputlength:
        gennonogramrow.append(randint(0, 1))
        lengthcount += 1

    return gennonogramrow


# Function to calculate the nonogramrow according to the task
def nonogramfunction(imputnonogramrow):
    # Initiate variables. The list with the results and the integer for the number to insert into the list.
    returnrow = []
    appendvariable = 0

    # Go through the random nonogramrow list item by item
    for num in imputnonogramrow:

        # Add 1 to appendvariable if the number is 1
        if num == 1:
            appendvariable += 1

        # Append appendvariable into the result list if the appendvariable is more than 0, then reset appendvariable.
        else:
            if appendvariable != 0:
                returnrow.append(appendvariable)
            appendvariable = 0

            # Extra run at the end in case the nonogramrow ends with a 1. Check if appendvariable is more than 0 and
            # then append that as well.

    if appendvariable != 0:
        returnrow.append(appendvariable)

    # Return the result
    return returnrow


# - - - Input the length of the nonogramrow here - - -
nonogramrowlength = 500

# Call function to generate a new random nonogramrow
nonogramrow = generatenonogram(nonogramrowlength)

# Call function to process the nonogramrow
resultrow = nonogramfunction(nonogramrow)

# Print the original nonogramrow
print(nonogramrow)

#Print empty row
print("")

# Print the processed result
print(resultrow)
