from flask import Flask
from file_system.setting import DevelopConfigs


def init_app():
    app = Flask(__name__)
    app.config.from_mapping(DevelopConfigs)
    print("INIT APP")
    with app.app_context():
        from file_system.routes import (
            root_bp,
            main_bp,
            upload_bp,
            download_bp,
            Blueprint as BlueprintType,
        )

        def register_blueprints(*blueprint_objs: BlueprintType) -> None:
            for blueprint_obj in blueprint_objs:
                app.register_blueprint(blueprint=blueprint_obj)

        register_blueprints(root_bp, main_bp, upload_bp, download_bp)

        return app
