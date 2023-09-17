import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def compare_cards(self, other_card):
        # Custom comparison logic
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        return values.index(self.value) > values.index(other_card.value)

class DeckOfCards:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one_card(self):
        if len(self.cards) > 0:
            card = self.cards.pop()
            return Card(card[0], card[1])
        else:
            return None

    def display_cards(self):
        for suit, value in self.cards:
            print(f"{value} of {suit}")

deck = DeckOfCards()
print("Bộ bài trước khi xáo trộn:")
deck.display_cards()

deck.shuffle()

dealt_card = deck.deal_one_card()
if dealt_card:
    print("\nThẻ đã chia:")
    print(dealt_card)
else:
    print("\nKhông còn thẻ trong bộ bài.")

print("\nBộ bài sau khi chia:")
deck.display_cards()

card1 = Card("Hearts", "A")
card2 = Card("Hearts", "K")

if card1.compare_cards(card2):
    print("\nThẻ 1 mạnh hơn thẻ 2")
else:
    print("\nThẻ 2 mạnh hơn thẻ 1")
