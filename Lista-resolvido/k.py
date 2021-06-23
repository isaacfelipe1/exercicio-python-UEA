# Faça um algoritmo para:
#a) Ler um valor k qualquer
#b) Calcular T, como segue abaixo:
#T = (k+1) + (k+2) + (k+3) + (k+4) + (k+5) + ... + (k+100)
k=int(input("Digite um valor\n"))
print("")
t=1
for t in range(1,10):
    result=k+t
    print(result)
    
