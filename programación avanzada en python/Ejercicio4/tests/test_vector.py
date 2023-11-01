import pytest
from ..geom2d import Vector


@pytest.mark.parametrize("obj, expected", [
    (Vector(1, 2), "(1.0000, 2.0000)")
])
def test_vector_str(obj, expected):
    assert str(obj) == expected


@pytest.mark.parametrize("obj, expected", [
    (Vector(1, 2), "V(1, 2)")
])
def test_vector_repr(obj, expected):
    assert repr(obj) == expected


@pytest.mark.parametrize("obj, expected", [
    (Vector(3, 4), 5)
])
def test_mod(obj, expected):
    assert obj.mod == expected


def test_equal():
    assert Vector(1.0, 2) == Vector(1, 2.0)


def test_le():
    assert Vector(3, 4) <= Vector(4, 5)


def test_add():
    assert (Vector(1, 2) + Vector(3, 4)) == Vector(4, 6)


def test_sub():
    assert (Vector(5, 3) - Vector(1, 1) == Vector(4, 2))


def test_neg():
    assert (-Vector(2, 5)) == Vector(-2, -5)


def test_rmul():
    assert (3 * Vector(3, 2)) == Vector(9, 6)


def test_mul():
    assert (Vector(2, 3) * Vector(2, 2)) == 10
