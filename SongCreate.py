import Epic


firstverse = Epic.userString("Enter the first verse:")
secondverse = Epic.userString("Enter the second verse:")
thirdverse = Epic.userString("Enter the third verse:")
fourthverse = Epic.userString("Enter the fourth verse")
Chorus = Epic.userString("Enter the chorus")
ChorusRepeat = Epic.userInt("Enter the chorus repeat total")

ChorusPlusOne = (ChorusRepeat + 1) 

Lines = [ ]

print "  "

Lines.append(firstverse)
Lines.append(Chorus * ChorusRepeat)
Lines.append(secondverse)
Lines.append(Chorus * ChorusRepeat)
Lines.append(thirdverse)
Lines.append(Chorus * ChorusRepeat)
Lines.append(fourthverse)
Lines.append(Chorus * ChorusRepeat + Chorus)

Lines = Lines*2
Lines.insert (8, "One More Time")

print Lines
print "         "
print "         "
for x in Lines: 
    print (x) 
    
#Shelby Gauthier