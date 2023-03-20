import os

import aiohttp_jinja2
import jinja2
from aiohttp import web

from app.db_connection import db_init
from app.router import setup_routes


async def on_startup(app):
    await db_init()


def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("app/templates"))

    app.on_startup.append(on_startup)

    setup_routes(app)

    return app


if __name__ == "__main__":
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("app/templates"))

    app.on_startup.append(on_startup)

    setup_routes(app)

    web.run_app(app, host="0.0.0.0", port=int(os.environ.get("APP_PORT", 8080)))
