import random
import skill

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