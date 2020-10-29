import random

class Hero:
  def __init__(self, name):
    self.name = name
    self.lev = 1
    self.hp = 100*self.lev

  def learn_skill(self):
    pass
    

  def get_stat(self):
    pass

class Monster:
  def __init__(self, lev):
    self.lev = int(lev)
    self.hp = lev*100
    self.damage = lev*21


class Warrior(Hero):
  def __init__(self, name):
    super().__init__(name)
    self.normal_attack_name = 'Sword Swing'
    self.normal_attack_damage = 20*self.lev
    self.basic_skill = Skill('Power Strike', 20, 20, 0.7, 1.3)

class Magician(Hero):
  def __init__(self, name):
    super().__init__(name)
    self.normal_attack_name = 'Wand Swing'
    self.normal_attack_damage = 10*self.lev
    self.basic_skill = Skill('Fire Ball', 18, 18, 0.5, 2)
    
    ##Warrior랑 Magician이랑 들고있는 속성이 비슷하기 때문에 Hero로 옮겨주고 생성할때 받는걸로 수정하는게 나을듯.


class Skill:
  def __init__(self, name, damage, lev_coefficient, low_boundary, high_boundary):
    self.name = name
    self.damage = float(damage)
    self.lev_coefficient = lev_coefficient
    self.low_boundary = low_boundary
    self.high_boundary = high_boundary
    self.lev = 1
  
  def set_name(self, new_name):
    self.name = new_name
  
  def set_damage(self, new_damage):
    self.damage = float(new_damage)
  
  ##나머지 속성들도 setter 만들 예정.

  
  def train_skill(self, hero_instance):
    if self.lev >= hero_instance.lev :
      print("레벨을 더 올리고 오세요.")
    else :
      self.lev += 1
      self.damage += self.lev_coefficient
      print("{0} 훈련이 완료되었습니다. 스킬 데미지는 {1}입니다.".format(self.name, self.damage))
  
  ##어떤 스킬 훈련할건지도 입력 받게 수정 예정
  
  def actual_damage(self):
    return self.damage*random.uniform(self.low_boundary, self.high_boundary) 



def normal_fight(hero):
    monster_lev = int(input('몇 레벨의 몬스터와 전투하시겠습니까? : '))
    monster = Monster(monster_lev)

    while monster.hp > 0 :
      if hero.hp <=0 :
        print("{}는 전투 중 사망하였습니다. 낮은 레벨의 몬스터를 상대하세요".format(hero.name))
        break

      else:
        action = int(input("어떻게 공격하시겠습니까? 1.일반공격 2.스킬(숫자로 선택해주세요) : "))
        if action == 1 :
          monster.hp -= hero.normal_attack_damage
          print("{0}로 공격하여 {1}데미지를 주었습니다. 몬스터의 체력은 {2}입니다.".format(hero.normal_attack_name, hero.normal_attack_damage, monster.hp))
          hero.hp -= monster.damage
          print('몬스터에게 {0} 데미지로 공격받았습니다. 남은 {1}의 체력은 {2}입니다.'.format(monster.damage, hero.name, hero.hp))


        elif action == 2:
          monster.hp -= int(hero.basic_skill.actual_damage())
          print("{0}로 공격하여 {1}데미지를 주었습니다. 몬스터의 체력이 {2}남았습니다.".format(hero.basic_skill.name, int(hero.basic_skill.actual_damage()), monster.hp))
          hero.hp -= monster.damage
          print('몬스터에게 {0} 데미지로 공격받았습니다. 남은 {1}의 체력은 {2}입니다.'.format(monster.damage, hero.name, hero.hp))
        else :
          print("할 수 없는 행동입니다.")
    
    if monster.hp <=0 :
      hero.lev += 1
      hero.hp = 100*hero.lev
      print('전투에서 승리하였습니다! 축하합니다. {0}의 레벨이 {1}이 되었습니다.'.format(hero.name, hero.lev))

def boss_fight(hero):
    pass


if __name__ == '__main__':
  w1 = Warrior('gyugyu')
  normal_fight(w1)
  w1.basic_skill.train_skill(w1)
  w1.basic_skill.train_skill(w1)
















