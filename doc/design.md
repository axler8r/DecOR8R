# Design

_DecOR8R_ follow the `ThreadingUnixStreamServer` and `StreamRequestHandler` from
the [`socketserver`](https://docs.python.org/3/library/socketserver.html) module
design pattern. The server is a `ThreadingUnixStreamServer` and the handler is a
`treamRequestHandler`. The server is a daemon that listens for incoming
connections and creates a new thread for each connection. The handler is
responsible for processing the request and sending the response back to the
client.

