import collections
from typing import Any, Optional, Mapping, Dict, TypeVar, Callable, Union, overload, Text, Protocol, Iterator, IO
from collections import Container, Iterable, MutableSet

_K = TypeVar("_K")
_V = TypeVar("_V")
_R = TypeVar("_R")
_D = TypeVar("_D")

def is_immutable(self): ...
def iter_multi_items(mapping): ...
def native_itermethods(names): ...

class ImmutableListMixin(object):
    def __hash__(self) -> int: ...
    def __reduce_ex__(self, protocol): ...
    def __delitem__(self, key): ...
    def __delslice__(self, i, j): ...
    def __iadd__(self, other): ...
    __imul__: Any
    def __setitem__(self, key, value): ...
    def __setslice__(self, i, j, value): ...
    def append(self, item): ...
    remove: Any
    def extend(self, iterable): ...
    def insert(self, pos, value): ...
    def pop(self, index: int = ...): ...
    def reverse(self): ...
    def sort(self, cmp: Optional[Any] = ..., key: Optional[Any] = ..., reverse: Optional[Any] = ...): ...

class ImmutableList(ImmutableListMixin, list): ...  # type: ignore

class ImmutableDictMixin(object):
    @classmethod
    def fromkeys(cls, *args, **kwargs): ...
    def __reduce_ex__(self, protocol): ...
    def __hash__(self) -> int: ...
    def setdefault(self, key, default: Optional[Any] = ...): ...
    def update(self, *args, **kwargs): ...
    def pop(self, key, default: Optional[Any] = ...): ...
    def popitem(self): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def clear(self): ...

class ImmutableMultiDictMixin(ImmutableDictMixin):
    def __reduce_ex__(self, protocol): ...
    def add(self, key, value): ...
    def popitemlist(self): ...
    def poplist(self, key): ...
    def setlist(self, key, new_list): ...
    def setlistdefault(self, key, default_list: Optional[Any] = ...): ...

class UpdateDictMixin:
    on_update: Any
    def setdefault(self, key, default: Optional[Any] = ...): ...
    def pop(self, key, default=...): ...
    __setitem__: Any
    __delitem__: Any
    clear: Any
    popitem: Any
    update: Any

class TypeConversionDict(Dict[_K, _V]):
    @overload
    def get(self, key: _K, *, type: None = ...) -> Optional[_V]: ...
    @overload
    def get(self, key: _K, default: _D, type: None = ...) -> Union[_V, _D]: ...
    @overload
    def get(self, key: _K, *, type: Callable[[_V], _R]) -> Optional[_R]: ...
    @overload
    def get(self, key: _K, default: _D, type: Callable[[_V], _R]) -> Union[_R, _D]: ...

class ImmutableTypeConversionDict(ImmutableDictMixin, TypeConversionDict[_K, _V]):  # type: ignore
    def copy(self) -> TypeConversionDict[_K, _V]: ...
    def __copy__(self) -> ImmutableTypeConversionDict[_K, _V]: ...

class ViewItems:
    def __init__(self, multi_dict, method, repr_name, *a, **kw): ...
    def __iter__(self): ...

