from server_stub import ServerStub

# Funções aritméticas
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

# Server Stub para registrar as funções
class Server:
    def __init__(self, host='127.0.0.1', port=65432):
        self.stub = ServerStub(host, port)
        self.stub.register_function(somar, 'somar')
        self.stub.register_function(subtrair, 'subtrair')
        self.stub.register_function(multiplicar, 'multiplicar')
        self.stub.register_function(dividir, 'dividir')

    def run(self):
        self.stub.run()

if __name__ == "__main__":
    server = Server()
    print("Servidor pronto para receber chamadas...")
    server.run()