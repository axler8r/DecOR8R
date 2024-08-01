import os
from socketserver import StreamRequestHandler, ThreadingUnixStreamServer

from loguru import logger

from decor8r.processor import Processor

if os.path.exists("/tmp/decor8r.sock"):
    os.unlink("/tmp/decor8r.sock")


class Handler(StreamRequestHandler):
    def __init__(self, request, client_address, server) -> None:
        self._processor = Processor()
        super().__init__(request, client_address, server)

    def handle(self):
        request = self.rfile.readline().strip()
        response = self._processor.process(request)

        logger.info(f"Received request: {request}")

        if request == b"stop":
            logger.info("Stopping server")
            self.server.shutdown()
        else:
            logger.info(f"Sending response: {response}")
            self.wfile.write(response)


with ThreadingUnixStreamServer("/tmp/decor8r.sock", Handler) as server:
    server.serve_forever()
