#Faça um programa que verifica se um valor inteiro e positivo é primo. A rotina deve retornar um valor lógico determinando se o valor é primo ou não. Um valor primo é aquele que possui apenas 2 divisores: o número 1 e próprio valor. O primeiro valor primo é 2 (divisores: 1 e 2).
#Obs: O valor de entrada não pode ser 1, o programa deve repetir a pergunta até o número digitado ser maior que 1.

numero=int(input("Digite um valor maior que 1\n"))
total=0
while numero==1:
    numero=int(input("Digite um valor maior que 1\n"))
for c in range(1,numero+1):
    if numero%c==0:
        total+=1
if total==2:
     print("é primo")
else:
    print("Não é primo")
 
