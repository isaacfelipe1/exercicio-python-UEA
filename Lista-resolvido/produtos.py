

nome_produto=input("Informe o nome do produto\n")
quantidade_adiquirida=int(input("Informe a quantidade\n"))
preco=float(input("Digite o preço unitario\n"))
pagar=0
total_A_pagar=0
if quantidade_adiquirida<=5:
    pagar=(preco*2)/100
    total_A_pagar= preco-pagar
    print("Valor total", total_A_pagar)
    print("Desconto foi de ", pagar)
elif quantidade_adiquirida>5 and quantidade_adiquirida<=10:
    pagar=(preco*3)/100
    total_A_pagar= preco-pagar
    print("Valor total", total_A_pagar)
    print("Desconto foi de ", pagar)
elif quantidade_adiquirida>10:
    pagar=(preco*5)/100
    total_A_pagar= preco-pagar
    print("Valor total", total_A_pagar)
    print("Desconto foi de ", pagar)

