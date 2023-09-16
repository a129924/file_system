from typing import List, Iterable, Optional, Union, Dict, Tuple  # noqa: F401

from typing_extensions import Literal, TypedDict, TypeAlias  # noqa: F401
from werkzeug.datastructures import FileStorage
from werkzeug.wrappers.response import Response as BaseResponse  # noqa: F401


FileStorageList: TypeAlias = List[FileStorage]
FileStorageIterable: TypeAlias = Iterable[FileStorage]
TemplateHtmlString: TypeAlias = str


class UploadFileResult(TypedDict):
    filename: str
    dstpath: str
    success: bool


class SettingConfigs(TypedDict):
    ENV: str
    DEBUG: bool
    UPLOAD_FOLDER: str
    ALLOW_EXTENSIONS: List[str]
    SQLALCHEMY_DATABASE_URI: str


class UserInfo(TypedDict):
    username: str
    is_admin: bool
