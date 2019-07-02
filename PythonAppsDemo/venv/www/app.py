
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web



def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

@asyncio.coroutine
def init(loops):
    app = web.Application(loop=loops)
    app.router.add_route('GET', '/', index)
    srv = yield from loops.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

if __name__ == '__main__':
    print('...')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()