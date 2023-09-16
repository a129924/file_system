from file_system.data_type import SettingConfigs
from file_system.service.collections import get_project_root_path, join

r"./file_system/static/download_file"

DevelopConfigs: SettingConfigs = {
    "ENV": "development",
    "DEBUG": True,
    "UPLOAD_FOLDER": rf"{join(get_project_root_path(), 'download_file')}",
    "ALLOW_EXTENSIONS": [".txt", ".pdf", ".png", ".jpg", ".zip"],
    "SQLALCHEMY_DATABASE_URI": "sqlite:///desserts.sqlite",
}
