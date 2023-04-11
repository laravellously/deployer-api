import os

from piccolo.conf.apps import AppConfig, table_finder

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="deployer_db",
    migrations_folder_path=os.path.join(
        CURRENT_DIRECTORY,
        "migrations",
    ),
    table_classes=table_finder(
        modules=[
            "deployer.db.models.dummy_model",
        ],
    ),
    migration_dependencies=[],
    commands=[],
)
