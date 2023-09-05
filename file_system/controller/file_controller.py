from file_system.service.file_manager.upload_file import save_file as _save_file
from file_system.data_type import UploadFileResult, FileStorageIterable, List


class FileUploadController:
    def __init__(self, files: FileStorageIterable, root_path: str) -> None:
        self.files = files
        self.root_path = root_path

    async def save_files(
        self,
    ) -> List[UploadFileResult]:
        return [await _save_file(file, self.root_path) for file in self.files]
