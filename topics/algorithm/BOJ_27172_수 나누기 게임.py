N=int(input())
cards=[*map(int, input().split())]
scores = {card: 0 for card in cards}
for card in cards: 
    multiple = card*2
    while multiple <= 10**6:
        if multiple in scores: scores[card]+=1; scores[multiple] -= 1
        multiple+=card
for card in cards: print(scores[card])