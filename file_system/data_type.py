from typing import List, Iterable

from typing_extensions import TypedDict, TypeAlias
from werkzeug.datastructures import FileStorage


FileStorageList: TypeAlias = List[FileStorage]
FileStorageIterable: TypeAlias = Iterable[FileStorage]


class UploadFileResult(TypedDict):
    filename: str
    dstpath: str
    success: bool
