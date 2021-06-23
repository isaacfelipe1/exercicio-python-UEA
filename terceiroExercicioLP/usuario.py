nome_usuario=input("faça o login com seu nome\n")
senha=input("Digite sua senha\n")
while senha==nome_usuario:
    print("Erro! Senha ou nome de usuário inválido\n")
    nome_usuario=input("faça o login com seu nome\n")
    senha=input("Digitre sua senha\n")
