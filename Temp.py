def ReadTemps():     
    file = open('temps.txt')
    temps = []
    for line in file: 
        num = float(line)
        temps.append(num)
    return temps
            
def calculateAve(temps, start, stop):
    index = 1
    total = 0 
    mean = 0
    for num in temps:
        if index >= start and index <= stop:
            total = num + total 
        index = index + 1
    mean = total/(stop-start)
    return mean 
    
def count(temps, start, stop):
    index = 1
    total = 0
    for num in temps:
        if index >= start and index <= stop and num > 0:
            total = total + 1
        index = index + 1
    return total 
        
def main():
    temps = ReadTemps()
    print "During the first 81 years, the average deviation from the temperature anomoly is %s" % (calculateAve(temps, 0, 81)) 
    print "During the first 81 years, %s had a positive temperature anomoly" % (count(temps, 0, 81))
    print "During the last 35 years, the average deviation from the temperature anomoly is %s" % (calculateAve(temps, 82, 117))
    print "During the last 35 years, %s had a positivie temperature anomolu" % (count(temps, 82, 117))
    
main()  
    
    
    
    


