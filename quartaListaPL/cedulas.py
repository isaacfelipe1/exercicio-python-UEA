valor=float(input("Digite o valor a pagar:"))#esta pedindo um valor do usuario
cédulas=0
atual=100.0
apagar=valor
while True:
        #110 é menor ou igual valor queo usuario digitou
    if atual<=apagar:
        apagar-=atual#vale 100
        cédulas+=1
    else:
        if apagar == 0:
         break
        if atual == 100:
            atual = 50
        elif atual == 50:
                atual =20
        elif atual ==20:
                atual=10
        elif atual==10:
                 atual=5
        elif atual==5:
                atual=1
        elif atual==1:
            atual=0.50
        elif atual==0.50:
            atual=0.10
        elif atual==0.10:
            atual=0.05
        elif atual==0.05:
            atual=0.02
        elif atual==0.02:
            atual=0.001
        elif atual==0.001:
            atual=0
            cédulas=0
    print("%d cédula(s) de R$%5.2f" % (cédulas, atual))


