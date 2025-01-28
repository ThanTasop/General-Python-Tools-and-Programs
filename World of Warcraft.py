from random import randrange, uniform


class Equipment:
    def __init__(self, sword, cape):
        self.sword = sword
        self.cape = cape

    def __str__(self):
        return f"Sword value: {self.sword}\nArmor Value: {self.cape}"

    def __repr__(self):
        return f"Equipment({self.sword}, {self.cape})"


class Character:
    def __init__(self, name, equipment, health=100, attack_speed=2, delay=0):
        self.name = name
        self.equipment = equipment
        self.health = health*equipment.cape
        self.attack_speed = attack_speed
        self.delay = delay
        self.damage = 0
        self.max_delay = 5
        self.attack_range = (3, 11)
        self.max_health = 100*equipment.cape

    def attack(self):
        self.delay = self.max_delay-self.attack_speed
        return round(randrange(self.attack_range[0],self.attack_range[1])*self.equipment.sword)

    def is_dead(self):
        return self.health <= 0

    def end_round(self):
        if self.health < self.max_health:
            self.health += 1
        if self.delay > 0:
            self.delay -= 1

    def __str__(self):
        return f"Name: {self.name}\nHealth: {round(self.health)}\nAttack Speed: {self.attack_speed}\n\
Delay: {self.delay}\nEquipment: {str(self.equipment)}\nDamage Done: {self.damage}"

    def __iadd__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            self.health += other
        return self

    def __isub__(self, other):
        if isinstance(other, float):
            self.health -= other
        return self
    
    def __repr__(self):
        return f"Character({self.name}, {repr(self.equipment)}, {self.health/self.equipment.cape}, {self.attack_speed}, {self.delay})"


class Mage(Character):
    def __init__(self, name, equipment, health=100, attack_speed=2, delay=0, mana=100):
        super().__init__(name, equipment, health, attack_speed, delay)
        self.attack_range = (8, 17)
        self.mana = mana
        self.max_mana = 100

    def end_round(self):
        super().end_round()
        if self.mana < self.max_mana:
            self.mana += 1

    def lightning_spell(self):
        self.mana -= 55
        return randrange(30, 51)

    def attack(self):
        self.delay = self.max_delay-self.attack_speed
        if self.mana >= 55:
            return self.lightning_spell()
        else:
            return round(randrange(self.attack_range[0],self.attack_range[1])*self.equipment.sword)


class Tank(Character):
    def __init__(self, name, equipment, health=100, attack_speed=2, delay=0):
        super().__init__(name, equipment, health, attack_speed, delay)
        self.attack_range = (20, 30)
        self.health = health*equipment.cape * 2
        self.max_health = 100 * equipment.cape * 2


class Arena:
    def __init__(self, team_A, team_B):
        self.team_A = team_A
        self.team_B = team_B
        
    def __str__(self):
        new_A = []
        for char in self.team_A:
            new_A.append(str(char))
        new_B = []
        for char in self.team_B:
            new_B.append(str(char))
        return f"-------Team A-------\n{"\n-----\n".join(new_A)}\n-------Team B-------\n{"\n-----\n".join(new_B)}"

    def __repr__(self):
        string = "Arena(["
        string += ", ".join([repr(character) for character in self.team_A])
        string += "], ["
        string += ", ".join([repr(character) for character in self.team_B])
        string += "])"
        return string

    def play(self):
        counter = 0
        while True:
            list_A = [char for char in self.team_A if char.delay == 0]
            list_B = [char for char in self.team_B if char.delay == 0]
            for char in list_A:
                x = randrange(len(self.team_B))
                x = x % len(self.team_B)
                for _ in range(len(self.team_B)):
                    if self.team_B[x].health > 0:
                        damage = char.attack()
                        char.damage += damage
                        self.team_B[x].health -= damage
                        print(f"{char.name} dealt {damage} damage to {self.team_B[x].name}")
                        break
                    else:
                        x += 1
                        x = x % len(self.team_B)
            for char in list_B:
                x = randrange(len(self.team_A))
                x = x % len(self.team_A)
                for _ in range(len(self.team_A)):
                    if self.team_A[x].health > 0:
                        damage = char.attack()
                        char.damage += damage
                        self.team_A[x].health -= damage
                        print(f"{char.name} dealt {damage} damage to {self.team_A[x].name}")
                        break
                    else:
                        x += 1
                        x = x % len(list_A)
            deads_A = []
            for char in self.team_A:
                if char.health <= 0:
                    deads_A.append(char)
                    print(f"\n-----------------------------\nPlayer {char.name} died at round {counter}!\n-----------------------------\n")
                else:
                    char.end_round()
            for char in deads_A:
                self.team_A.remove(char)
            deads_B = []
            for char in self.team_B:
                if char.health <= 0:
                    deads_B.append(char)
                    print(f"\n-----------------------------\nPlayer {char.name} died at round {counter}!\n-----------------------------\n")
                else:
                    char.end_round()
            for char in deads_B:
                self.team_B.remove(char)
            if len(self.team_A) == 0 and len(self.team_B) > 0:
                print("Team B won!")
                for char in self.team_B:
                    print(char)
                break
            elif len(self.team_B) == 0 and len(self.team_A) > 0:
                print("Team A won!\n")
                for char in self.team_A:
                    print(char)
                    print("------------------")
                break
            counter += 1


e = Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3))
team_A = [Tank("Sammouro", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 2, randrange(0,4)), Tank("Anzgul", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 2, randrange(0,4)),
          Character("Tiezzarda", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 2, randrange(0,4)), Character("Terribleday", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 2, randrange(0,4)),
          Character("Jeims", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 2, randrange(0,4))]
team_B = [Mage("Night elf 1", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 3, randrange(0,3)), Mage("Night elf 2", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 3, randrange(0,3)),
          Character("Night elf 3", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 3, randrange(0,3)), Mage("Night elf 4", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 100, 3, randrange(0,3))]
c1 = uniform(1.1,1.5)
c2 = uniform(1.1,1.3)
#Arena(team_A,team_B).play()
c = Character("Sammouro", Equipment(c1, c2), 100, 2, randrange(0,4))
Arena(team_A, team_B).play()












