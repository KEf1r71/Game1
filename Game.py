import random
class Character:
    def __init__(self,name,hp,gun,speed,damage):
        self.name=name
        self.hp=hp
        self.gun=gun
        self.speed=speed
        self.damage=damage
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
