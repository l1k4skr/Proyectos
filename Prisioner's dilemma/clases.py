from random import choice

class player:
    def __init__(self, name) -> None:
        self.coins = 0
        self.name = name
        self.option = ["cooperate", "betray"]
        self.plays = []
    
    def __str__(self) -> str:
        self.show_info()
        return "\n"
            

    def show_info(self):
        print("Player: ", self.name)
        print("Coins: ", self.coins)
        print("Plays: ", self.plays)
        
    def choice_option(self, option=None):
        if option != None:
            return option
        
        else:
            return choice(self.option)


# Some basic strategies
class cooperate(player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.strategy = "Cooperate"
        
    def choice_option(self, option=None):
        return "cooperate"
    
class betray(player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.strategy = "Betray"
        
    def choice_option(self, option=None):
        return "betray"

class cooperate1_betray2(player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.strategy = "Cooperate and Betray"
        
    def choice_option(self, option=None):
        if len(self.plays) % 2 == 0:
            return "cooperate"
        else:
            return "betray"