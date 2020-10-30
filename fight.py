import skill
import characters
import random

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