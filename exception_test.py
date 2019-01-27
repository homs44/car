"""

자동차 상하좌우로 움직였을때 위치 찍어보기.
함수로 구현
나중에 클래스로 변경할꺼에요 왜 클래스로 변경해야되는지 

"""

#Exception

def divide():
    num1 = None
    num2 = None
    result = None
    try:
        num1 = float(input("숫자1를 입력하세요 : "))
        num2 = float(input("숫자2를 입력하세요 : "))
        result = num1/num2
        print("나누기 결과는 {0}".format(result))
    except ValueError :
        print("숫자를 제대로 입력하세요")
    except ZeroDivisionError:
        print("0으로 나눌 수 업습니다.")
    except Exception: #모든 에러는 Exception 클래스를 상속받기때문에 ValueError와 ZeroDivisionError를 제외한 나머지 오류는 여기서 except한다.
        print("오류를 발생했습니다.") 
    finally:
        print("done")
    

divide()