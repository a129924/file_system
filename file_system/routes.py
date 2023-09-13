from flask import Blueprint, Response as ResponseType

from file_system.view.index_view import (
    redirect_to_index as _redirect_to_index,
    render_index_page as _render_index_page,
    set_user as _set_user,
    index2 as _index2,
    upload_file as _upload_file,
    render_upload_file_page as _render_upload_file_page,
    render_download_template as _render_download_template,
    download_file as _download_file,
)
from file_system.data_type import TemplateHtmlString, BaseResponse
from file_system.setting import DevelopConfigs

TEMPLATE_FOLDER = "./static/templates"

root_bp: Blueprint = Blueprint("root", __name__, "/", template_folder=TEMPLATE_FOLDER)

main_bp: Blueprint = Blueprint(
    "index",
    __name__,
    url_prefix="/index",
    template_folder=TEMPLATE_FOLDER,
)

upload_bp: Blueprint = Blueprint(
    "upload", __name__, url_prefix="/upload-file", template_folder=TEMPLATE_FOLDER
)

download_bp: Blueprint = Blueprint(
    "download", __name__, url_prefix="/download-file", template_folder=TEMPLATE_FOLDER
)


# before_request
@main_bp.before_request
def print_hello_world() -> None:
    print("Hello World")


@root_bp.route("/", methods=["GET"])
def redirect_to_index() -> BaseResponse:
    return _redirect_to_index()


@main_bp.route("/", methods=["GET"])
def render_index_page() -> TemplateHtmlString:
    return _render_index_page()


@main_bp.route("/set-user", methods=["POST"])
def set_user() -> ResponseType:
    return _set_user()


@main_bp.route("/index2", methods=["GET"])
def index3() -> TemplateHtmlString:
    return _index2()


@upload_bp.route("/", methods=["POST"])
async def upload_file() -> TemplateHtmlString:
    return await _upload_file(DevelopConfigs)


@upload_bp.route("/", methods=["GET"])
def render_upload_file_page() -> TemplateHtmlString:
    return _render_upload_file_page()


@download_bp.route("/", methods=["GET"])
def render_download_file_page() -> TemplateHtmlString:
    return _render_download_template(DevelopConfigs)


@download_bp.route("/<string:filename>", methods=["GET"])
def download_file(filename: str) -> ResponseType:
    return _download_file(filename, DevelopConfigs)
