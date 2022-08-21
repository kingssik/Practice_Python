# 문제 : 자동차 객체를 담을 변수를 만들어주세요.
# 자동차 객체를 변수에 담고 그 변수를 이용해 최고속력이 서로 다르게 만들어주세요.

# 각 자동차가 자신의 최고속력으로 달리게 해주세요.
class Car:
    maxVel = 0
    def drive(self):
        print('자동차가 최대속력 {}로 달립니다.'.format(self.maxVel))

# 출력 : 자동차가 최대속력 220km로 달립니다.
c1 = Car()
c1.maxVel = 220
c1.drive()
# 출력 : 자동차가 최대속력 250km로 달립니다.
c1 = Car()
c1.maxVel = 220
c1.drive()