class Unit:
    def __init__(self, name, hp, speed):
        self.name = name # 멤버변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
# 공격유닛
class AttackUnit(Unit): # 일반유닛 클래스를 상속 받아서 사용한다.
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # unit으로 부터 상속을 받는다.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃/ 탱크 등을 수송. 공격 불가

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)

 # 벌쳐 : 지상 유닛, 기동성이 좋음
 vulture = AttackUnit("별쳐", 80, 10, 20)

 # 배틀크루져 : 공중 유닛, 체력도 굉장히 좋음, 공격력ㄷ ㅗ좋음.
 battlecruiser = FlyableAttackUnit("배틀크루저", 500 , 25, 3)

 vulture.move("11시")
 battlecruiser.fly(battlecruiser.name, "9시")

