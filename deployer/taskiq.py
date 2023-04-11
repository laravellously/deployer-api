import taskiq_fastapi

from deployer.settings import settings
from taskiq import InMemoryBroker, ZeroMQBroker

broker = ZeroMQBroker()

if settings.environment.lower() == "pytest":
    broker = InMemoryBroker()

taskiq_fastapi.init(broker, "tkiqtest.web.application:get_app")
