
# 계산기 클래스 만들기
# 더하기
# 빼기
# 곱하기
# 나누기
# 현재 값 출력

# 초기값은 0

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result = self.result + num

    def subtract(self, num):
        self.result = self.result - num

    def divide(self, num):
        self.result = self.result / num

    def multiply(self, num):
        self.result = self.result * num

    def printResult(self):
        print(self.result)

myCalculator = Calculator()

myCalculator.add(5) # 더하기

myCalculator.subtract(3) # 빼기

myCalculator.multiply(5) # 곱하기

myCalculator.divide(10) # 나누기

myCalculator.printResult() #현재 값이 출력

XCalculator = Calculator()

XCalculator.add(5)

XCalculator.subtract(20)

XCalculator.printResult()
