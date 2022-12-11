class Human:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"hello my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp

class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team


hb_player = Player("hb")
hb_player.say_hello()

hb_fan = Fan("hb_fan", "x")
hb_fan.say_hello()