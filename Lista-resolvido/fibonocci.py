anterior=0
proximo=0
usuario=int(input("Informe um numero\n"))

while (proximo<usuario):
    print(proximo)
    proximo=proximo+anterior
    anterior=proximo-anterior
    if(proximo==0):
        proximo=proximo+1