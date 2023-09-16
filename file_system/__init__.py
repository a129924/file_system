from flask import Flask
from flask_migrate import Migrate

from file_system.setting import DevelopConfigs

from file_system.model import db


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
        db.init_app(app)

        # if DevelopConfigs["ENV"] == "development":
        #     reset_db()
        #     create_default_user()

        migrate = Migrate(app, db)

        return app
