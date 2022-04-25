import math


class Math:

    def circle_len(self, radius):
        result = (radius * 2) * math.pi
        return result

    def circle_sq(self, radius):
        result = (radius ** 2) * math.pi
        return result

    def cube_V(self, edge):
        result = edge ** 3
        return result

    def sphere_S_area(self, radius):
        result = (4 * math.pi) * (radius ** 2)
        return result


MyMath = Math()
res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_V(edge=12)
res_4 = MyMath.sphere_S_area(radius=6)
print(res_1)
print(res_2)
print(res_3)
print(res_4)

# зачтено
