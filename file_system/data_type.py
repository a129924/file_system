from typing import List, Iterable, Optional, Union, Dict  # noqa: F401

from typing_extensions import TypedDict, TypeAlias
from werkzeug.datastructures import FileStorage


FileStorageList: TypeAlias = List[FileStorage]
FileStorageIterable: TypeAlias = Iterable[FileStorage]
TempleteHtmlString: TypeAlias = str


class UploadFileResult(TypedDict):
    filename: str
    dstpath: str
    success: bool


class SettingConfigs(TypedDict):
    ENV: str
    DEBUG: bool
    UPLOAD_FOLDER: str
    ALLOW_EXTENSIONS: List[str]
