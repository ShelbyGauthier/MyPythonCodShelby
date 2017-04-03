import Epic
import os

def readfiles():
    files = os.listdir('.')
    listoffiles = []
    
    for nameoffile in files:
        if '.txt' in nameoffile:
            listoffiles.append(nameoffile)
            
    return listoffiles
    
def readinfile(nameoffile, userinput):
        numbofwords = 0
        for line in open(nameoffile):
    		
    		listofwords = line.split(" ")
    		for word in listofwords:
    			print "%s %s" %(nameoffile, line)
    			numbofwords = numbofwords + 1
        print numbofwords
        return listofwords
      
       
def main():

	listoffiles = readfiles()
	userinput = Epic.userString("Enter a search term:")
	
	for nameoffile in listoffiles:
		readinfile(nameoffile, userinput)
    
		
main()