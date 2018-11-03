from .base import ABCFieldSpec
from .validator import FieldSpecMixin


class StringFieldSpec(ABCFieldSpec):

    v_types = ['length', 'empty', 'except_pattern', 'match_pattern']

    def _validate_type(self, field):
        assert isinstance(field, str), \
            'is not a string.'
        return field


class String(FieldSpecMixin, StringFieldSpec):
    pass
