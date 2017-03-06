from itertools import product
import random
import os
import time


SUIT = 'SCDH'
RANK = 'A23456789TJQK'
DECK = tuple(''.join(card) for card in product(RANK, SUIT))
"""Creates the deck (a set) by joining all possibilities of RANK, SUIT pairs.
"""
DECKVAL = {card: min(1 + RANK.index(card[0]), 10) for card in DECK}
"""Creates a dictionary of "Cards" as keys and their respective values as values
"""


def clear():
    os.system('clear')


class OutOfCards(Exception):
    pass


class Deck:
    """A shuffled deck of cards."""
    def __init__(self):
        self.cards = random.sample(DECK, len(DECK))

    def draw(self):
        """Draw one card from the deck and return it.
        Raise OutOfCards if the deck is out of cards.

        """
        if self.cards:
            return self.cards.pop()
        else:
            raise OutOfCards()


class Player:
    """A hand of cards in blackjack."""
    def __init__(self, DECK):
        self.cards = []
        for i in range(2):
            self.draw(DECK)

    def __str__(self):
        return ' '.join(self.cards)

    def draw(self, deck):
        """Draw one card from deck. Return the new card."""
        card = deck.draw()
        self.cards.append(card)
        return card

    @property
    def soft_value(self):
        """The "soft" value of the cards in the hand (counting aces as 1)."""
        return sum(DECKVAL[card] for card in self.cards)

    @property
    def value(self):
        """The "hard" value of the cards in the hand (counting aces as 11
        unless this would go bust, otherwise as 1).

        """
        v = self.soft_value
        if v <= 11 and any(card[0] == 'A' for card in self.cards):
            return v + 10
        else:
            return v

    @property
    def bust(self):
        """True if this hand is bust."""
        return self.soft_value > 21

    @property
    def blackjack(self):
        """True if this hand is a blackjack (ace plus ten or face card)."""
        return len(self.cards) == 2 and self.value == 21


def play_again():
    play_again = input("Play again? Y/n ").lower()
    if play_again != 'n':
        clear()
        main()
    else:
        print("\n\n\n\nCatch ya later!\n\n\n\n")
        time.sleep(1.5)
        clear()
        exit()


def main():
    """Play a hand of blackjack."""

    deck = Deck()
    hand = Player(deck)
    dealer = Player(deck)

    clear()
    print("========\/\/\/\/\/ Welcome to 21 Pythonjack! \/\/\/\/\/========\n")
    print("Suits:  [S] = Spades | [C] = Clubs | [D] = Diamonds | [H] = Hearts")
    print("Values:  [A] = Ace(1) | [T] = 10 | [J] = Jack | [Q] = Queen | [K] = King\n")
    print("Dealer's hand: {}".format(dealer.cards[0]))

    # Player logic
    while True:
        print("Your hand: {} | Total = {}\n".format(hand, hand.value))
        if hand.bust:
            print("Bust! You LOSE!\n")
            play_again()
        print("What's your move?")
        choice = input("\n[H]it or [S]tay? ").lower()

        if choice == 's':
            break
        elif choice == 'h':
            card = hand.draw(deck)
            print("\nYou drew: {}".format(card))
        else:
            print("Invalid input. Try again!\n")

    # Dealer logic ("soft 17" variant)
    while True:
        print("Dealer's hand: {} | Total = {}\n".format(dealer, dealer.value))
        if dealer.soft_value >= 17:
            break
        card = dealer.draw(deck)
        print("Dealer drew: {}\n".format(card))

    if dealer.bust:
        print("Dealer is bust. You WIN!\n")
        play_again()
    elif dealer.blackjack and not hand.blackjack:
        print("Dealer's blackjack beats your {}\n".format(hand.value))
        play_again()
    elif hand.blackjack and not dealer.blackjack:
        print("Your blackjack beats dealer's {}!\n".format(dealer.value))
        play_again()
    elif dealer.value > hand.value:
        print("Dealer's {} beats your {}!\n".format(dealer.value, hand.value))
        play_again()
    elif hand.value > dealer.value:
        print("Your {} beats dealer's {}!\n".format(hand.value, dealer.value))
        play_again()
    else:
        print("Push: {} each\n".format(hand.value))
        play_again()


clear()
main()
