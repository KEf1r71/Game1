import random
class Character:
    def __init__(self,name,hp,gun,speed,damage,fRange,gAccuracy):
        self.name=name
        self.hp=hp
        self.gun=gun
        self.speed=speed
        self.damage=damage
        self.fRange=fRange
        self.gAccuracy=gAccuracy
        self.slot=False
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
    def __init__(self,name,hp,gun,speed,damage):
        self.name=name
        self.hp=hp
        self.gun=gun
        self.speed=speed
        self.damage=damage
    def CreateEnemy():
        global B
        EnemyName=random.choice(["БОТ Боб","Афанасий","Нагибатор2004","deepNagibator200"])
        EnemyFullName=("ТОЧНО РЕАЛЬНЫЙ ИГРОК "+EnemyName)
        EnemyHp=random.randint(75,500)
        EnemyGun=random.choice(["Лещ","Бутерброд","Флогистонатор","Дисциплинированное Взыскание"])
        EnemySpeed=random.randint(50,200)
        EnemyDamage=random.randint(40,100)
        B=Enemy(EnemyFullName,EnemyHp,EnemyGun,EnemySpeed,EnemyDamage)
        print("Имя противника:",B.name,"Хп противника:",B.hp,"Оружие противника:",B.gun,"Скорость противника:",B.speed,"Урон противника:",B.damage)
Enemy.CreateEnemy()
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
armory=[Weapon("Lock18",15,20,0,40,50),
        Weapon("MagickStick3000",5,0,27,25,40),
        Weapon("Bayonet",10,40,0,5,90)
        Weapon("Handmade Assault Rifle",20,50,0,80,60)
        Weapon("Military Grade Assault Rifle",35,40,0,90,65)
        Weapon("Enchanted Magic Stick",10,0,40,40,50)
        Weapon("Old Magic Book",15,5,35,30,70)
        Weapon("M259 LMG",50,40,0,70,70)
        Weapon("Bolt Action Rifle",7,80,0,100,95)
        Weapon("L3 Sniper Rifle",5,95,0,120,100)]
