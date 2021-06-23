#Escreva um programa que leia números inteiros do teclado. O programa
#deve ler os números até que o usuário digite 0 (zero). No final da execução,exiba a quantidade de números digitados, assim como a soma e a média aritmética.
#cont=0
#media=0.0
#quant=0
#while True:
    n=int(input("Dígite um número\n"))
    cont+=n
    if n!=0:
        quant=quant+1
        media=cont/quant
    if n==0:
        break
print(" A quantidade números digitado\n", quant)
print("A soma dos números Dígitados\n",cont)
print("Média desses números Dígitados %5.2f\n" %media)
n+=1


