from fastapi.routing import APIRouter

from deployer.web.api import docs, dummy, echo, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/webhook", tags=["webhook"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
