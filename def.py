import sys

health = 100
health_evil = 100
password = "123456"


def show_health_evil(hp_ev):
    print("Здоровье врага:", hp_ev)


def show_health(hp):
    print("Здоровье:", hp)


def death(hp):
    show_health(hp)
    print("Вы погибли, игра окончена.")
    sys.exit()


def attack(hp_ev, damage):
    return max(0, hp_ev - damage)


def death_evil(hp_ev):
    if hp_ev <= 0:
        print("Вы убили тролля и выиграли!")
        sys.exit()


def damage_pl(hp, damage):
    return max(0, hp - damage)


print("Вы вошли в замок.")
print("Вы оглянулись.")
print("Справа — темный коридор, впереди — большая лестница, слева — дверь.")

while True:
    startCh = input("Куда пойти? 1) налево 2) направо 3) вперед: ").strip()

    if startCh == "1":
        print("Вы подергали за ручку. Дверь закрыта.")

    elif startCh == "2":
        print("Вы вошли в темноту. Там были летучие мыши с острыми, как лезвия, крыльями. Улетев, они порезали вас. -10 хп")
        health = damage_pl(health, 10)
        show_health(health)

        if health <= 0:
            death(health)
        print("Вы нашли бумажку с надписью: 'Пароль: 123456'")

    elif startCh == "3":
        break
    
    else:
        print("Введите 1, 2 или 3.")

print("Поднявшись по лестнице, вы увидели свое отражение. Вы попали в зеркальный лабиринт. Дверь захлопнулась. Вы можете пойти во все стороны.")

while True:
    stairs = input("Куда? 1) налево 2) направо 3) вперед: ").strip()

    if stairs == "1":
        print("Вы врезались в стекло.")

    elif stairs == "2":
        print("Вы прошли и наткнулись на тролля.")
        show_health_evil(health_evil)
        break
    
    elif stairs == "3":
        print("Вы прошли вперед и нашли дверь с кодовым замком.")

        while True:
            entered_password = input("Введите пароль или 0, чтобы вернуться: ").strip()

            if entered_password == "0":
                print("Вы вернулись в зеркальный лабиринт.")
                break
            
            elif entered_password == password:
                print("Пароль верный! Замок щелкнул, и дверь открылась.")
                print("За дверью оказался выход из замка. Вы выбрались и выиграли!")
                sys.exit()
                
            else:
                print("Неверный пароль. Дверь осталась закрытой.")

    else:
        print("Введите 1, 2 или 3.")

while True:
    fight_start = input("1 — Убежать, 2 — Ударить: ").strip()

    if fight_start == "1":
        print("Тролль догнал вас и убил ударом по голове.")
        health = damage_pl(health, health)
        death(health)

    elif fight_start == "2":
        health_evil = attack(health_evil, 10)
        print("Вы ударили тролля и нанесли ему 10 урона.")
        show_health_evil(health_evil)
        death_evil(health_evil)
        break
    
    else:
        print("Введите 1 или 2.")

while True:
    fight = input("1 — Продолжить бой, 2 — Убежать: ").strip()

    if fight == "1":
        health_evil = attack(health_evil, 10)
        print("Вы ударили тролля и нанесли ему 10 урона.")
        show_health_evil(health_evil)
        death_evil(health_evil)

    elif fight == "2":
        print("Тролль догнал вас и убил ударом по голове.")
        health = damage_pl(health, health)
        death(health)

    else:
        print("Введите 1 или 2.")
               

         

