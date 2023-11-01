import pytest
from ..geom2d import Point, Vector


@pytest.mark.parametrize("obj, expected", [
    (Point(1, 2), "Point (1, 2)")
])
def test_vector_str(obj, expected):
    assert str(obj) == expected


@pytest.mark.parametrize("obj, expected", [
    (Point(1, 2), "Point with x = 1 and y = 2")
])
def test_vector_repr(obj, expected):
    assert repr(obj) == expected


def test_equal():
    assert Point(1.0, 2) == Point(1, 2.0)


@pytest.mark.parametrize("a, b", [
    (Point(1, 2), 3)
])
def test_sub(a, b):
    with pytest.raises(TypeError):
        a - b


@pytest.mark.parametrize("a, b, c", [
    (Point(1, 1), Point(4, 5), Vector(3, 4))
])
def test_sub2(a, b, c):
    assert (a - b) == c


@pytest.mark.parametrize("a, b, c", [
    (Point(1, 1), Point(4, 5), 5)
])
def test_distance(a, b, c):
    assert a.distance(b) == c
