# ------------------------------------------------------
# reads the speeds in the specified file (filename)
# and returns them as a list of integers
# ------------------------------------------------------
def readData(filename):
    file = open(filename)
    speedlimit = []
    for line in file: 
        num = int(line)
        speedlimit.append(num)
      
    return speedlimit

# ------------------------------------------------------    
# calculates and returns the average of the numbers
# in the the specified list (l)
# ------------------------------------------------------

def getAverage(speedlimit):
    average = 0.0
    average = sum(speedlimit)/float(len(speedlimit))
    return average


# ------------------------------------------------------
# counts and returns the number of values in the 
# specified list (l) that are greater than or 
# equal to maxSpeed
# ------------------------------------------------------
def countSpeeders(speedlimit, maxSpeed):
    maxspeed = 69
    count = 0
    for num in speedlimit:
        if num > maxspeed:
            count = count + 1
    return count 
    
            
# ------------------------------------------------------
# Determines the number of people speeding during 
# rush hour and not during rush hour.  Also determines
# the total fines during rush hour and not during 
# rush hour.  A person is considered speeding if they
# are traveling faster than 69 MPH.  The fine for 
# speeding during rush hour is $150.  The fine for 
# speeding not during rush hour is $100.
#
# THE CORRECT OUTPUT IS:
#
# The average speed during rush hour was 63.47.
# The average speed not during rush hour was 64.07.
# There were 4 speeders during rush hour.  Total fine = $600
# There were 6 speeders not during rush hour.  Total fine = $600
# ------------------------------------------------------
def main():
    speedlimit = readData("data-rush.txt")
    rushhour = getAverage(speedlimit)
    rushspeeders = countSpeeders(speedlimit, 69)
    speedlimit = readData("data-not-rush.txt")
    nrushhour = getAverage(speedlimit)
    nrushspeeders = countSpeeders(speedlimit, 69)

    nrushhourfine = nrushspeeders * 100
    rushhourfine = rushspeeders * 150
    
    print "The average speed during rush hour was %s" % rushhour
    print "The average speed not during rush hour was %s" % nrushhour
    print "There were %s speeders during rush hour.  Total fine = $600" % rushspeeders
    print "There were %s speeders not during rush hour.  Total fine = $600" % nrushspeeders    
    

# ------------------------------------------------------
# kick off the program by calling main
# ------------------------------------h-----------------
main()