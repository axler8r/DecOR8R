import argparse
import os
import signal
import sys
from socketserver import ThreadingUnixStreamServer

from loguru import logger

from decor8r.handler import Handler


class Decor8rServer:
    """
    Represents a server for the DecOR8R application.

    Args:
        socket_path (str): The path to the Unix socket.

    Attributes:
        socket_path (str): The path to the Unix socket.
        server (ThreadingUnixStreamServer): The server instance.

    Methods:
        run(): Starts the server and listens for incoming connections.
        shutdown(signum, frame): Gracefully shuts down the server.
        cleanup(): Cleans up any resources used by the server.
    """

    def __init__(self, socket_path):
        self.socket_path = socket_path
        self.server = None

    def run(self):
        """
        Starts the server and listens for incoming connections.
        """
        if os.path.exists(self.socket_path):
            os.unlink(self.socket_path)

        self.server = ThreadingUnixStreamServer(self.socket_path, Handler)

        # Set up signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

        logger.info(f"Starting server on {self.socket_path}")
        try:
            self.server.serve_forever()
        except Exception as e:
            logger.error(f"Server error: {e}")
        finally:
            self.cleanup()

    def shutdown(self, signum, frame):
        """
        Gracefully shuts down the server.

        Args:
            signum (int): The signal number.
            frame (frame): The current stack frame.
        """
        logger.info("Shutting down server")
        if self.server:
            self.server.shutdown()

    def cleanup(self):
        """
        Cleans up any resources used by the server.
        """
        logger.info("Cleaning up")
        if os.path.exists(self.socket_path):
            os.unlink(self.socket_path)


def _parse_arguments():
    parser = argparse.ArgumentParser(description="Decor8r Server")
    parser.add_argument(
        "--socket", default="/tmp/decor8r.sock", help="Unix socket path"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_arguments()
    logger.add(
        sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO"
    )
    server = Decor8rServer(args.socket)
    server.run()