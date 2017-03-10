#If the temperature is between 60 and 70 degrees
#Then turn on the heater!
#If the temperature is above 80 degrees...
#Then turn on the air conditioner!
    

print "What is the temp?"
temperature = int(raw_input())

print "What is the day"
day = raw_input()

if (temperature > 60 and temperature < 70) or day == "Sunday":
    print "turn on the heater"
else:
    print "The temp is fine"
    
    

