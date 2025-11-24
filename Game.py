import random
class Character:
    def __init__(self,name,hp,gun,speed,damage,fRange,gAccuracy,cArmor,cPhysDef,cMgcDef,cLvl,currentXp,remainingXp,talent):
        self.name=name
        self.hp=hp
        self.gun=gun
        self.speed=speed
        self.damage=damage
        self.fRange=fRange
        self.gAccuracy=gAccuracy
        self.cArmor=cArmor
        self.cPhysDef=cPhysDef
        self.cMgcDef=cMgcDef
        self.cLvl=cLvl
        self.currentXp=currentXp
        self.remainingXp=100
        self.talent=0
        self.slot=False
        self.armorSlot=False
    def talentUse(self):
        if self.talent<=0:
            print("У вас нет очков таланта")
            return False
#Дописать функцию распределения очков таланта.
        print(f"У вас осталось {self.talent} очков таланта")
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
        print(f"До следующего уровня осталось {}")
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
    def __init__(self,name,pDefence,mDefence,character):
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
def LutiyFight(A,B):
    input("Нажмите Enter ")
    if B.speed<=A.speed:
        B.hp-=A.damage
        if B.hp<=0:
            print("Противник еще не повержен, и будет насмехаться над вами, пока вы не заплатите 49.99 на DLC ПОБЕДНАЯ АННИГИЛЯЦИЯ")
            return True
        if B.hp>0:
            print(B.hp,"Хп осталось у противника, НО! ЕСЛИ ВЫ КУПИТЕ DLC ПРЕВОСХОДСВО ЗА 69.99 ДО ПРОТИВНИК ПУДЕТ УМИРАТЬ ЗА ПЕРВЫЙ УДАР ОТ ДИЗМОРАЛИ.")
            A.hp-=B.damage
            if A.hp<=0:
                print("ПОМЕР")
                return True
            else:
                print("У тебя осталось",A.hp,"хп")
                LutiyFight(A,B)
    else:
        A.hp-=B.damage
        if A.hp<=0:
            print("ПОМЕР")
            return True
        if A.hp>0:
                print("У тебя осталось",A.hp,"хп")
                B.hp-=A.damage
                if B.hp<=0:
                    print("Противник еще не повержен, и будет насмехаться над вами, пока вы не заплатите 49.99 на DLC ПОБЕДНАЯ АННИГИЛЯЦИЯ")
                    return True
        if B.hp>0:
            print(B.hp,"Хп осталось у противника, НО! ЕСЛИ ВЫ КУПИТЕ DLC ПРЕВОСХОДСВО ЗА 69.99 ДО ПРОТИВНИК ПУДЕТ УМИРАТЬ ЗА ПЕРВЫЙ УДАР ОТ ДИЗМОРАЛИ.")
            LutiyFight(A,B)
LutiyFight(A,B)
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