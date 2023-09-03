from typing import Dict, List, Union

DevelopConfigs: Dict[str, Union[str, bool, List[str]]] = dict(
    ENV="development",
    DEBUG=True,
    UPLOAD_FOLDER=r"./file_system/static/download_file",
    ALLOW_EXTENSIONS=[".txt", ".pdf", ".png", ".jpg", ".zip"],
)
