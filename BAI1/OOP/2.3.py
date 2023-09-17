import random
class Cards:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def display_cards(self):
        for suit, value in self.cards:
            print(f"{value} of {suit}")

deck = Cards()
print("Bộ bài trước khi xáo trộn:")
deck.display_cards()
deck.shuffle()
print("\nBộ bài sau khi xáo trộn:")
deck.display_cards()
