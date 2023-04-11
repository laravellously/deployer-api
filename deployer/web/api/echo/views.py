import http
from typing import Annotated
from fastapi import APIRouter, Form, Request

from deployer.web.api.echo.schema import Message

router = APIRouter()

@router.post("/", response_model=Message)
async def send_echo_message(
    incoming_message: Message,
) -> Message:
    """
    Sends echo back to user.

    :param incoming_message: incoming message.
    :returns: message same as the incoming.
    """

    return {"message": "hello"}


@router.post("/paddle/392c8fca-0019-47cc-98e3-f4a10f62ed62", status_code=http.HTTPStatus.ACCEPTED)
async def webhook(data: Annotated[list, Form()]):
    print(data)
    return {}
