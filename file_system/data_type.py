from typing_extensions import TypedDict


class UploadFileResult(TypedDict):
    filename: str
    dstpath: str
    success: bool
