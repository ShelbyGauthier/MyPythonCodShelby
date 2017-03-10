import Epic
win = ""
import random     

def eathotdogs():
    Shelby = random.randrange(1, 9)
    Doris =  random.randrange(1, 9)
    Lexi = random.randrange (1, 9)
    ShelbyScore = 0 
    DorisScore = 0
    LexiScore = 0
    keepgoingmore = True
    while keepgoingmore: 
        import time
        time.sleep(1)
        ShelbyScore += Shelby
        DorisScore += Doris
        LexiScore += Lexi
        
        if ShelbyScore >= 50:
            keepgoingmore = False
            win = "Shelby"
            print ""
            print "ShelbyScore: %s" % ShelbyScore
            break
        else:
            print ""
            print "ShelbyScore: %s" % ShelbyScore
             
        if DorisScore >= 50:
            keepgoingmore = False
            win = "Doris"
            print "DorisScore: %s" % DorisScore  
            break
        else:
            print "DorisScore: %s" % DorisScore        

        if LexiScore >= 50:
            keepgoingmore = False
            win = "Lexi"
            print "LexiScore: %s" % LexiScore
            break
        else:
                print "LexiScore: %s" % LexiScore

        
    return win
            
def main():
    msg = Epic.userString("Pick a winner (Shelby, Doris, Lexi): ")
    win = eathotdogs()
    if msg == win:
        print "you guessed right"
    else:
        print "you guessed wrong" 
main()
