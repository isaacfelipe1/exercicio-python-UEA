c1=10
c2=22
c3=6.8

escolha=int(input("Digite (1) para Ligar todos os capacitadores ou (2) para os capacitadores em series\n"))
if escolha==1:
    cp=(c1+c2+c3)
    print(cp)
elif escolha==2:
    cs= ((c1/1) + (c2/1) + (c3/1))/1
    print(cs)

