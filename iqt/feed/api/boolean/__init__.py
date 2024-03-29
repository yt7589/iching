
from typing import List

from iqt.feed.core import Stream
from iqt.feed.core.methods import Methods
from iqt.feed.core.mixins import DataTypeMixin


@Stream.register_accessor(name="bool")
class BooleanMethods(Methods):
    ...


@Stream.register_mixin(dtype="bool")
class BooleanMixin(DataTypeMixin):
    ...


class Boolean:
    """A class to register accessor and instance methods."""

    @classmethod
    def register(cls, names: List[str]):
        """A function decorator that adds accessor and instance methods for
        specified data type.

        Parameters
        ----------
        names : `List[str]`
            A list of names used to register the function as a method.

        Returns
        -------
        Callable
            A decorated function.
        """
        def wrapper(func):
            BooleanMethods.register_method(func, names)
            BooleanMixin.register_method(func, names)
            return func
        return wrapper


from iqt.feed.api.boolean.operations import *
