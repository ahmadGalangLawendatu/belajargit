"""Modul Hewan"""


class Hewan:
    def __init__(self, nama="DefaultNama",
                 spesies="DefaultSpesies",
                 suara="DefaultSuara"):
        self.nama = nama
        self.spesies = spesies
        self.suara = suara

    def buat_suara(self):
        return f"{self.nama} bersuara {self.suara}"


cat = Hewan("Whiskers", "Cat", "Meow")
dog = Hewan("Buddy", "Dog", "Woof")
duck = Hewan("Daffy", "Duck", "Quack")

hewan_choices = [cat, dog, duck]
Hewan.hewan_choices = hewan_choices
