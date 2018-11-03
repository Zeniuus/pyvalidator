import re


class Validator:

    @staticmethod
    def v_positive(_):

        def _v_positive(field):
            assert field > 0, \
                f'is not positive.'

        return _v_positive

    @staticmethod
    def v_nonnegative(_):

        def _v_nonnegative(field):
            assert field >= 0, \
                f'is not nonnegative.'

        return _v_nonnegative

    @staticmethod
    def v_min(min):

        def _v_min(field):
            assert field >= min, \
                f'is smaller than minimum, {min}.'

        return _v_min

    @staticmethod
    def v_max(max):

        def _v_max(field):
            assert field <= max, \
                f'is smaller than minimum, {max}.'

        return _v_max

    @staticmethod
    def v_empty(_):

        def _v_empty(field):
            assert field, \
                'is empty.'

        return _v_empty

    @staticmethod
    def v_length(length):

        def _v_length(field):
            assert len(field) <= length, \
                f'exceeds length limit, {length}.'

        return _v_length

    @staticmethod
    def v_except_pattern(pattern):

        def _v_except_pattern(field):
            r_pattern = re.compile(pattern)
            assert not r_pattern.findall(field), \
                f'has invalid pattern: {pattern}'

        return _v_except_pattern

    @staticmethod
    def v_match_pattern(pattern):

        def _v_match_pattern(field):
            r_pattern = re.compile(pattern)
            assert r_pattern.findall(field), \
                f'does not have pattern: {pattern}'

        return _v_match_pattern


def get_required_validations(options, v_types):
    required_validations = []
    for v_type, v_option in options.items():
        if v_type in v_types:
            validation = getattr(Validator, f'v_{v_type}')(v_option)
            required_validations.append(validation)

    return required_validations


class FieldSpecMixin:

    def __init__(self, **kwargs):
        self._required_validations = get_required_validations(kwargs, self.v_types)
        self._nullable = kwargs.get('nullable', False)

    def validate_field(self, field):
        if field is None:
            if self._nullable:
                return True
            else:
                raise AssertionError('is not given or null.')

        field = self._validate_type(field)

        for validation in self._required_validations:
            validation(field)

        return True
