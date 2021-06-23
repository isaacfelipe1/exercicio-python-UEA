
while True:
    print("\n--------------------------------------\n")
    nome=input("Digite o nome\n")
    if nome.__len__()>3:
        print("Nome válido")
        print("\n--------------------------------------\n")
    elif nome.__len__()<3:
            print("Este nome é menor que 3 caractere\n")
            nome=input("Digite o nome\n")
            while nome.__len__()<3:
                print("Este nome é menor que 3 caractere\n")
                nome=input("Digite o nome\n")
    print("\n--------------------------------------\n")
    idade=int(input("Informe sua idade\n"))
    if idade<150:
        print("Idade válido\n")
    elif idade>150:
        while idade>150:
            print("Erro! Digite uma idade entre 0 e 150\n")
            idade=int(input("Informe sua idade\n"))
    print("\n......................................\n")   
    salario=float(input("Informe seu Sálario\n"))
    if salario>0:
        print("Salário válido\n")
    elif salario<0:
            while salario<0:
                print("Salário inválido! Dígite um salário válido\n")
                salario=float(input("Informe seu Salário\n"))
    sexo=input("Informe seu sexo  (m) para masculindo e (f) para femino\n")
    if sexo=='m':
        print("Masculino\n")
    if sexo=='f':
        print("Feminino")
    else:
        while sexo!='m' and sexo!='f':
                print("Inválido\n")
                sexo=input("Informe seu sexo  (m) para masculindo e (f) para femino\n")
                if sexo=='m':
                    print("Masculino\n")
                elif sexo=='f':
                    print("Feminino")
    estado_civil=input("Informe seu estado civil: (s) para solteiro (c) para casado (v) para viúva ou viuvo (d) para divorciado\n\n")
    if estado_civil=='s':
        print("Solteiro(a)\n")
    if estado_civil=='c':
        print("Casado(a)\n")
    if estado_civil=='v':
        print("viúva(a)\n")
    if estado_civil=='d':
        print("divorciado(a)\n")
    else:
        while estado_civil!='s' and estado_civil!='a' and estado_civil!='c' and estado_civil!='v' and estado_civil!='d':
                    print("Dígito inválido\n")
                    estado_civil=input("Informe seu estado civil: (s) para solteiro (c) para casado (v) para viúva ou viuvo (d) para divorciado:\n\n")
                    if estado_civil=='s':
                            print("Solteiro(a)\n")
                    elif estado_civil=='c':
                            print("Casado(a)\n")
                    elif estado_civil=='v':
                             print("viúva(a)\n")
                    elif estado_civil=='d':
                             print("divorciado(a)\n")


           