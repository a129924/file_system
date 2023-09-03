from io import BytesIO

from file_system.service.zip_manager.zip_file import zip_file as _zip_file


class ZipController:
    def __init__(self, *filenames: str, root_path: str) -> None:
        self.filenames = filenames
        self.root_path = root_path

    def zip_file(self) -> BytesIO:
        return _zip_file(*self.filenames, root_path=self.root_path)
