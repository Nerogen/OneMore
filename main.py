from math import factorial, sqrt


def first(nums: list[int]) -> list[int]:
    """ Set contain only unic elements """
    return list(set(nums))


def wilson_for_simple_numbers(left: int, right: int) -> list[int]:
    """ Wilson's theory: p is a simple number if p > 1 and (p - 1)! - 1 % p == 0"""
    return [num for num in range(left, right + 1) if num > 1 and (factorial(num - 1) + 1) % num == 0]


class Point:
    def __init__(self):
        self._x = None
        self._y = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y: int):
        self._y = y

    def distance(self, x: int, y: int) -> float:
        """ distance between two points is sqrt from (x2-x1)^2 + (y2-y1)^2 """
        return sqrt((x - self._x) ** 2 + (y - self._y) ** 2)

    def __str__(self):
        return f"X: {self._x} | Y: {self._y}"


def sorting(strings: list[str]) -> list[str]:
    return sorted(strings, key=len)[::-1]


def main():
    print("First task", first([1, 1, 2, 2]))
    print("Second task", wilson_for_simple_numbers(1, 10))
    point = Point()
    point.x, point.y = 10, 20
    print(point)
    print(point.distance(12, 22))
    print("Sorting:", sorting(["1", "22", "4444", "333", "666666", "55555"]))


if __name__ == '__main__':
    main()
