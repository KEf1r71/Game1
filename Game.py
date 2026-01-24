import random
class Character:
    def __init__(self,name,hp,gun,speed,damage,fRange,gAccuracy,cArmor,cPhysDef,cMgcDef,cLvl,currentXp,remainingXp,talent,):
        self.name=name
        self.hp=100
        self.gun=gun
        self.speed=30
        self.damage=10
        self.fRange=5
        self.gAccuracy=10
        self.cArmor=cArmor
        self.cPhysDef=cPhysDef
        self.cMgcDef=cMgcDef
        self.cLvl=cLvl
        self.currentXp=currentXp
        self.remainingXp=100
        self.talent=5
        self.slot=False
        self.armorSlot=False
        self.cAttackPoints=1
        self.cActionPoints=2
    #создать дефолтного дебильчика с базовыми статами и выдать ему какое нибудь изначальное оружие
    def talentUse(self):
        if self.talent<=0:
            print("У вас нет очков таланта")
            return False
        else:
            while self.talent>0:
                print(f"У вас есть {self.talent} очков таланта")
                print("Нажмите 1 чтобы прокачать здоровье")
                print("Нажмите 2 чтобы прокачать скорость")
                print("Нажмите 3 чтобы прокачать урон")
                print("Нажмите 4 чтобы прокачать точность")
                print("Нажмите 5 чтобы посмотреть свою статистику. ")
                print("Нажмите 6 чтобы выйти из меню прокачки. ")
                tUp=int(input("выберите навык для прокачки "))
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
        print(f"Нужно опыта до следующего уровня:{self.remainingXp-self.currentXp} ")
    def lvlGet(self,xpGave):
        self.currentXp+=xpGave
        print(f"Вы получили {xpGave} опыта ")
        lvlGive=0
        while self.currentXp>self.remainingXp:
            self.talent+=1
            self.lvlUp()
            lvlGive+=1
            self.currentXp-=100
        print(f"Получено {lvlGive} уровней, у вас остались нераспределенные очки талантов: {self.talent} ")
    def lvlUp(self):
        self.cLvl+=1
        print(f"У тебя теперь {self.cLvl} уровень. ")
        print(f"У тебя осталось {self.talent} очков талантов, готовых к распределению. ")
        print(f"До следующего уровня осталось {self.remainingXp-self.currentXp}")
name,hp,gun,speed,damage=None,None,None,None,None
def Function():
    global name,hp,gun,speed,damage,A
    try:
        if name==None:
            name=input("введите имя класса ")
        if hp==None:
            hp=int(input("введите здоровье класса "))
        if gun==None:
            gun=input("введите оружие класса ")
        if speed==None:
            speed=int(input("введите скорость класса "))
        if damage==None:
            damage=int(input("введите урон класса "))
        A=Character(name,hp,gun,speed,damage)
        print(A.name,A.hp,A.gun,A.speed,A.damage)
    except ValueError:
        print("это должно быть написано цифрами, переделывай ")
        Function()
Function()
class Armor:
    def __init__(self,name,pDefence,mDefence,character=None):
        self.name=name
        self.pDefence=pDefence
        self.mDefence=mDefence
    def take(self, character):
        character.armorSlot=True
        character.PhysDefence+=self.pDefence
        character.cMgcDefence+=self.mDefence
    def drop(self, character):
        character.armorSlot=False
        character.PhysDefence-=self.pDefence
        character.cMgcDefence-=self.mDefence
class Weapon:
    def __init__(self,name,fireRate, physDmg, magicDmg,range,accuracy):
        self.name=name
        self.fireRate=fireRate
        self.physDmg=physDmg
        self.magicDmg=magicDmg
        self.range=range
        self.accuracy=accuracy
    def take(self,character):
        character.slot=True
        character.damage+=self.physDmg+self.magicDmg
        character.speed+=self.fireRate
        character.fRange+=self.range
        character.gAccuracy+=self.accuracy
    def drop(self,character):
        character.slot=False
        character.damage-=self.physDmg+self.magicDmg
        character.speed-=self.fireRate
        character.fRange-=self.range
        character.gAccuracy-=self.accuracy
