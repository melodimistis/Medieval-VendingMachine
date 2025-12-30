import random

coins = random.randint(1, 10000)

class Player:
    def __init__ (self, name, coins):
        self.name = name
        self.coins = coins

usr = (Player('Traveler', coins))

class Equipment:
    def __init__ (self, name, price):
        self.name = name
        self.price = price

items_equipment = {
    '1': Equipment('Iron Sword', 399),
    '2': Equipment('Shield', 500),
    '3': Equipment('Iron Full Armor', 1500),
    '4': Equipment('Iron Axe', 450),
    '5': Equipment('Iron Pickaxe', 400),
    '6': Equipment('Bow', 220),
    '7': Equipment('Arrow (x32)', 190),
    '8': Equipment('Torch (x16)', 50),
    '9': Equipment('Shovel', 180),
    '10': Equipment('Hoe', 150),
    '11': Equipment('Fishing Rod', 240),
}

class Food:
    def __init__ (self, name, price):
        self.name = name
        self.price = price

items_food = {
    '1': Food('Bread', 100),
    '2': Food('Milk', 130),
    '3': Food('Apple', 50),
    '4': Food('Cooked Chicken', 180),
    '5': Food('Chicken Soup', 200),
    '6': Food('Chicken Grilled', 240),
    '7': Food('Mushroom Soup', 120),
    '8': Food('Corn', 75),
    '9': Food('Raw Chicken', 100),
    '10': Food('Cookies (x6)', 35),
    '11': Food('Raw Beef', 140),
    '12': Food('Cooked Beef', 250),
}

class Exp:
    def __init__ (self, name, price):
        self.name = name
        self.price = price

items_exp = {
    '1': Exp('Small Exp Bottle', 120),
    '2': Exp('Medium Exp Bottle', 230),
    '3': Exp('Large Exp Bottle', 300),
    '4': Exp('Skill Exp Bottle', 500),
    '5': Exp('Extra Skill Exp Bottle', 1300),
    '6': Exp('Class Exp Bottle', 1500),
    '7': Exp('Stat Exp Bottle', 3000),
    '8': Exp('Knowledge Exp Bottle', 4350),
    '9': Exp('Extra Stat Exp Bottle', 6500),
}

class Potions:
    def __init__ (self, name, price):
        self.name = name
        self.price = price

items_potions = {
    '1': Potions('Health Potion', 300),
    '2': Potions('Mana Potion', 500),
    '3': Potions('Stamina Potion', 450),
    '4': Potions('Buff Potion', 500),
    '5': Potions('Strength Potion', 600),
    '6': Potions('Defense Potion', 600),
    '7': Potions('Regen Potion', 300),
    '8': Potions('Resistance Potion', 1000),
    '9': Potions('Antidote Potion', 700),
}