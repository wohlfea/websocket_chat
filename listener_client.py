from __future__ import unicode_literals
from autobahn.asyncio.websocket import WebSocketClientProtocol, \
                                       WebSocketClientFactory
import asyncio


class MyClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print('Connected to server: {}'.format(response.peer))

    def onOpen(self):
        print('Websocket connection is now open.')

    def onClose(self, wasClean, code, reason):
        print('Websocket connection closed: {}'.format(reason))
        self.factory.loop.stop()

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))


if __name__ == '__main__':
    factory = WebSocketClientFactory('ws://127.0.0.1:9000')
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory, '127.0.0.1', 9000)
    loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
