from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine
from piccolo.engine.sqlite import SQLiteEngine

from deployer.settings import settings

# DB = PostgresEngine(
#     config={
#         "database": settings.db_base,
#         "user": settings.db_user,
#         "password": settings.db_pass,
#         "host": settings.db_host,
#         "port": settings.db_port,
#     },
# )

DB = SQLiteEngine('deployer.sqlite', True)

APP_REGISTRY = AppRegistry(
    apps=["deployer.db.app_conf"],
)
