# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:49:24 2019

@author: Brendan
"""

import collections
from random import choice 

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
        
deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(choice(deck))
print('\n')

#to look at top three cards
print(deck[:3])

#to print just the aces a[start:end:step]
print('\n')
print(deck[12::13])

#print deck implementing __getitem__ 
print('\n')
for card in deck: #or reverse using reversed(deck)
    print(card)
    
print(Card('Q', 'hearts') in deck)


