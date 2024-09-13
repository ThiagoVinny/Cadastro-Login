import os

# Arquivo onde serão armazenados os cadastros
file_path = 'usuarios.txt'

def cadastrar_usuario(username, password):
    # Verificar se o arquivo já existe e criar se não
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass
    
    # Verificar se o usuário já está cadastrado
    if usuario_existe(username):
        return "Usuário já existe. Tente outro nome de usuário."
    
    # Adicionar o novo usuário
    with open(file_path, 'a') as f:
        f.write(f"{username}:{password}\n")
    
    return "Cadastro realizado com sucesso!"

def usuario_existe(username):
    with open(file_path, 'r') as f:
        for linha in f:
            usuario, _ = linha.strip().split(":")
            if usuario == username:
                return True
    return False

def login(username, password):
    with open(file_path, 'r') as f:
        for linha in f:
            usuario, senha = linha.strip().split(":")
            if usuario == username and senha == password:
                return "Login bem-sucedido!"
    return "Nome de usuário ou senha incorretos."

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            print(cadastrar_usuario(username, password))
        
        elif opcao == "2":
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")
            print(login(username, password))
        
        elif opcao == "3":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

menu()
