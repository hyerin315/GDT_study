class Car :
    def __init__(self, speed, color, model): #__init__()은 외부에서 전달되는 초기값들을 받을 수 있다
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self): #self는 현재 객체를 의미 (l value : ex. myCar)
        self.speed = 60

    def accel(self):
        self.speed += 10

myCar = Car(0, "blue", "E-class") #Car() : 생성자

print("자동차 객체를 생성하였습니다")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)
print("자동차의 주행합니다.")

myCar.drive() #객체의 메소드, drive()로는 실행안됨 - 이게 실행되려면 외부 함수 생성해줘야함 (ex. def drive())
print("자동차의 속도는", myCar.speed)