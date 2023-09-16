from typing import List, Optional
from os import mkdir as _mkdir, listdir as _listdir

from os.path import (
    basename as _basename,
    exists as _exists,
    isfile as _isfile,
    isdir as _isdir,
    join as _join,
    splitext,
)

from os import getcwd as _getcwd


def isfile(path: str) -> bool:
    return _isfile(path)


def isdir(path: str) -> bool:
    return _isdir(path)


def join(*path: str) -> str:
    return _join(*path)


def is_exist(path: str) -> bool:
    return _exists(path)


def basename(path: str) -> str:
    return _basename(path)


def get_file_target(filepath: str, to_lower: bool = True) -> str:
    return splitext(filepath)[1].lower() if to_lower else splitext(filepath)[1]


def listdir(folderpath: Optional[str] = None) -> List[str]:
    return _listdir(folderpath)


def create_folder(folderpath: str) -> None:
    if not is_exist(folderpath):
        _mkdir(folderpath)


def get_project_root_path() -> str:
    return _getcwd()
