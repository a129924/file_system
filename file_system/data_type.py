from typing import List, Iterable, Optional, Union, Dict

from typing_extensions import TypedDict, TypeAlias
from werkzeug.datastructures import FileStorage


FileStorageList: TypeAlias = List[FileStorage]
FileStorageIterable: TypeAlias = Iterable[FileStorage]
TempleteHtmlString: TypeAlias = str


class UploadFileResult(TypedDict):
    filename: str
    dstpath: str
    success: bool
