from client_stub import ClientStub

def menu():
    print("Escolha uma operação:")
    print("1: Somar")
    print("2: Subtrair")
    print("3: Multiplicar")
    print("4: Dividir")
    print("5: Sair")

if __name__ == "__main__":
    client_stub = ClientStub()

    while True:
        menu()
        opcao = input("Opção: ")

        if opcao == '5':
            break

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = client_stub.somar(a, b)
        elif opcao == '2':
            resultado = client_stub.subtrair(a, b)
        elif opcao == '3':
            resultado = client_stub.multiplicar(a, b)
        elif opcao == '4':
            resultado = client_stub.dividir(a, b)
        else:
            print("Opção inválida.")
            continue

        print(f"Resultado: {resultado}\n")
