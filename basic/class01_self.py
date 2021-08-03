#클래스 정의
class Car :
    def drive(self):
        self.speed = 60

#객체 생성
myCar = Car()

#객체 속성 설정
myCar.speed = 0
myCar.model = "E-Class"
myCar.color = "blue"
myCar.year = "2017"

#객체 속성 출력
print("자동차의 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)
print("자동차를 주행합니다.")

#메소드 호출
myCar.drive()
print("자동차의 속도는", myCar.speed)
