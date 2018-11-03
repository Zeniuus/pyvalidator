import pytest

from pyvalidator import (
    field, validate, validate_field, InvalidInputError)


def test_validate_field():
    spec = field.Integer()

    assert validate_field(3, spec)

    with pytest.raises(InvalidInputError):
        validate_field('some-wrong-input', spec)


def test_validate():
    validation_spec = {
        'username': field.String(length=32),
        'password': field.String(length=32),
        'age': field.Integer(positive=True),
        'description': field.String(nullable=True),
    }

    body = {
        'username': 'Suhwan Jee',
        'password': 'some password',
        'age': 23,
    }
    assert validate(body, validation_spec)

    wrong_body = {
        'password': 'some password',
        'age': 23,
    }
    with pytest.raises(InvalidInputError):
        validate(wrong_body, validation_spec)
