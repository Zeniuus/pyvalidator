from abc import ABC, abstractmethod


class ABCFieldSpec(ABC):

    @abstractmethod
    def validate_field(self, field):
        raise NotImplementedError
