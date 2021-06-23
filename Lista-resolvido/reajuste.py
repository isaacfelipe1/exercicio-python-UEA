#Escreva um programa que receba um salário, aplique um reajuste de 35%, e depois desconte 27% do novo salário.
reajuste_salario=0
salario=float(input("Informe seu salário\n"))
reajuste=(salario *35)/100
reajuste_salario= salario+reajuste
print("Salário com Aumento é de  R$", reajuste_salario)
print("\n________Desconto do salário_______________\n")
desconte_reajuste=(reajuste_salario*27)/100
print(desconte_reajuste)
reajuste_salario_desconto=reajuste_salario-desconte_reajuste
print("Salário com desconto e de  R$: ", reajuste_salario_desconto)
