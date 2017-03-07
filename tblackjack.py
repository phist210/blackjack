from blackjack import *


test_deck = Deck()
player_hand = Player(deck)


DECKVALUES = {'AS': 1, 'AC': 1, 'AD': 1, 'AH': 1, '2S': 2, '2C': 2, '2D': 2, '2H': 2, '3S': 3, '3C': 3, '3D': 3, '3H': 3, '4S': 4, '4C': 4, '4D': 4, '4H': 4, '5S': 5, '5C': 5, '5D': 5, '5H': 5, '6S': 6, '6C': 6, '6D': 6, '6H': 6, '7S': 7, '7C': 7, '7D': 7, '7H': 7, '8S': 8, '8C': 8, '8D': 8, '8H': 8, '9S': 9, '9C': 9, '9D': 9, '9H': 9, 'TS': 10, 'TC': 10, 'TD': 10, 'TH': 10, 'JS': 10, 'JC': 10, 'JD': 10, 'JH': 10, 'QS': 10, 'QC': 10, 'QD': 10, 'QH': 10, 'KS': 10, 'KC': 10, 'KD': 10, 'KH': 10}

DECK = ('AS', 'AC', 'AD', 'AH', '2S', '2C', '2D', '2H', '3S', '3C', '3D', '3H', '4S', '4C', '4D', '4H', '5S', '5C', '5D', '5H', '6S', '6C', '6D', '6H', '7S', '7C', '7D', '7H', '8S', '8C', '8D', '8H', '9S', '9C', '9D', '9H', 'TS', 'TC', 'TD', 'TH', 'JS', 'JC', 'JD', 'JH', 'QS', 'QC', 'QD', 'QH', 'KS', 'KC', 'KD', 'KH')


def test_deck():
    test_deck != DECK
