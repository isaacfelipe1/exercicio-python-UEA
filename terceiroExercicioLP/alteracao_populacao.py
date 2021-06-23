
entrada=int(input("Dígite 1 para começar\n"))
while entrada!=1:
        print("Inválido\n")
        entrada=int(input("Dígite 1 para começar\n"))
   
else:
    a=int(input("Informe a população de A\n"))
    taxa_De_crescimento_A=float(input("Informe a taxa de crescimento da população de A\n"))
    b=int(input("Informe a população de B\n"))
    taxa_De_crescimento_B=float(input("Informe a taxa de crescimento de B\n"))
    calculo_taxa_A=taxa_De_crescimento_A/100
    calculo_taxa_B=taxa_De_crescimento_B/100
    anos=0
    while a<=b:
        a+= a*calculo_taxa_A
        b+=b*calculo_taxa_B
        anos+=1
    print("O número de anos de A para ultrapassar ou iguala a B é de", anos)