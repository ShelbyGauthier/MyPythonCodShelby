file = open('temps.txt')
temp = []
for line in file:
    words = line.split(" ")
    for word in words:
        temporary = word.replace(",", " ")
        temporary = temporary.replace(".", " ")
        if len(temporary) == 2:
            temp.append(temporary)
        else:
            print word + " " 
            
def calaculateAve(temps, start, stop):
    temps = ['temps.txt']
    return temps 

def getMax(temps):
    start = 0
    for t in temps:
        if t > start:
            start = t
        return start 
        

        
        
    
    
  
    
    
    
    