from io import BytesIO
from zipfile import ZipFile

from os.path import join


def zip_file(*filenames: str, root_path: str) -> BytesIO:
    zip_buffer = BytesIO()

    with ZipFile(zip_buffer, "w") as _zip_file:
        for filename in filenames:
            _zip_file.write(filename=join(root_path, filename), arcname=filename)

    zip_buffer.seek(0)

    return zip_buffer