class Enemy:
    def __init__(self,name,hp,gun,physDmg,mgcDmg,fRange,gAccuracy,cArmor,cPhysDef,cMgcDef,giveXp,lvl):
        self.name=name
        self.hp=hp
        self.gun=gun
        self.physDmg=physDmg
        self.mgcDmg=mgcDmg
        self.fRange=fRange
        self.gAccuracy=gAccuracy
        self.cArmor=cArmor
        self.cPhysDef=cPhysDef
        self.cMgcDef=cMgcDef
        self.giveXp=giveXp
        self.lvl=lvl
    def ChoiceEnemy(self,cLvl):
        if cLvl<=50:
            eLvl=max(1,cLvl+random.choice(-5,5))
        elif 50<cLvl<=100:
            eLvl = max(1, cLvl + random.choice(-5, 10))
        elif 100<cLvl<=200:
            eLvl = max(1, cLvl + random.choice(-10, 20))
        else:
            eLvl = max(1, cLvl + random.choice(-20, 40))
        avaliableEnemy=[]
        for i in enemy:
            if abs(i.lvl-eLvl)<=5:
                avaliableEnemy.append(i)
Enemy.CreateEnemy()

#добавить возможность подбежать к врагу
def HitChance(character,enemy,distance):
    BaseAccuracy=character.gAccuracy
    dRange=character.fRange-distance
    if dRange>=0:
#порезка урона
        damageP=0
    else:
        damageP=abs(dRange)
    finalHitChance=BaseAccuracy-damageP+character.speed
    return max(15,min(100,finalHitChance))


