import math
from typing import Self


class Vector:
    def __init__(self, x: float, y: float):
        # _x, _y son atributos privados.
        self.__x: float = x
        self.__y: float = y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def mod(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __le__(self, other: Self) -> bool:
        return self.mod <= other.mod

    def __hash__(self):
        return hash((self.x, self.y, 1))

    def __add__(self, other: Self) -> Self:
        """
        Suma de vectores
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        """
        Resta de vectores
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self) -> Self:
        """
        Vector inverso
        """
        return Vector(-self.x, -self.y)

    def __rmul__(self, other: float) -> Self:
        """
        Producto de escalar (real) por vector
        """
        return Vector(other * self.x, other * self.y)

    def __mul__(self, other: Self) -> float:
        """
        Producto escalar de vectores
        """
        return self.x * other.x + self.y * other.y

    def __repr__(self) -> str:
        return f'V({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'({self.x:.4f}, {self.y:.4f})'


class Point:
    def __init__(self, x: float, y: float):
        # _x, _y son atributos privados.
        self.__x: float = x
        self.__y: float = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    def __repr__(self):
        return f"Point with x = {self.x} and y = {self.y}"

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __sub__(self, other: Self) -> Vector:
        if type(other) is not Point:
            raise TypeError(f"{other} is not type of Point")
        return Vector(other.x - self.x, other.y - self.y)

    def distance(self, other: Self) -> float:
        return self.__sub__(other).mod

