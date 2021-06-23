preco_mercadoria=float(input("Informe o preço de mercadoria\n"))
percentual_DE_Desconto=float(input("Informe o percentual de desconto\n"))
percentagem_Do_Desconto=(preco_mercadoria* percentual_DE_Desconto)/100
preco_De_Desconto=preco_mercadoria- percentagem_Do_Desconto

print("Preço com desconto da percentagem : ", preco_De_Desconto)