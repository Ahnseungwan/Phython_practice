class Unit:
    def __init__(self, name, hp):
        self.name = name # 멤버변수
        self.hp = hp
        
# 공격유닛
class AttackUnit(Unit): # 일반유닛 클래스를 상속 받아서 사용한다.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # unit으로 부터 상속을 받는다.
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

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50 ,16)
firebat1.attack("5시") 
# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)