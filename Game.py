import random
import time
from enum import Enum

class Rarity(Enum):
    common="Обычный"
    rare="Редкий"
    expensive="Ценный"
class Item:
    def __init__(self, name, rarity, stat,itemType):
        self.name = name
        self.rarity = rarity
        self.stat = stat
        self.itemType = itemType
    @staticmethod
    def ChooseItem(createDrop,Rarity,Type):
        return random.choice(createDrop[Type][Rarity])
        return random.choice(createDrop[Type][Rarity])


class Character:
    def __init__(self, name, hp, gun, cArmor, cPhysDef, cMgcDef, cLvl, currentXp):
        self.name = name
        self.hp = 100
        self.gun = gun
        self.speed = 30
        self.damage = 10
        self.fRange = 5
        self.gAccuracy = 10
        self.cArmor = cArmor
        self.cPhysDef = cPhysDef
        self.cMgcDef = cMgcDef
        self.cLvl = cLvl
        self.currentXp = currentXp
        self.remainingXp = 100
        self.talent = 5
        self.slot = False
        self.armorSlot = False
        self.cAttackPoints = 1
        self.cActionPoints = 2
        self.cMaxHp = hp
        self.cash = 0
        self.medsSlot = False
        self.inventory=[]


    def inventoryView(self):
        if not self.inventory:
            print("Рюкзак пуст. ")
            return True
        else:
            for i, item in enumerate(self.inventory,0):
                print(f"{i} {item.name,item.rarity}")
            return True
        return False



    def inventory(self,i):
        self.inventoryView()
        invItem=self.inventory[i]
        if invItem.itemType == "meds":
            if self.hp+invItem.stat > self.cMaxHp:
                self.hp = self.cMaxHp
                self.inventory.remove(invItem)
                print(f"Вы восстановили здоровье до максимума ({self.cMaxHp})")
            elif self.hp == self.cMaxHp:
                #медикамент не тратится
                print("У вас максимальный запас здоровья, вы не можете использовать медикамент.")
            else:
                self.hp += invItem.stat
                self.inventory.remove(invItem)
                print(f"Вы восстановили здоровье до {self.hp}/{self.cMaxHp}")


        #добавить ограничения по типу невозможности хилиться больше максимального количества хп






    # создать дефолтного дебильчика с базовыми статами и выдать ему какое нибудь изначальное оружие
    def talentUse(self):
        if self.talent <= 0:
            print("У вас нет очков таланта")
            return False
        else:
            while self.talent > 0:
                print(f"У вас есть {self.talent} очков таланта")
                print("Нажмите 1 чтобы прокачать здоровье")
                print("Нажмите 2 чтобы прокачать скорость")
                print("Нажмите 3 чтобы прокачать урон")
                print("Нажмите 4 чтобы прокачать точность")
                print("Нажмите 5 чтобы посмотреть свою статистику. ")
                print("Нажмите 6 чтобы выйти из меню прокачки. ")
                tUp = int(input("выберите навык для прокачки "))
                if tUp == 1:
                    self.hp += 10
                    self.talent -= 1
                    print("Вы вложили 1 очко таланта в здоровье. ")
                elif tUp == 2:
                    self.speed += 10
                    self.talent -= 1
                    print("Вы вложили 1 очко таланта в скорость. ")
                elif tUp == 3:
                    self.damage += 5
                    self.talent -= 1
                    print("Вы вложили 1 очко таланта в урон. ")
                elif tUp == 4:
                    self.gAccuracy += 10
                    self.talent -= 1
                    print("Вы вложили 1 очко таланта в точность. ")
                elif tUp == 5:
                    self.stats()
                    continue
                elif tUp == 6:
                    print("Выход из прокачки...")
                    break
                else:
                    print("Не, не хочу.")
                    continue
        return True

    def stats(self):
        print(f"Имя персонажа: {self.name} ")
        print(f"Здоровье персонажа: {self.hp} ")
        print(f"Используемое оружие: {self.gun} ")
        print(f"Скорость персонажа: {self.speed} ")
        print(f"Урон Экипированного оружия: {self.damage} ")
        print(f"Дальность экипированного оружия : {self.fRange} ")
        print(f"Точность экипированного оружия: {self.gAccuracy} ")
        print(f"Экипированная броня: {self.cArmor} ")
        print(f"Физическая защита экипированной брони:{self.cPhysDef} ")
        print(f"Магическая защита экипированной брони:{self.cMgcDef} ")
        print(f"Текущий уровень персонажа:{self.cLvl} ")
        print(f"Текущий опыт:{self.currentXp} ")
        print(f"Нужно опыта до следующего уровня:{self.remainingXp - self.currentXp} ")

    def lvlGet(self, xpGave):
        self.currentXp += xpGave
        print(f"Вы получили {xpGave} опыта ")
        lvlGive = 0
        while self.currentXp > self.remainingXp:
            self.talent += 1
            self.lvlUp()
            lvlGive += 1
            self.currentXp -= 100
        print(f"Получено {lvlGive} уровней, у вас остались нераспределенные очки талантов: {self.talent} ")

    def lvlUp(self):
        self.cLvl += 1
        print(f"У тебя теперь {self.cLvl} уровень. ")
        print(f"У тебя осталось {self.talent} очков талантов, готовых к распределению. ")
        print(f"До следующего уровня осталось {self.remainingXp - self.currentXp}")


