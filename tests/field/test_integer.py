import pytest

from pyvalidator import field


def test_integer_type():
    spec = field.Integer()

    assert spec.validate_field(3)

    assert spec.validate_field(3)
    assert spec.validate_field('3')

    assert spec.validate_field(0)
    assert spec.validate_field('0')

    assert spec.validate_field(-3)
    assert spec.validate_field('-3')

    with pytest.raises(AssertionError):
        spec.validate_field('haha')

    with pytest.raises(AssertionError):
        spec.validate_field('3.3')

    with pytest.raises(AssertionError):
        spec.validate_field(None)


def test_integer_nullable():
    spec = field.Integer(nullable=True)

    assert spec.validate_field(None)


def test_integer_positive():
    spec = field.Integer(positive=True)

    assert spec.validate_field(3)

    with pytest.raises(AssertionError):
        spec.validate_field(0)
    with pytest.raises(AssertionError):
        spec.validate_field('0')

    with pytest.raises(AssertionError):
        spec.validate_field(-3)
    with pytest.raises(AssertionError):
        spec.validate_field('-3')


def test_integer_nonnegative():
    spec = field.Integer(nonnegative=True)

    assert spec.validate_field(3)

    assert spec.validate_field(0)
    assert spec.validate_field('0')

    with pytest.raises(AssertionError):
        spec.validate_field(-3)
    with pytest.raises(AssertionError):
        spec.validate_field('-3')


def test_integer_min():
    spec = field.Integer(min=3)

    assert spec.validate_field(3)
    assert spec.validate_field('3')

    assert spec.validate_field(6)
    assert spec.validate_field('6')

    with pytest.raises(AssertionError):
        spec.validate_field(2)
    with pytest.raises(AssertionError):
        spec.validate_field('2')

    with pytest.raises(AssertionError):
        spec.validate_field(0)
    with pytest.raises(AssertionError):
        spec.validate_field('0')


def test_integer_max():
    spec = field.Integer(max=3)

    assert spec.validate_field(3)
    assert spec.validate_field('3')

    assert spec.validate_field(2)
    assert spec.validate_field('2')

    with pytest.raises(AssertionError):
        spec.validate_field(6)
    with pytest.raises(AssertionError):
        spec.validate_field('6')

    assert spec.validate_field(0)
    assert spec.validate_field('0')
