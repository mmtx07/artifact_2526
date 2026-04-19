import datetime


class Artifact:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"{self.name} ({self.date})"

    def calculate_age(self):
        return datetime.datetime.now().year - self.date


class Painting(Artifact):
    def __init__(self, name, date, artist, medium):
        super().__init__(name, date)
        self.artist = artist
        self.medium = medium

    def __str__(self):
        return f"{self.name} ({self.date}) - {self.medium} by {self.artist}"

    def is_oil(self):
        return self.medium.lower() == "oil"


class Sculpture(Artifact):
    def __init__(self, name, date, material, size):
        super().__init__(name, date)
        self.material = material
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.date}) - {self.material}, size: {self.size}"

    def is_old(self, limit=100):
        return self.calculate_age() > limit
    
class Building(Artifact):
    def __init__(self, name, date, location, style):
        super().__init__(name, date)
        self.location = location
        self.style = style

    def __str__(self):
        return f"{self.name} ({self.date}) - {self.style} building in {self.location}"


def give_name_artifact():
    return f"artifact name: {__name__}"


if __name__ == "__main__":
    obj1 = Artifact("abc", 1321)
    print(f"{obj1.name} age: {obj1.calculate_age()}")
    print(obj1)
    print(f"{type(obj1).__name__=}")

    print("-------\n")

    painting1 = Painting("I and the Village", 1911, "Chagall", 'oil')
    print(painting1)
    print(f"{painting1.name}: age is {painting1.calculate_age()}; is oil: {painting1.is_oil()}")
    print(f"{type(painting1).__name__=}")

    print(give_name_artifact())