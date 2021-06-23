#Faça um programa que solicite uma senha de acesso do usuário, o sistema deve comparar com a senha “abc123” e:Caso o usuário digite a senha correta, informar “Acesso liberado”, masCaso o usuário digite a senha incorreta, informar “Acesso negado” e perguntar novamente enquanto a senha estiver incorreta.

senha_acesso="abc123"

senha=input("Informe sua senha\n")
while senha!=senha_acesso:
    print("Acesso negado\n")
    senha=input("Informe sua senha\n")
if senha==senha_acesso:
    print("Acesso Liberado")