class MultiDict(TypeConversionDict):
    def __init__(self, mapping: Optional[Any] = ...): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def add(self, key, value): ...
    def getlist(self, key, type: Optional[Any] = ...): ...
    def setlist(self, key, new_list): ...
    def setdefault(self, key, default: Optional[Any] = ...): ...
    def setlistdefault(self, key, default_list: Optional[Any] = ...): ...
    def items(self, multi: bool = ...): ...
    def lists(self): ...
    def keys(self): ...
    __iter__: Any
    def values(self): ...
    def listvalues(self): ...
    def copy(self): ...
    def deepcopy(self, memo: Optional[Any] = ...): ...
    def to_dict(self, flat: bool = ...): ...
    def update(self, other_dict): ...
    def pop(self, key, default=...): ...
    def popitem(self): ...
    def poplist(self, key): ...
    def popitemlist(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...

class _omd_bucket:
    prev: Any
    key: Any
    value: Any
    next: Any
    def __init__(self, omd, key, value): ...
    def unlink(self, omd): ...

class OrderedMultiDict(MultiDict):
    def __init__(self, mapping: Optional[Any] = ...): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __reduce_ex__(self, protocol): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def keys(self): ...
    __iter__: Any
    def values(self): ...
    def items(self, multi: bool = ...): ...
    def lists(self): ...
    def listvalues(self): ...
    def add(self, key, value): ...
    def getlist(self, key, type: Optional[Any] = ...): ...
    def setlist(self, key, new_list): ...
    def setlistdefault(self, key, default_list: Optional[Any] = ...): ...
    def update(self, mapping): ...
    def poplist(self, key): ...
    def pop(self, key, default=...): ...
    def popitem(self): ...
    def popitemlist(self): ...

class Headers(collections.Mapping):
    def __init__(self, defaults: Optional[Any] = ...): ...
    def __getitem__(self, key, _get_mode: bool = ...): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @overload
    def get(self, key: str, *, type: None = ...) -> Optional[str]: ...
    @overload
    def get(self, key: str, default: _D, type: None = ...) -> Union[str, _D]: ...
    @overload
    def get(self, key: str, *, type: Callable[[str], _R]) -> Optional[_R]: ...
    @overload
    def get(self, key: str, default: _D, type: Callable[[str], _R]) -> Union[_R, _D]: ...
    @overload
    def get(self, key: str, *, as_bytes: bool) -> Any: ...
    @overload
    def get(self, key: str, *, type: None, as_bytes: bool) -> Any: ...
    @overload
    def get(self, key: str, *, type: Callable[[Any], _R], as_bytes: bool) -> Optional[_R]: ...
    @overload
    def get(self, key: str, default: Any, type: None, as_bytes: bool) -> Any: ...
    @overload
    def get(self, key: str, default: _D, type: Callable[[Any], _R], as_bytes: bool) -> Union[_R, _D]: ...
    def getlist(self, key, type: Optional[Any] = ..., as_bytes: bool = ...): ...
    def get_all(self, name): ...
    def items(self, lower: bool = ...): ...
    def keys(self, lower: bool = ...): ...
    def values(self): ...
    def extend(self, iterable): ...
    def __delitem__(self, key: Any) -> None: ...
    def remove(self, key): ...
    def pop(self, **kwargs): ...
    def popitem(self): ...
    def __contains__(self, key): ...
    has_key: Any
    def __iter__(self): ...
    def __len__(self): ...
    def add(self, _key, _value, **kw): ...
    def add_header(self, _key, _value, **_kw): ...
    def clear(self): ...
    def set(self, _key, _value, **kw): ...
    def setdefault(self, key, value): ...
    def __setitem__(self, key, value): ...
    def to_list(self, charset: Text = ...): ...
    def to_wsgi_list(self): ...
    def copy(self): ...
    def __copy__(self): ...

class ImmutableHeadersMixin:
    def __delitem__(self, key: str) -> None: ...
    def __setitem__(self, key, value): ...
    set: Any
    def add(self, *args, **kwargs): ...
    remove: Any
    add_header: Any
    def extend(self, iterable): ...
    def insert(self, pos, value): ...
    def pop(self, **kwargs): ...
    def popitem(self): ...
    def setdefault(self, key, default): ...

class EnvironHeaders(ImmutableHeadersMixin, Headers):
    environ: Any
    def __init__(self, environ): ...
    def __eq__(self, other): ...
    def __getitem__(self, key, _get_mode: bool = ...): ...
    def __len__(self): ...
    def __iter__(self): ...
    def copy(self): ...

class CombinedMultiDict(ImmutableMultiDictMixin, MultiDict):  # type: ignore
    def __reduce_ex__(self, protocol): ...
    dicts: Any
    def __init__(self, dicts: Optional[Any] = ...): ...
    @classmethod
    def fromkeys(cls): ...
    def __getitem__(self, key): ...
    def get(self, key, default: Optional[Any] = ..., type: Optional[Any] = ...): ...
    def getlist(self, key, type: Optional[Any] = ...): ...
    def keys(self): ...
    __iter__: Any
    def items(self, multi: bool = ...): ...
    def values(self): ...
    def lists(self): ...
    def listvalues(self): ...
    def copy(self): ...
    def to_dict(self, flat: bool = ...): ...
    def __len__(self): ...
    def __contains__(self, key): ...
    has_key: Any

class FileMultiDict(MultiDict):
    def add_file(self, name, file, filename: Optional[Any] = ..., content_type: Optional[Any] = ...): ...

class ImmutableDict(ImmutableDictMixin, dict):  # type: ignore
    def copy(self): ...
    def __copy__(self): ...

class ImmutableMultiDict(ImmutableMultiDictMixin, MultiDict):  # type: ignore
    def copy(self): ...
    def __copy__(self): ...

class ImmutableOrderedMultiDict(ImmutableMultiDictMixin, OrderedMultiDict):  # type: ignore
    def copy(self): ...
    def __copy__(self): ...

class Accept(ImmutableList):
    provided: Any
    def __init__(self, values=...): ...
    def __getitem__(self, key): ...
    def quality(self, key): ...
    def __contains__(self, value): ...
    def index(self, key): ...
    def find(self, key): ...
    def values(self): ...
    def to_header(self): ...
    def best_match(self, matches, default: Optional[Any] = ...): ...
    @property
    def best(self): ...

class MIMEAccept(Accept):
    @property
    def accept_html(self): ...
    @property
    def accept_xhtml(self): ...
    @property
    def accept_json(self): ...

class LanguageAccept(Accept): ...
class CharsetAccept(Accept): ...

def cache_property(key, empty, type): ...

class _CacheControl(UpdateDictMixin, dict):
    no_cache: Any
    no_store: Any
    max_age: Any
    no_transform: Any
    on_update: Any
    provided: Any
    def __init__(self, values=..., on_update: Optional[Any] = ...): ...
    def to_header(self): ...

class RequestCacheControl(ImmutableDictMixin, _CacheControl):  # type: ignore
    max_stale: Any
    min_fresh: Any
    no_transform: Any
    only_if_cached: Any

class ResponseCacheControl(_CacheControl):
    public: Any
    private: Any
    must_revalidate: Any
    proxy_revalidate: Any
    s_maxage: Any

class CallbackDict(UpdateDictMixin, dict):
    on_update: Any
    def __init__(self, initial: Optional[Any] = ..., on_update: Optional[Any] = ...): ...

class HeaderSet(MutableSet):
    on_update: Any
    def __init__(self, headers: Optional[Any] = ..., on_update: Optional[Any] = ...): ...
    def add(self, header): ...
    def remove(self, header): ...
    def update(self, iterable): ...
    def discard(self, header): ...
    def find(self, header): ...
    def index(self, header): ...
    def clear(self): ...
    def as_set(self, preserve_casing: bool = ...): ...
    def to_header(self): ...
    def __getitem__(self, idx): ...
    def __delitem__(self, idx): ...
    def __setitem__(self, idx, value): ...
    def __contains__(self, header): ...
    def __len__(self): ...
    def __iter__(self): ...
    def __nonzero__(self): ...

class ETags(Container, Iterable):
    star_tag: Any
    def __init__(self, strong_etags: Optional[Any] = ..., weak_etags: Optional[Any] = ..., star_tag: bool = ...): ...
    def as_set(self, include_weak: bool = ...): ...
    def is_weak(self, etag): ...
    def contains_weak(self, etag): ...
    def contains(self, etag): ...
    def contains_raw(self, etag): ...
    def to_header(self): ...
    def __call__(self, etag: Optional[Any] = ..., data: Optional[Any] = ..., include_weak: bool = ...): ...
    def __bool__(self): ...
    __nonzero__: Any
    def __iter__(self): ...
    def __contains__(self, etag): ...

class IfRange:
    etag: Any
    date: Any
    def __init__(self, etag: Optional[Any] = ..., date: Optional[Any] = ...): ...
    def to_header(self): ...

class Range:
    units: Any
    ranges: Any
    def __init__(self, units, ranges): ...
    def range_for_length(self, length): ...
    def make_content_range(self, length): ...
    def to_header(self): ...
    def to_content_range_header(self, length): ...

class ContentRange:
    on_update: Any
    units: Optional[str]
    start: Any
    stop: Any
    length: Any
    def __init__(self, units: Optional[str], start, stop, length: Optional[Any] = ..., on_update: Optional[Any] = ...): ...
    def set(self, start, stop, length: Optional[Any] = ..., units: Optional[str] = ...): ...
    def unset(self) -> None: ...
    def to_header(self): ...
    def __nonzero__(self): ...
    __bool__: Any

class Authorization(ImmutableDictMixin, Dict[str, Any]):  # type: ignore
    type: str
    def __init__(self, auth_type: str, data: Optional[Mapping[str, Any]] = ...) -> None: ...
    @property
    def username(self) -> Optional[str]: ...
    @property
    def password(self) -> Optional[str]: ...
    @property
    def realm(self) -> Optional[str]: ...
    @property
    def nonce(self) -> Optional[str]: ...
    @property
    def uri(self) -> Optional[str]: ...
    @property
    def nc(self) -> Optional[str]: ...
    @property
    def cnonce(self) -> Optional[str]: ...
    @property
    def response(self) -> Optional[str]: ...
    @property
    def opaque(self) -> Optional[str]: ...
    @property
    def qop(self) -> Optional[str]: ...

class WWWAuthenticate(UpdateDictMixin, dict):
    on_update: Any
    def __init__(self, auth_type: Optional[Any] = ..., values: Optional[Any] = ..., on_update: Optional[Any] = ...): ...
    def set_basic(self, realm: str = ...): ...
    def set_digest(self, realm, nonce, qop=..., opaque: Optional[Any] = ..., algorithm: Optional[Any] = ...,
                   stale: bool = ...): ...
    def to_header(self): ...
    @staticmethod
    def auth_property(name, doc: Optional[Any] = ...): ...
    type: Any
    realm: Any
    domain: Any
    nonce: Any
    opaque: Any
    algorithm: Any
    qop: Any
    stale: Any

class _Writer(Protocol):
    def write(self, data: bytes) -> Any: ...

class FileStorage(object):
    name: Optional[Text]
    stream: IO[bytes]
    filename: Optional[Text]
    headers: Headers
    def __init__(
        self,
        stream: Optional[IO[bytes]] = ...,
        filename: Union[None, Text, bytes] = ...,
        name: Optional[Text] = ...,
        content_type: Optional[Text] = ...,
        content_length: Optional[int] = ...,
        headers: Optional[Headers] = ...,
    ): ...
    @property
    def content_type(self) -> Optional[Text]: ...
    @property
    def content_length(self) -> int: ...
    @property
    def mimetype(self) -> str: ...
    @property
    def mimetype_params(self) -> Dict[str, str]: ...
    def save(self, dst: Union[Text, _Writer], buffer_size: int = ...): ...
    def close(self) -> None: ...
    def __nonzero__(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __getattr__(self, name: Text) -> Any: ...
    def __iter__(self) -> Iterator[bytes]: ...
