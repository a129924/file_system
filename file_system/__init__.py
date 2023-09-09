from flask import Flask
from file_system.setting import DevelopConfigs


def init_app():
    app = Flask(__name__)
    app.config.from_mapping(DevelopConfigs)

    with app.app_context():
        from file_system.routes import (  # noqa: E402
            main_bp,
            upload_bp,
            Blueprint as BlueprintType,
        )

        def register_blueprints(*blueprint_objs: BlueprintType) -> None:
            for blueprint_obj in blueprint_objs:
                app.register_blueprint(blueprint=blueprint_obj)

        register_blueprints(main_bp, upload_bp)

        return app
