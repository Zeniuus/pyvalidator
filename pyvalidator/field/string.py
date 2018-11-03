import re

from .base import ABCFieldSpec


class String(ABCFieldSpec):

    def __init__(self, length=None, nullable=False, empty=True,
                 except_pattern=None, match_pattern=None):
        self._length = length
        self._nullable = nullable
        self._empty = empty
        self._except_pattern = except_pattern
        self._match_pattern = match_pattern

    def validate_field(self, field):
        if field is None:
            if self._nullable:
                return True
            else:
                raise AssertionError('is not given or null.')
        assert isinstance(field, str), \
            'is not a string.'
        if not self._empty:
            assert field != '', \
                'is empty.'
        if self._length is not None:
            assert len(field) <= self._length, \
                f'exceeds length limit, {self._length}.'
        if self._except_pattern is not None:
            r_pattern = re.compile(self._except_pattern)
            assert not r_pattern.findall(field), \
                f'has invalid pattern: {self._except_pattern}'
        if self._match_pattern is not None:
            r_pattern = re.compile(self._match_pattern)
            assert r_pattern.findall(field), \
                f'does not have pattern: {self._except_pattern}'
        return True
