import time

health = 100

def show_health(health):
     print("Здоровье: ", health)

for i in range(10, 0, -1):
    print(i)

print("Вы вошли в замок.")
print("Вы оглянулись.")
print("Справа - темный коридор, впереди - большая лестница, слева - дверь.")
startCh = input("Куда пойти? 1)налево 2)направо 3)вперед ")

if startCh == "1":
    for left in "Вы подергали за ручку. Дверь закрыта.":
        print(left, end="", flush = True)
        time.sleep(0.05)
        continue
    

elif  startCh == "2":
    for right in "Вы вошли в темноту. Там были летучие мыши с острыми, как лезвия, крыльями. Улетев, они порезали вас. -10хп":
            print(right, end="", flush=True)
            time.sleep(0.05)
            continue
    health = health - 10
    

elif startCh == "3":
    for arrow in "Поднявшись по лестнице, вы увидели свое отражение. Вы попали в зеркальный лабиринт. Дверь захлопнулась. Вы можете пойти во все стороны. ":
                print(arrow, end="", flush=True)
                time.sleep(0.05)

    stairs = input("Куда? 1)налево 2)направо 3)вперед")

    if stairs == "1":
        for starlef in "Вы врезались в стекло":
            print(starlef, end="", flush = True)
            time.sleep(0.05)
            continue

    elif  stairs == "2":
        for starri in "Вы прошли":
            print(starri, end="", flush=True)
            time.sleep(0.05)
            continue
        

    elif stairs == "3":
        for starr in "Вы прошли и нашли выход":
            print(arrow, end="", flush=True)
            time.sleep(0.05)
            break
    else:
        print("Я вас не понял.")
          
else:
    print("Я вас не понял.")



