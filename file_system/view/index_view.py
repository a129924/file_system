from flask import render_template, send_file, request, Response

from file_system.data_type import Union, Optional, SettingConfigs, TemplateHtmlString
from file_system.controller.file_controller import FileUploadController
from file_system.controller.zip_controller import ZipController
from file_system.service.collections import join, listdir, get_file_target


def index() -> str:
    return render_template("index.html")


def index2() -> str:
    return "Hello world3267sssss"


async def upload_file(config: SettingConfigs) -> TemplateHtmlString:
    files = tuple(
        file
        for file in request.files.getlist("file")
        if file.filename
        and get_file_target(file.filename) in config["ALLOW_EXTENSIONS"]
    )

    file_upload_controller = FileUploadController(
        files=files, root_path=config["UPLOAD_FOLDER"]
    )

    await file_upload_controller.save_files()

    return render_template("upload_file.html", files=files)


def render_upload_file_page() -> TemplateHtmlString:
    return render_template("upload_file.html")


def download_file(
    config: SettingConfigs, filename: Optional[str] = None
) -> Union[str, Response]:
    if filename is None:
        return render_template(
            "download.html",
            download_files=listdir(
                join(
                    config["UPLOAD_FOLDER"],
                )
            ),
        )

    return send_file(
        ZipController(filename, root_path=config["UPLOAD_FOLDER"]).zip_file(),
        as_attachment=True,
        download_name="file.zip",
        mimetype="application/zip",
    )


def listdirs(filepath: Optional[str] = None) -> str:
    from os import listdir
    from sys import platform

    return f"listdir: {listdir(filepath)}, filepath:{filepath}, os:{platform}"
