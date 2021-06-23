#Escrever um algoritmo que leia o nome e o sexo de 50 pessoas informe o nome e o sexo de cada uma. Opções: ex.:(1 – MASCULINO / 2 - FEMININO). No final informe total de homens e de mulheres.
contador=1
homems=0
cont=0
i=0
while contador<=2:
    contador=contador+1
    nome=input("Informe o nome\n")
    sexo=int(input("Digite (1)- para Masculino (2)- para Feminino\n"))
    if sexo==1:
        homems+=sexo
        print("Nome: {} seu sexo é : masculino".format(nome))
    if sexo==2:
        cont=cont+1
        print("Nome: {} seu sexo é : Feminino".format(nome))

print("Total de Homens : ", homems)
print("Total de Mulheres: ", cont)
            
    