def LutiyFight(character,currentEnemy):
    meet=[f"Вы встретились с {currentEnemy.name}. Как он вообще тут оказался?...",
          f"Вы заметили {currentEnemy.name}. Не думаю, что он пойдет на контакт."]
    print(random.choice(meet))
    print(f"У этого противника {currentEnemy.hp}.")
    distance=random.randint(1,100)
    print(f"Враг в {distance} метрах от вас.")

    while character.hp>0 and currentEnemy.hp>0:
        attackPoints=character.cAttackPoints
        actionPoints=character.cActionPoints
        print("Нажмите 1 для атаки.\nНажмите 2 для побега. \nНажмите 3 для приближения к врагу. \nНажмите 4 для отдаления от врага. \nНажмите 5 для принятия медикаментов.")
        print(f"вам доступно {character.cActionPoints} очков действий и {character.cAttackpoints} очков атаки")
        battleChoice=int(input())

        while attackPoints>0 or actionPoints>0:
            if battleChoice==1:
                if attackPoints<=0:
                    print("У вас недостаточно очков аттаки")
                    continue
                attackPoints-=1
                hitChance = HitChance(character, currentEnemy, distance)
                print(f"Шанс попадания {hitChance}.(Удалить) ")
                if random.randint(1, 100) <= hitChance:
                    damage = character.damage
                    currentEnemy.hp -= damage
                    print(f"Вы Нанесли {damage} урона.")
                    if currentEnemy.hp <= 0:
                        print(f"Вы поразили {currentEnemy.name}.")
                        character.lvlGet(currentEnemy.giveXp)
                else:
                    print("Вы промахнулись")

            if battleChoice==2:
                if actionPoints<=0:
                    print("У вас недостаточно очков действия")
                    continue

                runawayChance = character.speed / 10
                runaway = random.random()
                if runaway <= runawayChance:
                    break
                else:
                    print("Вам не удалось сбежать.")
                    continue
            if battleChoice==3:
                if actionPoints<=0:
                    print("У вас недостаточно очков действия")
                    continue
                actionPoints-=1
                runDistance = character.speed * 5
                distance -= runDistance
                print(f"Вы пробежали {runDistance} метров к врагу.")
                continue
            if battleChoice==4:
                if actionPoints<=0:
                    print("У вас недостаточно очков действия")
                    continue
                actionPoints-=1
                runawayDistance = character.speed * 5
                distance += runawayDistance
                print(f"Вы пробежали {runDistance} метров от врага.")
                continue
            if battleChoice==5:
                if actionPoints<=0:
                    print("У вас недостаточно очков действия")
                    continue
                actionPoints-=1








        if battleChoice==1:
            hitChance=HitChance(character,currentEnemy,distance)
            print(f"Шанс попадания {hitChance}.(Удалить) ")
            if random.randint(1,100)<=hitChance:
                damage=character.damage
                currentEnemy.hp-=damage
                print(f"Вы Нанесли {damage} урона.")
                if currentEnemy.hp<=0:
                    print(f"Вы поразили {currentEnemy.name}.")
                    character.lvlGet(currentEnemy.giveXp)
            else:
                print("Вы промахнулись")
        if battleChoice==2:
            runawayChance=character.speed/10
            runaway=random.random()
            if runaway<=runawayChance:
                break
            else:
                print("Вам не удалось сбежать.")
                continue
        if battleChoice==3:
            runDistance=character.speed*5
            distance-=runDistance
            print(f"Вы пробежали {runDistance} метров к врагу.")
            continue
        if battleChoice==4:
            runawayDistance=character.speed*5
            distance+=runawayDistance
            print(f"Вы пробежали {runDistance} метров от врага.")
            continue
        if battleChoice==5:
            #И тут будет тоже, клянусь.
            continue
        if currentEnemy.hp>0:
            enemyHitChance=currentEnemy.gAccuracy - max(0, (distance - currentEnemy.fRange) // 10)
# Продумать алгоритм действий внутри битвы, для побега и динамической прокачки.
enemy=[Enemy("Goblin", 15, "Wooden Stick", 10, 5, 30, "Burlap Clothes", 5, 5, 2, 1),
       Enemy("Goblin With A Magic Stick", 20, "Magic(?) Stick", 15, 25, 20, "Burlap Clothes", 5, 5, 3, 3),
       Enemy("Goblin, Who Thinks He's A Warrior", 30, "Wooden Sword (Kind Of)", 20, 10, 30, "Poor Wooden Shield", 10, 5, 5, 5),
       Enemy("Skeleton", 25, "Stone Sword", 20, 13, 30, "Nothing...", 0, 0, 7, 10),
       Enemy("Skeleton Wizard", 25, "Magic Stick", 23, 25, 40, "Old Magic Cape", 10, 15, 10, 10),
       Enemy("A Guy With A Knife", 30, "Bayonet", 30, 5, 60, "Nice Set Of Clothes", 20, 10, 10, 15),
       Enemy("Beginner Wizard", 30, "A Spell Book (Over 100 Spells inside!)", 20, 25, 40, "Enchanted Clothes (Whole set for only 9.99!)", 5, 15, 13, 15),
       Enemy("Armed Bum", 30, "Handmade Sword", 40, 5, 20, "Coat", 10, 10, 20, 20),
       Enemy("FireArmed Bum", 30, "Poor Handmade Hammer Pistol", 30, 13, 25, "Coat", 10, 10, 22, 20),
       Enemy("Wolf", 50, "Teeth, I guess?", 40, 3, 50, "Nothing...", 5, 5, 30, 25),
       Enemy("An Alright Wizard", 30, "Magic Stick. A really simple one", 30, 35, 40, "Simple Enchanted Clothes", 15, 25, 25, 25),
       Enemy("Expirienced Armed Bum", 35, "Handmade Sword", 45, 7, 25, "Coat", 15, 10, 30, 30),
       Enemy("Goblin Wizard", 30, "Magic Stick 3000", 35, 40, 55, "Enchanted Set Of Clothes", 15, 20, 32, 30),
       Enemy("Zombie", 40, "Hands? Jaw?", 45, 3, 30, "Nice Set Of Clothes", 20, 15, 35, 35),
       Enemy("Bear", 50, "Paws", 40, 2, 40, "Nothing...", 0, 0, 40, 41),
       Enemy("Armed Guy", 50, "Lock18", 40, 50, 30, "Light Gear", 20, 10, 50, 50),
       Enemy("Armed Guy", 55, "Handmade SMG", 40, 50, 40, "Light Gear With Vest", 30, 10, 50, 50),
       Enemy("Armed Guy", 55, "Handmade Thompson", 55, 60, 50, "Roadsign Gear", 35, 10, 55, 55),]
armor=[Armor("Burlap Clothes",10,5),
       Armor("Old Cape",5,15),
       Armor("Nice Set Of Clothes",20,10),
       Armor("Enchanted Magic Clothes",7,20),
       Armor("Roadsign Armor Set",35,10),
       Armor("Wizard Clothes",15,35),
       Armor("High Quality Metal Gear",50,15),
       Armor("Military Grade Armor",60,15),
       Armor("Anti-Radiation Suit",30,30),
       Armor("Enchanted Old Wizard's Set",20,50),]
armory=[Weapon("Lock18",15,20,0,40,50),
        Weapon("MagickStick3000",5,0,27,25,40),
        Weapon("Bayonet",10,40,0,5,90),
        Weapon("Handmade Assault Rifle",20,50,0,80,60),
        Weapon("Military Grade Assault Rifle",35,40,0,90,65),
        Weapon("Enchanted Magic Stick",10,0,40,40,50),
        Weapon("Old Magic Book",15,5,35,30,70),
        Weapon("M249 LMG",50,40,0,70,70),
        Weapon("Bolt Action Rifle",7,80,0,100,95),
        Weapon("L3 Sniper Rifle",5,95,0,120,100)]
def Main():
