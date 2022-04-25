import math


class Circle:

    def __init__(self, x=0, y=0, r=1.0):
        self.x = x
        self.y = y
        self.r = r

    def check_S(self):
        check_S = math.pi * (self.r ** 2)
        print("Площадь окружности равна {}".format(check_S))
        return check_S

    def check_P(self):
        check_P = self.r * (math.pi * 2)
        print("Периметр окружности равен {}".format(check_P))
        return check_P

    def get_big(self, k):
        self.r *= math.sqrt(k)
        print("Окружность увеличена в {} раз".format(k))

    def check_intersect(self, circle):
        x3 = circle.x
        y3 = self.y
        hypot = math.hypot(abs(self.x - x3), abs(circle.y - y3))
        if hypot <= (self.r + circle.r):
            print("Окружности пересекаются.")
            return True
        else:
            print("Окружности не пересекаются.")
            return False


circle_1 = Circle(3, -4, 2)
circle_2 = Circle(-3, -2, 2.5)
circle_2.check_S()
circle_2.check_P()
circle_1.check_intersect(circle_2)
circle_2.check_intersect(circle_1)
circle_2.get_big(4)
circle_1.check_intersect(circle_2)
circle_2.check_intersect(circle_1)
circle_2.check_S()
circle_2.check_P()

# зачтено
