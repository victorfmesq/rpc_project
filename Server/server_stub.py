from xmlrpc.server import SimpleXMLRPCServer

class ServerStub:
    def __init__(self, host='127.0.0.1', port=65432):
        self.server = SimpleXMLRPCServer((host, port))

    def register_function(self, func, name):
        self.server.register_function(func, name)

    def run(self):
        self.server.serve_forever()
