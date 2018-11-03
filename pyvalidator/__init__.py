__version__ = '1.0.0'


def validate_field(field, spec):
    try:
        return spec.validate_field(field)
    except AssertionError as e:
        raise InvalidInputError(f'{field} {e}')


def validate(body, spec):
    assert isinstance(spec, dict), \
        'Specification should be dict type!'
    for field_name, field_spec in spec.items():
        validate_field(body.get(field_name, None), field_spec)
    return True


class InvalidInputError(Exception):
    pass
