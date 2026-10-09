health = 100
health_evil = 100



def show_health_evil(health_evil):
     print ("Здоровье врага: ", health_evil)

def show_health(health):
     print("Здоровье: ", health)

def death(helth):
     health = health - 100
     while True:
          print("Игра окончена")
          break

def attack(health_evil):
     health_evil = health_evil - 10

def death_evil(health_evil):
    while health_evil <= 0:
     print("Вы убили тролля и выйграли!")
     break

def damage_pl(health, damage):
    return health - damage

if health_evil == 0:
     death_evil  

elif health == 0:
     death
     
print("Вы вошли в замок.")
print("Вы оглянулись.")
print("Справа - темный коридор, впереди - большая лестница, слева - дверь.")
while True:
          startCh = int(input("Куда пойти? 1)налево 2)направо 3)вперед "))

          if startCh == 1:
               print("Вы подергали за ручку. Дверь закрыта.")
               continue
    
          elif startCh == 2:
               print("Вы вошли в темноту. Там были летучие мыши с острыми, как лезвия, крыльями. Улетев, они порезали вас. -10хп")
               damage = 10
               health = damage_pl(health, damage)
               show_health(health)
               continue
          break
while True:

          if startCh == 3:
               print("Поднявшись по лестнице, вы увидели свое отражение. Вы попали в зеркальный лабиринт. Дверь захлопнулась. Вы можете пойти во все стороны. ")
               stairs = int(input("Куда? 1)налево 2)направо 3)вперед"))
                   


          if stairs == 1:
             print("Вы врезались в стекло")
             continue
     
          elif stairs == 2:
               print("Вы прошли и наткнулись на тролля")
               show_health_evil
          fight_start = int(input("1 - Убежать, 2 - Ударить "))

          if(fight_start == 1):
               print("Тролль догнал вас и шотнул ударом по голове")
               death

          elif (fight_start == 2):
                attack
                print("Вы ударили тролля и нанесли ему 10хп")
                show_health_evil
          fight = int(input("Если хотите продолжать бой, продолжайте нажимать на цифру 1, в другом случае, нажмите 2"))
          if (fight == 1):
               while fight == 1:
                    attack
                    show_health_evil
          elif fight == 2:
               print("Тролль догнал вас и шотнул ударом по голове")
               damage = 100
               damage_pl
               

         

