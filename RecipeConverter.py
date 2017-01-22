#Shelby Gauthier
print "--Original Recipe--"

print "Enter the amount of flour (cups):", 
flour = raw_input() 

print "Enter the amount of water (cups):", 
water = raw_input()

print "Enter the amount of salt (teaspoons)", 
salt = raw_input()

print "Enter the amount of yeast (teaspoons)", 
yeast = raw_input()

print "Enter the loaf adjustment factor (e.g. 2.0 double the size):",
factor = raw_input()

print "--Modified Recipe--"
print "flour: %.2f" % (int(flour) * (int(factor))), 
print "cups"
print "water: %.2f" % (int(water) * (int(factor))), 
print "cups"
print "salt: %.2f" % (int(salt) * (int(factor))), 
print "teaspoons"
print "yeast: %.2f" % (int(yeast) * (int(factor))),
print "teaspoons"

