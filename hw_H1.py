"""
Реализовать классы Survivor и Zombie, отнаследованные от одного класса
с атрибутом hp (health points), отвечающий за здоровье. Смоделировать
их сражение. К примеру, в цикле с задержкой через time.sleep(1)
давать каждому по очереди выполнять действие attack, которое через
наносит случайный урон random.randint(0, 20). Интересные вариации и
возможная интерактивность для выбора действий приветствуется.
"""
import random
random.seed()
class Entity:
    def __init__(self, name):
        self._name = name
        self._hp = 100
        self._attack_power = random.randint(0, 20)
        self._attack_modifier = 0
    ###################################################
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp_in):
        if 0 > hp_in:
            print("hp cannot be < 0!")
            return
        self._hp = hp_in

    @hp.deleter
    def age(self):
        print(f'Error! hp cannot be deleted!')
    #######################################################
    @property
    def attack_modifier(self):
        return self._attack_modifier

    @attack_modifier.setter
    def attack_modifier(self, attack_modifier_in):
        self._attack_modifier = attack_modifier_in

    @attack_modifier.deleter
    def attack_modifier(self):
        print(f'Error! attack_modifier cannot be deleted!')
    ###########################################
    @property
    def attack_power(self):
        return self._attack_power

    @attack_power.setter
    def attack_power(self, attack_power_in):
        if 0 > attack_power_in + self._attack_modifier:
            print("attack_power cannot be < 0!")
            return
        self._attack_power = attack_power_in + self._attack_modifier

    @attack_power.deleter
    def attack_power(self):
        print(f'Error! attack_power cannot be deleted!')
    ###################################################
    def receive_damage(self, damage):
        self._hp -= damage
        if self._hp<=0:
            self._hp = 0
            print(f'{self._name} died!')
        else:
            print(f'{self._name} has {self._hp} hp left.')
#########################################################################################
class Human(Entity):
    """docstring for Human."""

    def __init__(self, name):
        super().__init__(name)
        self._has_weapon = False

    def got_weapon(self):
        self._has_weapon = True

    def is_armed(self):
        return self._has_weapon
#########################################################################################
class Zombie(Entity):
    """docstring for Zombie."""

    def __init__(self, name):
        super().__init__(name)

name = input("Input your name: ")

jhon = Human(name)
z = Zombie("Zombie")

# while jhon.hp * z.hp > 0:
#     z.receive_damage(jhon.attack_power)
#     jhon.receive_damage(z.attack_power)
#     z.attack_power = random.randint(0,20)
#     jhon.attack_power = random.randint(0,20)

while jhon.hp * z.hp > 0:
    user_in = input("1 - attack the enemy!\n2 - try to avoid enemy's attack!\n3 - try to find a weapon!\n4 - kill yourself!\n\n")
    try:
        if int(user_in) == 1:
            print("Smash!")
            z.receive_damage(jhon.attack_power)
            jhon.receive_damage(z.attack_power)
            z.attack_power = random.randint(0,20)
            jhon.attack_power = random.randint(0,20)
        elif int(user_in) == 2:
            if random.randint(0, 1):
                print("You avoided enemy's attack! Now you have a temporary advantage!")
                jhon.attack_power += jhon.attack_power + 5
                z.attack_power = random.randint(0,20)
            else:
                print("You failed to avoid enemy's attack! It hurts and your blood smells awful!")
                jhon.receive_damage(z.attack_power)
                z.attack_power = random.randint(0,20)
                jhon.attack_power = random.randint(0,20)
        elif int(user_in) == 3:
            if not jhon.is_armed():
                if random.randint(1, 3) > 2:
                    print("You have found a weapon! Congratulations!")
                    jhon.got_weapon()
                    jhon.attack_modifier = random.randint(6, 12)
                    print(f'Now you have a permanent attack_modifier = {jhon.attack_modifier}')
                    jhon.attack_power = random.randint(0,20)
                    print("...But still the enemy attacks you!")
                    jhon.receive_damage(z.attack_power)
                    z.attack_power = random.randint(0,20)
                else:
                    print("You failed to find a weapon! Enemy attacks you! Enormous pain!")
                    jhon.receive_damage(z.attack_power)
                    z.attack_power = random.randint(0,20)
                    jhon.attack_power = random.randint(0,20)
            else:
                print("You have already armed! You are wasting your time so you are attacked by the enemy!")
                jhon.receive_damage(z.attack_power)
                z.attack_power = random.randint(0,20)
                jhon.attack_power = random.randint(0,20)
        elif int(user_in) == 4:
            jhon.receive_damage(jhon.hp)
            print("You successfully ended your life!")
        else:
            print("Incorrect input. Try again")
    except ValueError:
        print("Incorrect input. Try again")
