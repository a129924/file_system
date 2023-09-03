import asyncio

from werkzeug.datastructures import FileStorage

from file_system.data_type import UploadFileResult
from file_system.service.collections import (
    get_file_target,
    create_folder,
    join,
)


async def save_file(file: FileStorage, root_path: str) -> UploadFileResult:
    filename: str = file.filename  # type: ignore
    print("底層save_file")

    target: str = get_file_target(filename)
    dst_path: str = join(root_path, target)

    create_folder(dst_path)
    print(f"target: {target}, filename: {filename}")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, file.save, join(dst_path, filename))

    return UploadFileResult(filename=filename, dstpath=dst_path, success=True)
