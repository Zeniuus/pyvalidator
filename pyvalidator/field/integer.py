from .base import ABCFieldSpec
from .validator import FieldSpecMixin


class IntegerFieldSpec(ABCFieldSpec):

    v_types = ['positive', 'nonnegative', 'min', 'max']

    def _validate_type(self, field):
        try:
            val = int(field)
        except ValueError:
            raise AssertionError('is not an integer.')
        return val


class Integer(FieldSpecMixin, IntegerFieldSpec):
    pass
