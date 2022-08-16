"""HTTP client providing sync and async access to APIs.

To use it, first create a client:

  >>> client = Client(base_url=settings.API_URL)

If the endpoints you are going to hit require authentication, use
`AuthenticatedClient` instead:

  >>> client = AuthenticatedClient(
  ...     base_url=settings.API_URL,
  ...     token='<your-super-secret-token>',
  ... )

Now call the endpoint using the corresponding data models:

  >>> ...


NOTE: This package is based on generated code by `openapi-python-client`.

"""

import inspect
from dataclasses import dataclass, field
from enum import Enum

import httpx

from xatch.tools import UNSET
from xatch.web.api import types as T


class HttpMethod(Enum):
    """HTTP methods to be used in API Clients."""

    GET = "get"
    OPTIONS = "options"
    HEAD = "head"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"

    DEFAULT = GET

    @staticmethod
    def check(value: str) -> str:
        """Check if a string value is a valid HTTP method."""
        if (res := value.upper()) in HttpMethod.__members__:
            return res
        else:
            raise ValueError(f"Invalid HTTP method '{value}'.")


HTTPX_REQUEST_PARAMETERS = inspect.signature(httpx.request).parameters

HTTP_METHOD = str | HttpMethod  # For typing

# Some shortcuts
HTTP = HttpMethod
GET = HttpMethod.GET
OPTIONS = HttpMethod.OPTIONS
HEAD = HttpMethod.HEAD
POST = HttpMethod.POST
PUT = HttpMethod.PUT
PATCH = HttpMethod.PATCH
DELETE = HttpMethod.DELETE


def parse_http_method(method: HTTP_METHOD) -> str:
    """Get a valid HTTP m string value."""
    if method:
        if isinstance(method, HttpMethod):
            return method.name
        else:
            return HttpMethod.check(method)
    else:
        return HttpMethod.DEFAULT.name


# TODO: Use `httpx.Client`, and `httpx.AsyncClient` for these classes.
@dataclass
class Client:
    """A class for keeping track of data related to the backend API."""

    base_url: str
    cookies: T.Cookies = field(default_factory=dict, kw_only=True)
    headers: T.Headers = field(default_factory=dict, kw_only=True)
    timeout: float = field(default=5.0, kw_only=True)
    verify: T.VerifySSL = field(default=True, kw_only=True)

    def get_headers(self) -> T.Headers:
        """Get headers to be used in all endpoints."""
        return self.headers

    def get_cookies(self) -> T.Cookies:
        """Get cookies to be used in all endpoints."""
        return self.cookies

    def _get_args(
        self, method: HTTP_METHOD, **kwargs: object
    ) -> T.AnyMapping:
        """Prepare arguments for httpx.request."""
        from urllib.parse import urljoin
        from xatch.tools import asdict

        MAPPINGS = ("cookies", "data", "headers", "files", "params")
        url: str = urljoin(self.base_url, kwargs.pop("url", ""))
        res = {
            "method": parse_http_method(method),
            "timeout": kwargs.pop("timeout", self.timeout),
            "verify": kwargs.pop("verify", self.verify),
        }
        for name in HTTPX_REQUEST_PARAMETERS:
            if (value := kwargs.pop(name, UNSET)) is not UNSET:
                res[name] = asdict(value) if name in MAPPINGS else value
        if headers := self.get_headers():
            res["headers"] = {**headers, **res.get("headers", {})}
        if cookies := self.get_cookies():
            res["cookies"] = {**cookies, **res.get("cookies", {})}
        if params := {**res.get("params", {}), **kwargs}:
            res["params"] = params
            url = url.format_map(params)
        res["url"] = url
        return res

    def __call__(
        self, method: HTTP_METHOD, url: str, **kwargs: object
    ) -> httpx.Response:
        """Execute a http request and parse the result."""
        args = self._get_args(method=method, url=url, **kwargs)
        return httpx.request(**args)


@dataclass
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints."""

    token: str

    def get_headers(self) -> T.Headers:
        """Get headers to be used in authenticated endpoints."""
        return {"Authorization": f"Bearer {self.token}", **self.headers}
