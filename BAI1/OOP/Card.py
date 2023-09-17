class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def print_card(self):
        print(f"Card suit: {self.suit}")
        print(f"Card value: {self.value}")
def main():
    my_card = Card("Hearts", "A")
    my_card.print_card()
if __name__ == "__main__":
    main()



