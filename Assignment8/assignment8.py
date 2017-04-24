import json
import Epic
import urllib2



def readJson(websiteLink):
    #get the url from the apixu website
    
    url = "https://api.apixu.com/v1/current.json?key=7dff8dbe59a5465686504422172404&q=" 
    jsonTxt = urllib2.urlopen(websiteLink).read()
    weatherStuff = json.loads(jsonTxt)
    
    return weatherStuff

def printWeather(weatherStuff):
    
    #print the weather
    
    print "Here is the current weather for %s %s" % (weatherStuff['location']['name'], weatherStuff['location']['region'])
    print "%s degrees(F) and %s" %(weatherStuff['current']['temp_f'],weatherStuff['current']['condition']['text'])
    print "It really feels like %s degrees(F) though" % (weatherStuff['current']['feelslike_f'])
    
    return weatherStuff

    

def main():
    #ask user input and put it in front of the link to get the weather
    user = Epic.userString("Please enter a zip code or city name:")
    weatherStuff = readJson('https://api.apixu.com/v1/current.json?key=7dff8dbe59a5465686504422172404&q=' + user)
    printWeather(weatherStuff)
    repeat = Epic.userString("Want to check another location? (y/n): ")
    
    #keep asking user the same questions if they want to ask for another location again
    if (repeat == "y"):
        user = Epic.userString("Please enter a zip code or city name:")
        weatherStuff = readJson('https://api.apixu.com/v1/current.json?key=7dff8dbe59a5465686504422172404&q=' + user)
        printWeather(weatherStuff)
        repeat = Epic.userString("Want to check another location? (y/n): ")
    
    if (repeat == "n"):
        return False


main()