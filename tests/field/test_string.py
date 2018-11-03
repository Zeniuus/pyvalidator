import pytest

from pyvalidator import field


def test_string_type():
    spec = field.String()

    assert spec.validate_field('test-string')

    assert spec.validate_field('')

    with pytest.raises(AssertionError):
        spec.validate_field(None)

    with pytest.raises(AssertionError):
        spec.validate_field(3)


def test_string_nullable():
    spec = field.String(nullable=True)

    assert spec.validate_field(None)


def test_string_not_empty():
    spec = field.String(empty=False)

    with pytest.raises(AssertionError):
        assert spec.validate_field('')


def test_string_length():
    spec = field.String(length=10)

    spec.validate_field('')

    spec.validate_field('short-str')

    spec.validate_field('len-10-str')

    with pytest.raises(AssertionError):
        spec.validate_field('some-long-string')


def test_string_except_pattern():
    spec = field.String(except_pattern='lo')

    spec.validate_field('Hi, world!')

    with pytest.raises(AssertionError):
        spec.validate_field('Hello, world!')

    spec = field.String(except_pattern=r';.+DROP\s+TABLE')

    spec.validate_field('user-nickname')

    with pytest.raises(AssertionError):
        spec.validate_field('user-nickname; DROP TABLE user;')


def test_string_match_pattern():
    spec = field.String(match_pattern='lo')

    spec.validate_field('Hello, world!')

    with pytest.raises(AssertionError):
        spec.validate_field('Hi, world!')

    spec = field.String(match_pattern=r'Bearer .+\..+\..+')

    spec.validate_field('Bearer some.jwt.token')

    with pytest.raises(AssertionError):
        spec.validate_field('Bearer Wrong auth header')
