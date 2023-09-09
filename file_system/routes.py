from flask import Blueprint

from file_system.view.index_view import (
    index as _index,
    index2 as _index2,
    upload_file as _upload_file,
)
from file_system.data_type import TempleteHtmlString
from file_system.setting import DevelopConfigs

TEMPLATE_FOLDER = "./static/templates"

main_bp: Blueprint = Blueprint(
    "index",
    __name__,
    url_prefix="/index",
    template_folder=TEMPLATE_FOLDER,
)

upload_bp: Blueprint = Blueprint(
    "upload", __name__, url_prefix="/upload", template_folder=TEMPLATE_FOLDER
)


@main_bp.route("/", methods=["GET"])
def index() -> TempleteHtmlString:
    return _index()


@main_bp.route("/index2", methods=["GET"])
def index2() -> TempleteHtmlString:
    return _index2()


@upload_bp.route("/", methods=["GET", "POST"])
async def upload_file():
    return await _upload_file(DevelopConfigs)
