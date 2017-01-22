print "How many malcorps did you fint on planet Exlon ?",
Exlon = raw_input()
print "How many malcorps did you find on planet Mobiles ?",
Mobiles = raw_input()
print "how many malcorps did you find on planet Monosantoes ?",
Monosantoes = raw_input()

total = int(Exlon) + int(Mobiles) + int(Monosantoes)
print "You found %s malcorps!" % total
print "The average number of malcorps per planet is %.2f." % (total / 3.0)
