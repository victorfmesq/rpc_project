import xmlrpc.client

class ClientStub:
    def __init__(self, server_address='http://127.0.0.1:65432'):
        self.server = xmlrpc.client.ServerProxy(server_address)

    def somar(self, a, b):
        return self.server.somar(a, b)

    def subtrair(self, a, b):
        return self.server.subtrair(a, b)

    def multiplicar(self, a, b):
        return self.server.multiplicar(a, b)

    def dividir(self, a, b):
        return self.server.dividir(a, b)
