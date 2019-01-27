
d_up = 1
d_down = 2
d_left = 3
d_right = 4


class Car:

    def __init__(self):
        self.x = 0
        self.y = 0
    
    def drive(self, direction):
        if direction == d_up:
            self.y = self.y + 1
        elif direction == d_down:
            self.y = self.y - 1
        elif direction == d_left:
            self.x = self.x - 1
        elif direction == d_right:
            self.x = self.x + 1
        else:
            print("잘못된 방향입니다.")

    def printLocation(self):
        print("자동차의 위치는 : {0}, {1}".format(self.x, self.y))



class K3(Car):
    # 오버라이딩 overriding
    def printLocation(self):
        print("K3의 위치는 : {0}, {1}".format(self.x, self.y))


car1 = K3()

car1.drive(d_up)

car1.printLocation()
