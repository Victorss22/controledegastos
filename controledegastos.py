class Conta:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Valor de R$ {valor} depósitado com sucesso, seu saldo atual é de: R${self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente!")


class ControleDeGastos:
    def __init__(self):
        self.conta = Conta()

    def registrar_ganho(self, valor):
        self.conta.depositar(valor)

    def registrar_depesa(self, valor):
        self.conta.sacar(valor)


def mostrar_menu():
    print("\n====== Menu Principal ======")
    print("1. Registrar Receita")
    print("2. Registrar Despesa")
    print("3. Somar Contas - Em Desenvolvimento")
    print("4. Sair")


def main():
    sistema = ControleDeGastos()
    while True:
        mostrar_menu()
        opcao = input("Escolha Sua Opção: ")
        if opcao == "1":
            valor = float(input("Digite o valor da receita: "))
            sistema.registrar_ganho(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor da despesa: "))
            sistema.registrar_depesa(valor)
        elif opcao == "3":
            print("Opção em desenvolvimento")
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida... Por favor escolha uma opção válida.")


if __name__ == "__main__":
    main()
