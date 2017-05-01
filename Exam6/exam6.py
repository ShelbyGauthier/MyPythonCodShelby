import Epic

weapons = ['Candlestick','Wrench','Pipe']
suspects = ['Miss Scarlet','Col Mustard', 'Mr Green']

#i dont know why my code doesnt let me remove what the user enters from the list
# it keeps crashing

def main():
    answer  = ""
    myList = createList(weapons,suspects)
    printOutcomes(myList,answer)
    
    #while loop will keep going if the length of the list is not equal to 1 or less than 1 i think
    while(len(myList) > 1):
        
        weaponSuspect = Epic.userString("Is the clue about a weapon or a suspect (w or s)?")
        weaponSuspect.lower()
        
        if weaponSuspect == "w":
            answer = Epic.userString("Enter the weapon that was not used (%s):" % weapons)
            #capitalize first letter of each word
            answer.title()
        if weaponSuspect == "s":
            answer = Epic.userString("Enter the innocent suspect (%s)" % suspects)
            answer.title()
        
        myList = createList(weapons,suspects)
        
        printOutcomes(myList,answer)
    
    print "It was %s" % (suspects[0])
    
    print "Good job!"

#remove user input from the list and print out the total outcomes left
def printOutcomes(myList,answer):
      
      print "%s possibilites left" % len(myList)
      myList.remove(answer)  

      return myList


#create the list with weapons and suspects
def createList(weapons, suspects):
    weaponss = []
    suspectts = []
    myList = []
    
    
    for s in suspects:
        for w in weapons:
            myList.append("%s %s" % (s, w))
    
    return myList
    return weaponss
    return suspectts    

main()