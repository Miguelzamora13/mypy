# Stubs for string

# Based on http://docs.python.org/3.2/library/string.html

from typing import Mapping, Sequence, Any, Optional, Union, List, Tuple, Iterable, AnyStr

ascii_letters = ''
ascii_lowercase = ''
ascii_uppercase = ''
digits = ''
hexdigits = ''
letters = ''
lowercase = ''
octdigits = ''
punctuation = ''
printable = ''
uppercase = ''
whitespace = ''

def capwords(s: AnyStr, sep: AnyStr = None) -> AnyStr: ...
# TODO: originally named 'from'
def maketrans(_from: str, to: str) -> str: ...
def atof(s: unicode) -> float: ...
def atoi(s: unicode, base: int = 10) -> int: ...
def atol(s: unicode, base: int = 10) -> int: ...
def capitalize(word: AnyStr) -> AnyStr: ...
def find(s: unicode, sub: unicode, start: int = None, end: int = None) -> int: ...
def rfind(s: unicode, sub: unicode, start: int = None, end: int = None) -> int: ...
def index(s: unicode, sub: unicode, start: int = None, end: int = None) -> int: ...
def rindex(s: unicode, sub: unicode, start: int = None, end: int = None) -> int: ...
def count(s: unicode, sub: unicode, start: int = None, end: int = None) -> int: ...
def lower(s: AnyStr) -> AnyStr: ...
def split(s: AnyStr, sep: AnyStr = None, maxsplit: int = -1) -> List[AnyStr]: ...
def rsplit(s: AnyStr, sep: AnyStr = None, maxsplit: int = -1) -> List[AnyStr]: ...
def splitfields(s: AnyStr, sep: AnyStr = None, maxsplit: int = -1) -> List[AnyStr]: ...
def join(words: Iterable[AnyStr], sep: AnyStr = None) -> AnyStr: ...
def joinfields(word: Iterable[AnyStr], sep: AnyStr = None) -> AnyStr: ...
def lstrip(s: AnyStr, chars: AnyStr = None) -> AnyStr: ...
def rstrip(s: AnyStr, chars: AnyStr = None) -> AnyStr: ...
def strip(s: AnyStr, chars: AnyStr = None) -> AnyStr: ...
def swapcase(s: AnyStr) -> AnyStr: ...
def translate(s: str, table: str, deletechars: str = None) -> str: ...
def upper(s: AnyStr) -> AnyStr: ...
def ljust(s: AnyStr, width: int, fillhar: AnyStr = ' ') -> AnyStr: ...
def rjust(s: AnyStr, width: int, fillhar: AnyStr = ' ') -> AnyStr: ...
def center(s: AnyStr, width: int, fillhar: AnyStr = ' ') -> AnyStr: ...
def zfill(s: AnyStr, width: int) -> AnyStr: ...
def replace(s: AnyStr, old: AnyStr, new: AnyStr, maxreplace: int = None) -> AnyStr: ...

class Template(object):
    # TODO: Unicode support?
    template = ''

    def __init__(self, template: str) -> None: ...
    def substitute(self, mapping: Mapping[str, str], **kwds: str) -> str: ...
    def safe_substitute(self, mapping: Mapping[str, str],
                        **kwds: str) -> str: ...

# TODO(MichalPokorny): This is probably badly and/or loosely typed.
class Formatter(object):
    def format(self, format_string: str, *args, **kwargs) -> str: ...
    def vformat(self, format_string: str, args: Sequence[Any],
                kwargs: Mapping[str, Any]) -> str: ...
    def parse(self, format_string: str) -> Iterable[Tuple[str, str, str, str]]: ...
    def get_field(self, field_name: str, args: Sequence[Any],
                  kwargs: Mapping[str, Any]) -> Any: ...
    def get_value(self, key: Union[int, str], args: Sequence[Any],
                  kwargs: Mapping[str, Any]) -> Any:
        raise IndexError()
        raise KeyError()
    def check_unused_args(self, used_args: Sequence[Union[int, str]], args: Sequence[Any],
                          kwargs: Mapping[str, Any]) -> None: ...
    def format_field(self, value: Any, format_spec: str) -> Any: ...
    def convert_field(self, value: Any, conversion: str) -> Any: ...
