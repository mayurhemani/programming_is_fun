class Dog:
    def __init__(self, nameOfTheDog):
        self.color = ""
        self.breed = ""
        self.furryOrNot = False
        self.loudnessOfBark = 0
        print(nameOfTheDog + " was just created")

    def run(self):
        print("This dog is running")

    def sit(self):
        print("This dog it sitting")

    def bark(self):
        print("Bow wow!" * self.loudnessOfBark)



bruno = Dog("bruno")
mars = Dog("mars")

bruno.loudnessOfBark = 10
mars.loudnessOfBark = 2


bruno.bark()
mars.bark()


#### self becomes whichever object the method is called from.
