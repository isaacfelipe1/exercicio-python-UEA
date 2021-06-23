#Crie um programa que converta duas temperaturas Fahrenheit para Celsius, depois informe a maior temperatura entre elas.
p_graus_Celsius=0
p1_graus_Celsius=0
primeiraTemperatura=int(input("Informe a primiera temperatura em Fahrenheit\n"))
p_graus_Celsius=(primeiraTemperatura-32)/1.8
print("Celsius ", p_graus_Celsius)
segunda_Temperatura=int(input("Informe a segunda temperatura em Fahrenheit\n"))
p1_graus_Celsius=(segunda_Temperatura-32)/1.8
print(p1_graus_Celsius)

if p_graus_Celsius>p1_graus_Celsius:
    print("A maior tempertura é a primeira com: \n", p_graus_Celsius)
elif p1_graus_Celsius>p_graus_Celsius:
    print("A segunda é maior com:\n", p1_graus_Celsius)
