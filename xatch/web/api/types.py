"""Contains some shared types for properties."""

from dataclasses import dataclass, field
from ssl import SSLContext
from typing import BinaryIO, Generic, Sequence, TypeVar, Union


AnyMapping = dict[str]
StrMapping = dict[str, str] | Sequence[tuple[str, str]]

Headers = StrMapping
Cookies = StrMapping  # TODO: `CookieJar`?
RequestData = AnyMapping
FormData = Union[RequestData, 'BaseForm']

VerifySSL = str | bool | SSLContext


T = TypeVar('T', bound='BaseModel')


@dataclass
class BaseModel:
    """A base class for a request API model."""

    extra_properties: AnyMapping = field(init=False, default_factory=dict)

    @classmethod
    def create(cls, **kwargs: object) -> T:
        """Create an instance using given keyword arguments as fields."""
        fields = cls.__dataclass_fields__
        errors = [f for f in fields if f in kwargs and not fields[f].init]
        if errors:
            msg = f"'{cls.__name__}.from_dict' got unexpected fields {errors}"
            raise ValueError(msg)
        params = {k: kwargs.pop(k) for k in tuple(kwargs) if k in fields}
        res = cls(**params)
        res.extra_properties = kwargs
        return res

    @property
    def extra_keys(self) -> list[str]:  # noqa: D102
        return self.extra_properties.keys()

    def __getitem__(self, key: str) -> object:  # noqa: D105
        return self.extra_properties[key]

    def __setitem__(self, key: str, value: object):  # noqa: D105
        self.extra_properties[key] = value

    def __delitem__(self, key: str):  # noqa: D105
        del self.extra_properties[key]

    def __contains__(self, key: str) -> bool:  # noqa: D105
        return key in self.extra_properties


@dataclass
class BaseForm:
    """A base class for a request API form."""


FileJson = tuple[str | None, BinaryIO, str | None]


@dataclass
class File:
    """Contains information for file uploads."""

    payload: BinaryIO
    file_name: str = None
    mime_type: str = None

    def astuple(self) -> FileJson:
        """Return a value that httpx will accept for multipart/form-data."""
        return (self.file_name, self.payload, self.mime_type)


T = TypeVar("T")


@dataclass
class Response(Generic[T]):
    """A response from an endpoint."""

    status_code: int
    content: bytes
    headers: dict[str, str]
    parsed: T | None
