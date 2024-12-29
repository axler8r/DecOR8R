from socketserver import StreamRequestHandler

from loguru import logger

from decor8rd.processor import Processor


class Handler(StreamRequestHandler):
    """
    A request handler class that processes incoming requests.

    This class extends the StreamRequestHandler class from the socketserver module.
    It handles incoming requests by processing them using an instance of the Processor class.

    Attributes:
        _processor (Processor): An instance of the Processor class used to process requests.

    Methods:
        handle(): Overrides the handle method of the StreamRequestHandler class.
                  It reads the incoming request, processes it, and sends the response back.

    """

    def __init__(self, request, client_address, server) -> None:
        self._processor = Processor()
        super().__init__(request, client_address, server)

    def handle(self):
        """
        Handles the incoming request and sends the response.

        This method reads the request from the client, processes it using the
        `_processor` object, and sends the response back to the client.

        If the request is empty, a warning is logged and no response is sent.

        If the request is "stop", a stop command is logged and the server is
        shut down.

        Any exceptions that occur during request processing are logged as errors.

        Returns:
            None
        """
        try:
            request = self.rfile.readline().strip()
            logger.info(f"Received request: {request} from {self.client_address}")

            if not request:
                logger.warning("Empty request received")
                return

            if request == b"stop":
                logger.info("Stop command received")
                self.server.shutdown()
                return

            response = self._processor.process(request)
            logger.info(f"Sending response: {response}")
            self.wfile.write(response)

        except Exception as e:
            logger.error(f"Error processing request: {e}")