name, hp, gun, speed, damage = None, None, None, None, None


# def Function():
#     global name, hp, gun, speed, damage, A
#     try:
#         if name == None:
#             name = input("введите имя класса ")
#         if hp == None:
#             hp = int(input("введите здоровье класса "))
#         if gun == None:
#             gun = input("введите оружие класса ")
#         if speed == None:
#             speed = int(input("введите скорость класса "))
#         if damage == None:
#             damage = int(input("введите урон класса "))
#         A = Character(name, hp, gun, speed, damage)
#         print(A.name, A.hp, A.gun, A.speed, A.damage)
#     except ValueError:
#         print("это должно быть написано цифрами, переделывай ")
#         Function()


#Function()


class Armor:
    def __init__(self, name, pDefence, mDefence, character=None):
        self.name = name
        self.pDefence = pDefence
        self.mDefence = mDefence

    def take(self, character):
        character.armorSlot = True
        character.PhysDefence += self.pDefence
        character.cMgcDefence += self.mDefence

    def drop(self, character):
        character.armorSlot = False
        character.PhysDefence -= self.pDefence
        character.cMgcDefence -= self.mDefence


class Weapon:
    def __init__(self, name, fireRate, physDmg, magicDmg, range, accuracy):
        self.name = name
        self.fireRate = fireRate
        self.physDmg = physDmg
        self.magicDmg = magicDmg
        self.range = range
        self.accuracy = accuracy

    def take(self, character):
        character.slot = True
        character.damage += self.physDmg + self.magicDmg
        character.speed += self.fireRate
        character.fRange += self.range
        character.gAccuracy += self.accuracy
        character.cAttackPoints = self.fireRate // 5

    def drop(self, character):
        character.slot = False
        character.damage -= self.physDmg + self.magicDmg
        character.speed -= self.fireRate
        character.fRange -= self.range
        character.gAccuracy -= self.accuracy
        character.cAttackPoints = 1


class Meds:
    def __init__(self, name, healHp, actionPointsUse):
        self.name = name
        self.healHp = healHp
        self.actionPointsUse = actionPointsUse

    def take(self, character, item):
        character.medsSlot = item
        character.inventory.append(item)
        return f"{item.name} был добавлен в инвентарь"

    def drop(self, character, item):
        character.medsSlot = False
        character.inventory.remove(item)
        return f"{item.name} был удален из инвентаря"


class Enemy:
    def __init__(self, name, hp, gun, physDmg, mgcDmg, fRange,cArmor, gAccuracy, cPhysDef, cMgcDef, giveXp, lvl,):
        self.name = name
        self.hp = hp
        self.gun = gun
        self.physDmg = physDmg
        self.mgcDmg = mgcDmg
        self.fRange = fRange
        self.gAccuracy = gAccuracy
        self.cArmor = cArmor
        self.cPhysDef = cPhysDef
        self.cMgcDef = cMgcDef
        self.giveXp = giveXp
        self.lvl = lvl
        self.maxHp = hp
    @staticmethod
    def ChoiceEnemy(cLvl):
        if cLvl <= 50:
            eLvl = max(1, cLvl + random.randint(-5, 5))
        elif 50 < cLvl <= 100:
            eLvl = max(1, cLvl + random.randint(-5, 10))
        elif 100 < cLvl <= 200:
            eLvl = max(1, cLvl + random.randint(-10, 20))
        else:
            eLvl = max(1, cLvl + random.randint(-20, 40))
        avaliableEnemy = []
        for i in enemy:
            if abs(i.lvl - eLvl) <= 5:
                avaliableEnemy.append(i)
        return random.choice(avaliableEnemy)




