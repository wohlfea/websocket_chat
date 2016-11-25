from __future__ import unicode_literals
from autobahn.asyncio.websocket import WebSocketServerProtocol, \
                                       WebSocketServerFactory
import asyncio


class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        """Print which client is connecting to the server."""
        print('Client connecting: {}'.format(request.peer))

    def onMessage(self, payload, isBinary):
        """Echo back the message verbatim."""
        self.sendMessage(payload, isBinary)


if __name__ == '__main__':
    factory = WebSocketServerFactory()
    factory.protocol = MyServerProtocol
    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '127.0.0.1', 9000)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()
