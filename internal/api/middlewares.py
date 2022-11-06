import logging
from typing import Callable, Awaitable
from aiohttp import web

logger = logging.getLogger(__name__)

Handler = Callable[[web.Request], Awaitable[web.Response]]


@web.middleware
async def logging_middleware(req: web.Request, handler: Handler) -> web.Response:
    rsp = await handler(req)
    msg = f'method={req.method} uri={req.path} status={rsp.status}'
    if rsp.status >= 500:
        logger.error(msg)
    else:
        logger.debug(msg)
    return rsp


@web.middleware
async def error_middleware(req: web.Request, handler: Handler) -> web.Response:
    try:
        rsp = await handler(req)
    except web.HTTPError as e:
        raise e
    except Exception:
        logger.exception("unexpected error")
        return web.Response(status=web.HTTPInternalServerError.status_code)
    else:
        return rsp