# добавить возможность подбежать к врагу
def HitChance(character, enemy, distance):
    BaseAccuracy = character.gAccuracy
    dRange = character.fRange - distance
    if dRange >= 0:
        # порезка урона
        damageP = 0
    else:
        damageP = abs(dRange)
    finalHitChance = BaseAccuracy - damageP + character.speed
    return max(15, min(100, finalHitChance))


def CrateItems(caseType, crateRarity):
    items = []
    # поменять проверку сначала типа потом редкости снизу
    if crateRarity == 1:
        if caseType == "meds":
            return random.choice(CrateDrop["meds"][1])
    if crateRarity == 2:
        if caseType == "meds":
            return random.choice(CrateDrop["meds"][2])
    if crateRarity == 3:
        if caseType == "meds":
            return random.choice(CrateDrop["meds"][3])
    if crateRarity == 1:
        if caseType == "weapon":
            return random.choice(CrateDrop["weapon"][1])
    if crateRarity == 2:
        if caseType == "weapon":
            return random.choice(CrateDrop["weapon"][2])
    if crateRarity == 3:
        if caseType == "weapon":
            return random.choice(CrateDrop["weapon"][3])
    if crateRarity == 1:
        if caseType == "armor":
            return random.choice(CrateDrop["armor"][1])
    if crateRarity == 2:
        if caseType == "armor":
            return random.choice(CrateDrop["armor"][2])
    if crateRarity == 3:
        if caseType == "armor":
            return random.choice(CrateDrop["armor"][3])


def CaseOpen(character, caseRarity):
    global armory, armor, meds
    print("Вы роетесь в сундуке", end="")
    for i in range(6):
        time.sleep(0.3)
        print(".", end="")
    print()
    caseType = random.choice(["meds", "Weapon", "Armor"])
    if character.lvl <= 10:
        caseChance = random.random()
        if caseChance <= 0.9:
            crateRarity = 1
        elif caseChance <= 0.99:
            crateRarity = 2
        else:
            crateRarity = 3
    if character.lvl <= 20:
        caseChance = random.random()
        if caseChance <= 0.7:
            crateRarity = 1
        elif caseChance <= 0.95:
            crateRarity = 2
        else:
            crateRarity = 3
    if character.lvl <= 40:
        caseChance = random.random()
        if caseChance <= 0.5:
            crateRarity = 1
        elif caseChance <= 0.7:
            crateRarity = 2
        else:
            crateRarity = 3
    if character.lvl <= 60:
        caseChance = random.random()
        if caseChance <= 0.2:
            crateRarity = 1
        elif caseChance <= 0.5:
            crateRarity = 2
        else:
            crateRarity = 3
    crateName = case_types[caseType][crateRarity]
    givenDrop = CrateItems(caseType, crateRarity)
    print(f"Вы нашли {givenDrop} в {crateName}")
    print("1 чтобы экипировать")
    print("2 чтобы оставить")
    if caseType == "Weapon":
        dropChoice = int(input())
        if dropChoice == 1:
            Weapon.take(character)
        else:
            Weapon.drop(character)
    if caseType == "Meds":
        dropChoice = int(input())
        if dropChoice == 1:
            Meds.take(character)
        else:
            Meds.drop(character)
    if caseType == "Armor":
        dropChoice = int(input())
        if dropChoice == 1:
            Armor.take(character)
        else:
            Armor.drop(character)


# список медикаментов, добвить оружия и добавить стату очков атаки или оптимизировать скорострельность под очки атаки.

