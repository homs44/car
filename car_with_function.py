
d_up = 1
d_down = 2
d_left = 3
d_right = 4

car = {
    "x" : 0,
    "y" : 0
}

car2 = {
    "x": 0,
    "y": 1
}

 # 자동차 운전
def drive(direction):
    if direction == d_up:
        car["y"] = car["y"] + 1
    elif direction == d_down:
        car["y"] = car["y"] - 1
    elif direction == d_left:
        car["x"] = car["x"] - 1
    elif direction == d_right:
        car["x"] = car["x"] + 1
    else:
        print("잘못된 방향입니다.")

# 자동차 좌표 출력
def printLocation():
    print("자동차의 위치는 : {0}, {1}".format(car["x"], car["y"]))



 # 자동차2 운전
def drive2(direction):
    if direction == d_up:
        car2["y"] = car2["y"] + 1
    elif direction == d_down:
        car2["y"] = car2["y"] - 1
    elif direction == d_left:
        car2["x"] = car2["x"] - 1
    elif direction == d_right:
        car2["x"] = car2["x"] + 1
    else:
        print("잘못된 방향입니다.")

# 자동차2 좌표 출력
def printLocation2():
    print("자동차2의 위치는 : {0}, {1}".format(car2["x"], car2["y"]))



printLocation()

drive(d_up)
printLocation()

drive(d_up)
printLocation()

drive(d_right)
printLocation()

drive(d_down)
printLocation()

printLocation2()

drive2(d_up)

printLocation2()