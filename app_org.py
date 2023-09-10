from typing import Optional, Union

from flask import Flask, request, render_template, send_file
from flask.wrappers import Response

from file_system.setting import DevelopConfigs
from file_system.controller.file_controller import FileUploadController
from file_system.controller.zip_controller import ZipController
from file_system.service.collections import join, listdir, get_file_target

app = Flask(__name__, template_folder="./file_system/static/templates")
app.config.from_mapping(DevelopConfigs)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/index2")
def index2():
    return "Hello world3267sssss"


@app.route("/upload-file", methods=["GET", "POST"])
async def upload_file() -> str:
    if request.method == "POST":
        files = tuple(
            file
            for file in request.files.getlist("file")
            if file.filename
            and get_file_target(file.filename) in app.config["ALLOW_EXTENSIONS"]
        )

        file_upload_controller = FileUploadController(
            files=files, root_path=app.config["UPLOAD_FOLDER"]
        )

        await file_upload_controller.save_files()

        if files:
            return render_template("upload_file.html", files=files)

    return render_template("upload_file.html")


@app.route("/download")
@app.route("/download/<string:filename>")
def download_file(filename: Optional[str] = None) -> Union[str, Response]:
    if filename is None:
        return render_template(
            "download.html",
            download_files=listdir(
                join(
                    app.config["UPLOAD_FOLDER"],
                )
            ),
        )
    # print()
    root_path = join(app.config["UPLOAD_FOLDER"], filename)
    return send_file(
        ZipController(
            *listdir(root_path),
            root_path=root_path,
        ).zip_file(),
        as_attachment=True,
        download_name="file.zip",
        mimetype="application/zip",
    )


@app.route("/ls")
@app.route("/ls/<path:filepath>")
def listdirs(filepath: Optional[str] = None) -> str:
    from os import listdir
    from sys import platform

    return f"listdir: {listdir(filepath)}, filepath:{filepath}, os:{platform}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
