from flask import render_template
from file_system.data_type import FileStorageList, List


def render_upload_file_template(files: FileStorageList) -> str:
    return render_template("upload_file.html", files=files)


def render_download_all_file_template(download_files: List[str]) -> str:
    return render_template("download.html", download_files=download_files)
