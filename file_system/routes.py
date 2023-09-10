from flask import Blueprint

from file_system.view.index_view import (
    index as _index,
    index2 as _index2,
    upload_file as _upload_file,
    render_upload_file_page as _render_upload_file_page,
)
from file_system.data_type import TemplateHtmlString
from file_system.setting import DevelopConfigs

TEMPLATE_FOLDER = "./static/templates"

main_bp: Blueprint = Blueprint(
    "index",
    __name__,
    url_prefix="/index",
    template_folder=TEMPLATE_FOLDER,
)

upload_bp: Blueprint = Blueprint(
    "upload", __name__, url_prefix="/upload-file", template_folder=TEMPLATE_FOLDER
)


@main_bp.route("/", methods=["GET"])
def index() -> TemplateHtmlString:
    return _index()


@main_bp.route("/index2", methods=["GET"])
def index2() -> TemplateHtmlString:
    return _index2()


@upload_bp.route("", methods=["POST"])
async def upload_file() -> TemplateHtmlString:
    return await _upload_file(DevelopConfigs)


@upload_bp.route("/", methods=["GET"])
def render_upload_file_page():
    return _render_upload_file_page()
