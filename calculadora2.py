def calculadora():
    n1 = int(input("Número: "))
    while True:
        operacao = input("[+] Adicionar\n[-] Subtrair\n[*] Multiplicar\n[/] Dividir\nOperação: ")
        n2 = int(input("Número: "))
        operacoes = {
                "+": adicionar(n1,n2),
                "-": subtrair(n1,n2),
                "*": multiplicar(n1,n2),
                "/": dividir(n1,n2)
                }
        print(f"{n1} {operacao} {n2} =  {operacoes[operacao]}")
        n1 = operacoes[operacao]
        nova_operacao = input("Nova operação - [S] Sim ou [N] Não: ").lower()
        if nova_operacao == "n":
            break

def adicionar(n1, n2):
    return n1 + n2
def subtrair(n1, n2):
    return n1 - n2
def multiplicar(n1, n2):
    return n1 * n2
def dividir(n1, n2):
    return n1 / n2

calculadora()