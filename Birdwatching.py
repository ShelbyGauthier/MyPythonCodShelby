import Epic

def countBirds(filename):
    d = {}
    for line in open(filename):
        temp = line.split(',')
        birdname = temp[0].strip()
        birdcount = int(temp[1].strip())    
        # I had to go back and fix because it was producing a string 
        if birdname in d:
            d[birdname] = birdcount + d[birdname]
        else:
            d[birdname] = birdcount 
            
    return d 
            
def askUser(d):
    e = Epic.userString("Please enter a bird name:")     
    
    #using from epic.py 
    
    print "I have seen that bird %s time(s)." % d[e]

def main():
    d = countBirds("Birds.txt")
    askUser(d)
    
main()      
        
    
    
    
    