from collections import namedtuple

Card = namedtuple('Card',['rank', 'suit'])

class FrenchDeck:

  rank = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [ Card(rank, suit)  for suit in self.suits
                                      for rank in self.rank]
    print(self._cards)

if __name__=="__main__":
  FrenchDeck()