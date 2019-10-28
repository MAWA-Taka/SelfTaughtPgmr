
class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("Smith")
horse = Horse("Silver", rider)

print(horse.name)
print(horse.rider.name)
