d=0
a=int(input("Informe o valor de A\n"))
while a==0:
    a=int(input("Informe o valor de A\n"))
if a<0:
    print("Não existe número real para delta menor que zero")
elif a>0:
        b=int(input("Informe o valor de B\n"))
        c=int(input("Informe o valor de C\n"))
        d=(b*b)-a*c
        print(d)  


       