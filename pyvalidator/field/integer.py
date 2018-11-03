from .base import ABCFieldSpec


class Integer(ABCFieldSpec):

    def __init__(self, positive=None, nonnegative=None,
                 nullable=False, min=None, max=None):
        self._nullable = nullable
        self._positive = positive
        self._nonnegative = nonnegative
        self._min = min
        self._max = max

    def validate_field(self, field):
        if field is None:
            if self._nullable:
                return True
            else:
                raise AssertionError('is not given or null.')
        try:
            val = int(field)
        except ValueError:
            raise AssertionError('is not an integer.')

        if self._min is not None:
            assert val >= self._min, \
                f'is smaller than minimum, {self._min}.'
        if self._max is not None:
            assert val <= self._max, \
                f'is smaller than maximum, {self._max}.'
        if self._positive is not None:
            assert val > 0, \
                f'is not positive.'
        if self._nonnegative is not None:
            assert val >= 0, \
                f'is not nonnegative.'
        return True
