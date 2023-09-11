from flask import (
    render_template,
    send_file,
    request,
    make_response,
    Response,
    redirect,
    url_for,
)

from file_system.data_type import Optional, SettingConfigs, TemplateHtmlString
from file_system.controller.file_controller import FileUploadController
from file_system.controller.zip_controller import ZipController
from file_system.service.collections import join, listdir, get_file_target


def render_index_page() -> TemplateHtmlString:
    selected_user = request.cookies.get("selected_user")
    return render_template(
        "index.html",
        users=[
            "admin",
            "user1",
            "user2",
            "user3",
            "user4",
            "user5",
        ],
        selected_user=selected_user,
    )


def set_user() -> Response:
    selected_user: Optional[str] = request.form.get("selected-user")
    print(f"selected_user: {selected_user}")
    response = make_response(redirect(url_for("index.render_index_page")))
    if selected_user == "選擇使用者":
        return response

    response.set_cookie(
        key="selected_user", value=selected_user if selected_user else ""
    )
    return response


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


def render_download_template(config: SettingConfigs) -> TemplateHtmlString:
    return render_template(
        "download.html", download_files=listdir(join(config["UPLOAD_FOLDER"]))
    )


def download_file(filename: str, config: SettingConfigs) -> Response:
    root_path = join(config["UPLOAD_FOLDER"], filename)

    return send_file(
        ZipController(
            *listdir(root_path),
            root_path=root_path,
        ).zip_file(),
        as_attachment=True,
        download_name="file.zip",
        mimetype="application/zip",
    )


def listdirs(filepath: Optional[str] = None) -> str:
    from os import listdir
    from sys import platform

    return f"listdir: {listdir(filepath)}, filepath:{filepath}, os:{platform}"
