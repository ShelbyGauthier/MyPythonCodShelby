import Epic

ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def BuildDeck():
    return [rank+" of "+suit for rank in ranks for suit in suits]

def shuffle(deck):
    first = deck[:26]
    second = deck[26:]
    shuffle = []

    for i in range(26):
        shuffle.append(first[i])
        shuffle.append(second[i])
    return shuffle
    
def deal(deck):
    hand = deck[:5]
    return hand
    
def main():
    deck = BuildDeck()
    i = 0;
    ShuffleUser = Epic.userInt("How many times do you want to shuffle the deck ")
    while i < ShuffleUser:
        deck = shuffle(deck)
        i += 1
    print deal(deck)
    
main()