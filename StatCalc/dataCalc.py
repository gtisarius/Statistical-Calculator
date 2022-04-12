import statistics

# Define the list
oldListOfValues = []

def stat():
    # Convert the old list into floats
    listOfValues = []
    for value in oldListOfValues:
        listOfValues.append(float(value))
    # List values
    print('Your list: ')
    for values in listOfValues:
        print('- ' + str(values))
    amountOfValues = len(listOfValues)
    print('Current amount of values in list: ' + str(amountOfValues))
    chosenAction = input('''You can choose from the following options: 
    - Type any number in to add a value to the list
    - Type rem to remove a value from the list
    - Type cls to clear the list
    - Type calc to calculate statistics
''')
    if chosenAction == 'rem':
        # Remove the latest value in the list
        oldListOfValues.pop(int(amountOfValues - 1))
        stat()
    elif chosenAction == 'cls':
        # Remove all values in the list
        oldListOfValues.clear()
        stat()
    elif chosenAction == 'calc':
        # Use modules to calculate mean, median, minimum and maximum value, range, and standard deviation
        avgValue = statistics.mean(listOfValues)
        medianValue = statistics.median(listOfValues)
        minValue = min(listOfValues)
        maxValue = max(listOfValues)
        rangeOfValues = maxValue - minValue
        standardDeviation = statistics.stdev(listOfValues)
        # Because mode can sometimes give an error when there isn't one in a data set, this determines if a data set does
        try:
            modeValue = statistics.mode(listOfValues)
        except:
            modeCalculated = False
        else:
            modeCalculated = True
        # Prints mean and median
        print('Mean: ' + str(avgValue))
        print('Median: ' + str(medianValue))
        # Prints mode
        if modeCalculated == True:
            print('Mode: ' + str(modeValue))
        else:
            print('Mode: No mode detected')
        # Prints range, standard deviation, and min/max values
        print('Range: ' + str(rangeOfValues))
        print('Standard Deviation: ' + str(standardDeviation))
        print('')
        print('Max Value: ' + str(maxValue))
        print('Min Value: ' + str(minValue))
        print('')
        input('Enter anything to continue: ')
        stat()
    else:
        # Use the input section above to determine what is added to the list
        newItem = chosenAction
        oldListOfValues.append(newItem)
        stat()
stat()