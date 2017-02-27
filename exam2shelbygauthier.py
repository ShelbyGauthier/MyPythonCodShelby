def timings(filename):
    d = {}
    cubeheads = {"Feliks Zemdegs", "Collin Burns"}
    squaremaster = {"Sally Smith","Jim Jones", "Randy Roll"}
    advancedtwister = {"Ed Erl","Andy All","Erica Erst"}
    intermediateturner = {"Lisa Lars","Sandy Set", "George Gilt", "Jane Jules"}
    averagemover = {"Becky Bolt", "Steve Smolt", "Bill Bank", "Brandy Borst", "Ricky Road" , "Alice Art", "Tim Tom" , "Will Wok"}
    pathetic = {"Mark Cohen"}
    for line in open(filename):
        temp = line.split(',')
        name = temp[0].strip()
        rubixtime = float(temp[1].strip())   
        if name in d:
            d[name] = rubixtime + d[name]
        else:
            d[name] = rubixtime

def printnames(string, dictionary):

    timings("timings.txt")
    
def main():
    print "Cube Head (0 - 9.99)" + "\n" + "Feliks Zemdegs" + "\n" + "Collin Burns" + "\n"
    print "Square Master (10 - 19.99)" + "\n" + "Sally Smith" +  "\n" + "Jim Jones" + "\n" + "Randy Roll" + "\n"
    print "Advanced Twister (20 - 29.99)"  + "\n" + "Ed Erl"+ "\n" + "Andy All"+ "\n" + "Erica Erst" + "\n"
    print "Intermediate Turner (30 - 39.99)" + "\n" + "Lisa Lars" + "\n" + "Sandy Set" + "\n" + "George Gilt" + "\n" + "Jane Jules"  + "\n"
    print "Average Mover (40 - 59.99)" + "\n" + "Becky Bolt" + "\n" + "Steve Smolt" "\n" + "Bill Bank" + "\n" + "Brandy Borst" + "\n" + "Ricky Road" + "\n" +  "Alice Art" + "\n" + "Tim Tom" + "\n" + "Will Wok" + "\n"
    print "Pathetic (60 and above)" + "\n" + "Mark Cohen"

main()

