import Epic
import random 

print "Pick the first card to turn over (1-9):"
num = int(raw_input())  
print "Pick the second card to turn over (1-9):"
num = int(raw_input())  
while num is <1 or num >10:
    print "Pick the first card to turn over (1-9):"
    num = int(raw_input())  
    print "Pick the second card to turn over (1-9):"
    num = int(raw_input())  
    
first = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
second = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']

r = random.randrange(0, 10)
rr = random.randrange(0, 10)
print first[r], second[rr]
