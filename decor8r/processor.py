class Processor:
    def __init__(self):
        pass

    def process(self, request: bytes) -> bytes:
        return request.upper()
