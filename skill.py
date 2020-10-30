import random

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