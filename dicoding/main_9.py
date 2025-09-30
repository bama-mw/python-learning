class Animal:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    def deskripsi(self) -> str:
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara(self) -> str:
        return "meow!"

myCat = Cat(name="Neko", age=3, species="Persian")

print(myCat.deskripsi())
print(myCat.suara())