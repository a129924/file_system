from file_system.data_type import SettingConfigs


DevelopConfigs: SettingConfigs = {
    "ENV": "development",
    "DEBUG": True,
    "UPLOAD_FOLDER": r"./file_system/static/download_file",
    "ALLOW_EXTENSIONS": [".txt", ".pdf", ".png", ".jpg", ".zip"],
}
