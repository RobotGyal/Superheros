import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
    def attack(self):
        return random.randint(0,self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0, self.max_block)

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_armor(self, armor):
        self.armors.append(armor)
    def add_kill(self, num_kills):
        self.kills += num_kills
    def add_deaths(self, num_deaths):
        self.deaths+=num_deaths
    def attack(self):
        total_damage=0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    def defend(self, damage_amt):
        for damage_amt in self.armors:
            total_armor = 0
            total_armor += damage_amt.block()
        return total_armor
    def take_damage(self, damage):
        self.current_health -= damage
    def is_alive(self):
        if self.current_health > 0:
            return  True
        return False
    def fight(self, opponent):
        while (self.is_alive() == True and opponent.is_alive() == True):
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
            if opponent.is_alive() == False: #if opponent loses
                self.add_kill(1)
                opponent.add_deaths(1)
                print("Winner is: ", self.name)
            else: #if opponent wins
                self.add_deaths(1)
                opponent.add_kill(1)
                print("Winner is: ", opponent.name)

class Team(Hero):
    def __init__(self, name):
        self.name = name
        self.heroes = []
    def add_hero(self, hero):
        self.heroes.append(hero)
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero) 
        return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    def attack(self, other_team):
        hero = random.choice(self.heroes)
        opponent = random.choice(other_team.heroes)
        Hero.fight(hero, opponent)
    def revive_heroes(self, health=100):
        Hero.health = 100
    def stats(self):
        print("Here are the current team stats: \n")
        for hero in self.heroes:
            print(hero.name, hero.kills, hero.deaths, hero.abilities, hero.armor)


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    opponent = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    opponent.add_ability(ability3)
    opponent.add_ability(ability4)
    hero1.fight(opponent)

    weapon1 = Weapon("Sword", 500)
    weapon1.attack()