class Player :
  count = 0
  def __init__(self, name):
    Player.count += 1
    self.name = name
    print(self.name,'이 팀에 합류했습니다.')
    
  def __del__(self):
    Player.count -= 1
    print(self.name,'이 팀을 떠났습니다.')
  
  @classmethod
  def how_many(cls):
    return cls.count
  
  @staticmethod
  def pay(name, present_pay, changed):
    print("%s의 내년도 연봉은 %d 입니다." %(name, present_pay + changed))

class Hitter(Player):
  def __init__(self, name, batting_average):
    super().__init__(name)
    self.batting_average = batting_average
  
  def is_he_good(self):
    if self.batting_average >= 0.3 :
      print(self.name,' is good hitter.')
    else :
      print(self.name,' needs more practice')

class Pitcher(Player):
   def __init__(self, name, era):
    super().__init__(name)
    self.era = era

   def is_he_good(self):
    if self.era <= 3 :
      print(self.name,' is good pitcher.')
    else :
      print(self.name,' needs more practice')

p1 = Hitter('허경민', 0.334)
p2 = Hitter('페르난데스', 0.343)
p3 = Hitter('정수빈', 0.293)
p4 = Pitcher('알칸타라', 2.67)
p5 = Pitcher('이영하', 5.44)
p6 = Pitcher('유희관', 4.37)

team = [p1, p2, p3, p4, p5, p6]

for member in team:
  member.is_he_good()

Player.how_many()

