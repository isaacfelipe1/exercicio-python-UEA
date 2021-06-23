valorUm=int(input("Dígite o inicio\n"))
valorDois=int(input("Dígite o fim\n"))
while valorUm<=valorDois:
    print('%d x %d= %d'%(valorUm,valorDois,valorDois*valorUm))
    valorUm=valorDois+1