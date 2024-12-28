class Processor:
    """
    The Processor class is responsible for processing requests.

    Methods:
        process(request: bytes) -> bytes: Processes the given request and returns the processed result.
    """

    def __init__(self):
        pass

    def process(self, request: bytes) -> bytes:
        """
        Processes the given request and returns the processed result.

        Args:
            request (bytes): The request to be processed.

        Returns:
            bytes: The processed result.
        """
        return request.upper()
