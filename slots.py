import random

class SlotMachine:

    SLOT_OPTIONS = ["BAR", "cherries", "space", "7"]

    def __init__(self):
        self.bet = 0
        self.multiplier = 0
        self.game_earnings = 0
        self.slots = ["", "", ""]

    def get_pay_multiplier(slotmachine):
        pass

    # Get players bet
    def get_bet(self):
        bet_amount = -1
        while bet_amount < 0 or bet_amount > 50:
            bet_amount = int(input("How much would you like to bet (0 to quit)? "))
            if bet_amount < 0 or bet_amount > 50:
                print("Please enter a legal betting amount of $1 to $50")
        self.bet = bet_amount

    """ 
    BAR is 45% chance
    Cherries is 40% chance
    SPACE is 5% chance
    7 is 10% chance
    """
    def pull(self):
        for slot in range(0, len(self.slots)):
            chance = random.randint(1, 100)
            if chance <= 5:
                self.slots[slot] = "SPACE"
            elif chance <= 15:
                self.slots[slot] = "7"
            elif chance <= 55:
                self.slots[slot] = "Cherries"
            else:
                self.slots[slot] = "BAR"

    """
    Cherries | not cherries | any = 5x bet
    Cherries | cherries | not cherries = 15x bet
    Cherries | cherries | cherries = 30x bet
    BAR | BAR | BAR = 50x bet
    7 | 7 | 7 = 100x bet
    """
    def get_pay_multiplier(self):
        if self.slots[0] == "Cherries" and self.slots[1] != "Cherries":
            self.multiplier = 5
        elif self.slots[0] == self.slots[1] == "Cherries" and self.slots[2] != "Cherries":
            self.multiplier = 15
        elif self.slots[0] == self.slots[1] == self.slots[2] == "Cherries":
            self.multiplier = 30
        elif self.slots[0] == self.slots[1] == self.slots[2] == "BAR":
            self.multiplier = 50
        elif self.slots[0] == self.slots[1] == self.slots[2] == "7":
            self.multiplier = 100
        else:
            self.multipler = 0
    
    def display(self):
        print(self.slots)
        earnings = self.bet * self.multiplier
        print(f"You received a multipler of {self.multiplier}X")
        if earnings == 0:
            print("Sorry - you lost!")
        else:
            self.game_earnings += earnings
            print(f"Congratulations, you won ${earnings}")
            print("---------------------")
            print(f"You have earned a total of${self.game_earnings} today!")



def main():
    #Initiate slot machine variable
    slotm = SlotMachine()

    while True:
        slotm.get_bet()
        if slotm.bet == 0:
            # Breaks out of the while loop and ends the program
            print("Thanks for playing!")
            break
        else:
            slotm.pull()
            slotm.get_pay_multiplier()
            slotm.display()

main()