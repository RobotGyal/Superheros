import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
    def attack(self):
        return random.randint(0,self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        pass
    def block(self):
        pass

class Hero:
    def __init__(self, name, starting_health):
        self.starting_health = "100"
    def add_ability(self, ability):
        pass
    def attack(self):
        pass
    def defend(self, incoming_danger):
        pass
    def take_damage(self, damage):
        pass
    def is_alive(self):
        pass
    def fight(self, opponent):
        pass


if __name__ == "__main__":
    ability = Ability("Debugging ability", 20)
    print(ability.name)
    print(ability.attack())