def LutiyFight(character, currentEnemy):
    meet = [f"Вы встретились с {currentEnemy.name}. Как он вообще тут оказался?...",
            f"Вы заметили {currentEnemy.name}. Не думаю, что он пойдет на контакт."]
    print(random.choice(meet))
    print(f"У этого противника {currentEnemy.hp}.")
    distance = random.randint(1, 100)
    print(f"Враг в {distance} метрах от вас.")

    while character.hp > 0 and currentEnemy.hp > 0:
        attackPoints = character.cAttackPoints
        actionPoints = character.cActionPoints
        print(
            "Нажмите 1 для атаки.\nНажмите 2 для побега. \nНажмите 3 для приближения к врагу. \nНажмите 4 для отдаления от врага. \nНажмите 5 для принятия медикаментов.")


        while attackPoints > 0 or actionPoints > 0:
            print(f"вам доступно {character.cActionPoints} очков действий и {character.cAttackPoints} очков атаки")
            battleChoice = int(input())
            if battleChoice == 1:
                if attackPoints <= 0:
                    print("У вас недостаточно очков аттаки")
                    continue
                character.cAttackPoints -= 1
                hitChance = HitChance(character, currentEnemy, distance)
                print(f"Шанс попадания {hitChance}.(Удалить) ")
                hit = False
                if random.randint(1, 100) <= hitChance:
                    damage = character.damage
                    currentEnemy.hp -= damage
                    print(f"Вы Нанесли {damage} урона.")
                    hit = True
                    if currentEnemy.hp <= 0:
                        print(f"Вы поразили {currentEnemy.name}.")
                        character.lvlGet(currentEnemy.giveXp)
                else:
                    print("Вы промахнулись")

            if battleChoice == 2:
                if actionPoints <= 0:
                    print("У вас недостаточно очков действия")
                    continue

                runawayChance = character.speed / 10
                runaway = random.random()
                if runaway <= runawayChance:
                    break
                else:
                    print("Вам не удалось сбежать.")
                    continue
            if battleChoice == 3:
                if actionPoints <= 0:
                    print("У вас недостаточно очков действия")
                    continue
                character.cActionPoints -= 1
                runDistance = character.speed * 5
                distance -= runDistance
                print(f"Вы пробежали {runDistance} метров к врагу.")
                continue
            if battleChoice == 4:
                if actionPoints <= 0:
                    print("У вас недостаточно очков действия")
                    continue
                character.cActionPoints -= 1
                runawayDistance = character.speed * 5
                distance += runawayDistance
                print(f"Вы пробежали {runawayDistance} метров от врага.")
                continue
            if battleChoice == 5:
                if actionPoints <= 0:
                    print("У вас недостаточно очков действия")
                    continue
                character.cActionPoints -= 1

            if currentEnemy.hp > 0:
                enemyHitChance = currentEnemy.gAccuracy - max(0, (distance - currentEnemy.fRange) // 10)
                if distance >= currentEnemy.fRange:
                    runDistance = 5 * 5
                    distance -= runDistance
                    print(f"Враг пробежал {runDistance} метров в вашу сторону.")
                    continue
                elif distance <= currentEnemy.fRange:
                    print(f"Шанс попадания врага {enemyHitChance} (Удалить)")
                    if random.randint(1, 100) <= enemyHitChance:
                        character.hp -= currentEnemy.physDmg + currentEnemy.mgcDmg
                        print(
                            f"{currentEnemy.name} попадает по вам и наносит вам {currentEnemy.physDmg + currentEnemy.mgcDmg} урона.")
                        character.cActionPoints = character.cActionPoints
                        character.cAttackPoints = character.cAttackPoints
                        if character.hp <= 0:
                            print("ВЫ УМЕРЛИ")
                            return False
                    else:
                        print(f"{currentEnemy.name} промахнулся!")
                        character.cActionPoints = character.cActionPoints
                        character.cAttackPoints = character.cAttackPoints
                        continue
            turnCounter = 0
            if currentEnemy.hp <= currentEnemy.maxHp * 0.3:
                healHp = currentEnemy.maxHp * 0.7
                if turnCounter == 0:
                    turnCounter += 1
                    continue
                elif turnCounter >= 1:
                    if hit:
                        continue
                    else:
                        currentEnemy.hp = healHp
                        continue


# Продумать алгоритм действий внутри битвы, для побега и динамической прокачки.
enemy = [Enemy("Goblin", 15, "Wooden Stick", 10, 5, 30, "Burlap Clothes", 5, 5, 2, 1,1),
         Enemy("Goblin With A Magic Stick", 20, "Magic(?) Stick", 15, 25, 20, "Burlap Clothes", 5, 5, 3, 3,1),
         Enemy("Goblin, Who Thinks He's A Warrior", 30, "Wooden Sword (Kind Of)", 20, 10, 30, "Poor Wooden Shield", 10,
               5, 5, 5,3),
         Enemy("Skeleton", 25, "Stone Sword", 20, 13, 30, "Nothing...", 10, 0, 7, 10,3),
         Enemy("Skeleton Wizard", 25, "Magic Stick", 23, 25, 40, "Old Magic Cape", 10, 15, 10, 10,5),
         Enemy("A Guy With A Knife", 30, "Bayonet", 30, 5, 60, "Nice Set Of Clothes", 20, 10, 10, 15,5),
         Enemy("Beginner Wizard", 30, "A Spell Book (Over 100 Spells inside!)", 20, 25, 40,
               "Enchanted Clothes (Whole set for only 9.99!)", 5, 15, 13, 15,7),
         Enemy("Armed Bum", 30, "Handmade Sword", 40, 5, 20, "Coat", 10, 10, 20, 20,8),
         Enemy("FireArmed Bum", 30, "Poor Handmade Hammer Pistol", 30, 13, 25, "Coat", 10, 10, 22, 20,10),
         Enemy("Wolf", 50, "Teeth, I guess?", 40, 3, 50, "Nothing...", 5, 5, 30, 25,10),
         Enemy("An Alright Wizard", 30, "Magic Stick. A really simple one", 30, 35, 40, "Simple Enchanted Clothes", 15,
               25, 25, 25,13),
         Enemy("Expirienced Armed Bum", 35, "Handmade Sword", 45, 7, 25, "Coat", 15, 10, 30, 30,15),
         Enemy("Goblin Wizard", 30, "Magic Stick 3000", 35, 40, 55, "Enchanted Set Of Clothes", 15, 20, 32, 30,15),
         Enemy("Zombie", 40, "Hands? Jaw?", 45, 3, 30, "Nice Set Of Clothes", 20, 15, 35, 35,15),
         Enemy("Bear", 50, "Paws", 40, 2, 40, "Nothing...", 10, 0, 40, 41,20),
         Enemy("Armed Guy", 50, "Lock18", 40, 50, 30, "Light Gear", 20, 10, 50, 50,20),
         Enemy("Armed Guy", 55, "Handmade SMG", 40, 50, 40, "Light Gear With A Plate Carrier", 30, 10, 50, 50,23),
         Enemy("Armed Guy", 55, "Handmade Thompson", 55, 60, 50, "Roadsign Gear", 35, 10, 55, 55,25), ]

armor = [Armor("Burlap Clothes", 10, 5),
         Armor("Old Cape", 5, 15),
         Armor("Nice Set Of Clothes", 20, 10),
         Armor("Enchanted Magic Clothes", 7, 20),
         Armor("Roadsign Armor Set", 35, 10),
         Armor("Wizard Clothes", 15, 35),
         Armor("High Quality Metal Gear", 50, 15),
         Armor("Military Grade Armor", 60, 15),
         Armor("Anti-Radiation Suit", 30, 30),
         Armor("Enchanted Old Wizard's Set", 20, 50), ]

armory = [Weapon("Simple Handmade Rifle", 5, 40, 0, 30, 35),
          Weapon("Simple Axe", 30, 30, 0, 7, 60),
          Weapon("Lock18", 15, 20, 0, 40, 50),
          Weapon("MagickStick3000", 5, 0, 27, 25, 40),
          Weapon("Bayonet", 10, 40, 0, 5, 90),
          Weapon("Handmade Assault Rifle", 20, 50, 0, 80, 60),
          Weapon("Military Grade Assault Rifle", 35, 40, 0, 90, 65),
          Weapon("Enchanted Magic Stick", 10, 0, 40, 40, 50),
          Weapon("Old Magic Book", 15, 5, 35, 30, 70),
          Weapon("M249 LMG", 50, 40, 0, 70, 70),
          Weapon("Bolt Action Rifle", 7, 80, 0, 100, 95),
          Weapon("L3 Sniper Rifle", 5, 95, 0, 120, 100)]

meds = [Meds("Bandage", 5, 1)
    , Meds("Propital Syringe", 150, 1),
        Meds("AFAK", 400, 2),
        Meds("", 150, 1)]

# доделать список ниже
CrateDrop = {"meds": {
    1: [Meds("Bandage", 5, 1)],
    2: [Meds("AFAK", 400, 2)],
    3: [Meds("Propital Syringe", 150, 1)]
    # предмет
},
    "weapon": {
        1: [Weapon("Simple Handmade Rifle", 5, 40, 0, 30, 35),
            Weapon("Simple Axe", 30, 30, 0, 7, 60),
            Weapon("Lock18", 15, 20, 0, 40, 50),
            Weapon("MagickStick3000", 5, 0, 27, 25, 40),
            Weapon("Bayonet", 10, 40, 0, 5, 90)],
        2: [Weapon("Handmade Assault Rifle", 20, 50, 0, 80, 60),
            Weapon("Enchanted Magic Stick", 10, 0, 40, 40, 50)],
        3: [Weapon("Old Magic Book", 15, 5, 35, 30, 70),
            Weapon("M249 LMG", 50, 40, 0, 70, 70),
            Weapon("Bolt Action Rifle", 7, 80, 0, 100, 95),
            Weapon("L3 Sniper Rifle", 5, 95, 0, 120, 100)],
        "armor": {
            1: [Armor("Burlap Clothes", 10, 5),
                Armor("Old Cape", 5, 15)],
            2: [Armor("Nice Set Of Clothes", 20, 10),
                Armor("Enchanted Magic Clothes", 7, 20),
                Armor("Roadsign Armor Set", 35, 10),
                Armor("Wizard Clothes", 15, 35),
                Armor("Anti-Radiation Suit", 30, 30)],
            3: [Armor("High Quality Metal Gear", 50, 15),
                Armor("Military Grade Armor", 60, 15),
                Armor("Enchanted Old Wizard's Set", 20, 50)]
        }

    }
}

case_types = {
    'meds': {
        1: "Car First Aid Kit",
        2: "Survival Kit",
        3: "Military First Aid Kit"
    },
    'weapons': {
        1: "Ящик с простым оружием",
        2: "Ящик с оружием среднего качества",
        3: "Ящик с элитным оружием"
    },
    'armor': {
        1: "Коробка с простой одеждой",
        2: "Коробка с защитной экипировкой",
        3: "Коробка с продвинутой бронёй"
    }}


def Events(character, currentEnemy):
    events = ["Trader", "Fight", "CrateFound", "NothingHappened"]
    eventchance = [13, 60, 7, 20]
    eventchoice = random.choices(events, weights=eventchance)[0]
    if eventchoice == "Trader":
        pass
    elif eventchoice == "Fight":
        LutiyFight(character, currentEnemy)
        return True
    elif eventchoice == "CrateFound":
        print("потом напишу")
        CaseOpen(character)
        return True
    elif eventchoice == "NothingHappened":
        print("Вы шли довольно долго не найдя абсолютно ничего и решили передохнуть.")
        print("Персонаж отдыхает", end="")
        for i in range(6):
            time.sleep(0.3)
            print(".", end="")
        print()
        return True
    return False


def Main():
    print("Добро пожаловать в .")
    input("Нажмите ENTER чтобы начать.")
    gameName = input("Придумайте имя вашего персонажа ")
    player1 = Character(gameName, 100, "Кулаки", 5, 5, 1, 1,0)
    print(f"{player1.name} создан.")
    print(
        f"Имя персонажа: {player1.name}.\nЗдоровье персонажа: {player1.hp}.\nОружие персонажа: {player1.gun},\nСкорость персонажа: {player1.speed}.\nУрон персонажа: {player1.damage}.\n Дальность оружия персонажа: {player1.fRange}.\nТочность персонажа: {player1.gAccuracy}.\nОпыта до 2го уровня нужно: {player1.remainingXp}.")
    # Попробовать добавить меню действий и ивенты
    while player1.hp > 0:
        print("Нажмите 1 для того чтобы осмотреться.\nНажмите 2 для открытия инвентаря.")
        menuChoice = int(input())
        if menuChoice == 1:
            print("Осмотревшись вы обнаружили себя в густом, болотистом лесу. Вы решили пройти дальше.")
            currentEnemyM = Enemy.ChoiceEnemy(player1.cLvl)
            print(Events(player1,currentEnemyM))
#добавить больше кнопок для выбора, дописать инвентарь создав список в персонаже и напимать функцию которая этот список показывает при помощи цикла for и  обращения к конкретным атрибутам
Main()