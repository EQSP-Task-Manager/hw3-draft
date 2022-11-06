from aiohttp import web
from .config import setup_args_parser
from .logger import setup_logger
from .api import PingHandler
from .api import logging_middleware, error_middleware

def setup_app() -> web.Application:
    app = web.Application(
        middlewares=[logging_middleware, error_middleware]
    )
    app.router.add_view(
        '/ping', PingHandler
    )
    return app


def main():
    args_parser = setup_args_parser()
    args = args_parser.parse_args()
    logger = setup_logger(args.log_level)

    app = setup_app()
    logger.info('starting application')
    web.run_app(app, host=args.host, port=args.port)
    logger.info('stopped application')


if __name__ == '__main__':
    main()
