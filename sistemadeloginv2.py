import csv
import subprocess

def criar_conta():
    usuario = input("Digite o nome de usuário desejado: ")
    senha = input("Digite a senha desejada: ")

   
    with open("usuarios.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[0] == usuario:
                print("Nome de usuário já existente. Tente novamente.")
                return

    
    with open("usuarios.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([usuario, senha])
    print("Conta criada com sucesso!")

def realizar_login():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    
    with open("usuarios.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[0] == usuario and linha[1] == senha:
                print("Login bem-sucedido!")
                abrir_aplicativos()
                return

    print("Credenciais inválidas. Tente novamente.")

def abrir_aplicativos():
    
    subprocess.Popen(["notepad.exe"])

# Menu principal
while True:
    print("1 - Criar conta")
    print("2 - Realizar login")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_conta()
    elif opcao == "2":
        realizar_login()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")