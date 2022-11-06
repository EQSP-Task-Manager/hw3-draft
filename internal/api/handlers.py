from aiohttp import web


class PingHandler(web.View):

    async def get(self) -> web.Response:
        return web.Response(status=web.HTTPInternalServerError.status_code)
