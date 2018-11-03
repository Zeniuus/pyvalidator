from abc import ABC, abstractmethod


class ABCFieldSpec(ABC):

    @abstractmethod
    def _validate_type(self, field):
        raise NotImplementedError

    @abstractmethod
    def validate_field(self, field):
        raise NotImplementedError
