"""Collection of simple tools not tied to any specific framework.

In more stable versions of `xatch`, these tools will probably become part of
`xotl.tools`_.

.. _xotl.tools: https://github.com/merchise/xotl.tools

"""


class Unset:
    """Class for a false marker value.

    Useful as a replacement when `None` could be one of the expected valid
    values.

    """

    _singleton: 'Unset' = None

    def __new__(cls):  # noqa
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
        return cls._singleton

    def __bool__(self) -> bool:  # noqa
        return False


UNSET: Unset = Unset()


def named_lambda(**kwargs: callable) -> callable:
    """Return a named lambda function.

    Only one value must be provider in the `kwargs` parameters.  For example::

        >>> sum = named_lambda(sum=lambda df: df.sum(axis=1))

    """
    count = len(kwargs)
    if count == 1:
        name, fun = next(iter(kwargs.items()))
        fun.__name__ = fun.__qualname__ = name
        return fun
    else:
        raise ValueError(
            f"Invalid number of arguments, one expented, {count} given"
        )


def sda(obj: object, name: str, default: object = None) -> object:
    """Set default attribute value.

    Inserts the attribute with a value of 'default' if the object does not
    already have an attribute with the given 'name'.

    Return the value for 'name' if already present, else 'default'.

    """
    try:
        return getattr(obj, name)
    except AttributeError:
        setattr(obj, name, default)
        return default


def asdict(obj: object) -> dict[str, object]:
    """Return a new dictionary mapping from a given object.

    The function applies recursively to field values that are
    dataclass instances.

    """
    from collections import abc
    import dataclasses as dc

    if not isinstance(obj, type):
        if callable(getattr(obj, 'asdict', None)):
            return obj.asdict()
        elif dc.is_dataclass(obj):
            return dc.asdict(obj)
        elif callable(getattr(obj, 'dict', None)):  # pydantic
            return obj.dict()
        elif isinstance(obj, (abc.Mapping, abc.Sequence)):
            return dict(obj)
        else:
            tname = type(obj).__name__
            raise TypeError(
                f"asdict() should not be called on '{tname}' instances."
            )
    else:
        raise TypeError(
            f"asdict() should not be called on '{obj.__name__}' type."
        )


def current_process_contains(arg: str) -> bool:
    """Return True if `arg` is in the list of current parent processes."""
    import psutil

    arg = arg.lower()
    cp = psutil.Process()
    return next(
        (True for p in cp.parents() if arg in p.name().lower()),
        False,
    )


def is_type(arg: object) -> bool:
    """Return True if `arg` is a type, including those for generic typing."""
    from typing import Any, get_origin

    generic_base = type(Any)
    if (aux := generic_base.__base__) is not object:
        generic_base = aux
    return isinstance(arg, (type, generic_base)) or get_origin(arg)


def pop_items(source: dict, *keys) -> dict:
    """Pop a collection of keys from a source dictionary."""
    return {key: value for key in keys if (value := source.pop(key, None))}


def get_line(s: str, /, index: int = 0, strip_chars: str = None) -> str:
    """Get index line in a text."""
    if s:
        items = s.split('\n')
        if 0 <= index < len(items):
            res = s.split('\n')[index]
            if strip_chars:
                res = res.strip(strip_chars)
        else:
            res = ''
    else:
        res = ''
    return res


class slicer:
    """A simple syntax constructor for `slice` instances.

    For example::

      >>> slicer[1:10:2] == slice(1, 10, 2)
      >>> slicer[10] == 10

    """

    def __new__(cls, *args: object) -> slice:
        """Create a slice object (no need to use this)."""
        return slice(*args)

    def __class_getitem__(cls, index: object) -> object:
        """Create the slice the correct way."""
        return index
