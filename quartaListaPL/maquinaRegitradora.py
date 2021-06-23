#Escreva um programa para controlar uma pequena máquina registradora.
#Você deve solicitar ao usuário que digite o código do produto e a quantidade
#. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
soma=0
total_compra=0
um=0.50
dois=1.00
tres=4.00
cinco=7.00
nove=8.00
while True:
    codigo_produto=int(input("Dígite o código\n"))
    if codigo_produto==0 :
            print("Obrigado por utilizar o programa\n")
            break
    while codigo_produto!=1 and codigo_produto !=2 and codigo_produto!=3 and codigo_produto!=5 and codigo_produto!=9:
        print("código invalido\n")
        codigo_produto=int(input("Dígite o código\n"))
    quant=int(input("Informe a quantidade\n"))
    if codigo_produto !=0 and codigo_produto==1:
        while codigo_produto !=0 and codigo_produto==1:
                soma+=quant*um
                codigo_produto+=1
    elif codigo_produto !=0  and codigo_produto==2:
       while codigo_produto !=0 and codigo_produto==2:
                soma+=quant*dois
                codigo_produto+=1
    elif codigo_produto !=0 and codigo_produto==3:
        while codigo_produto !=0 and codigo_produto==3:
                soma+=quant*tres
                codigo_produto+=1
    elif codigo_produto !=0 and codigo_produto==5:
        while codigo_produto !=0 and codigo_produto==5:
                soma+=quant*cinco
                codigo_produto+=1
        
    elif codigo_produto !=0 and codigo_produto==9:
        while codigo_produto !=0 and codigo_produto==9:
                soma+=quant*nove
                codigo_produto+=1
       
    
        
print("Total", soma)
   
