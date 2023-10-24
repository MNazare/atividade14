# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("qual o valor do salario?"))
if salario > 1250.00:
    aumento = 10
elif salario < 1250.00:
  aumento = 15
bonus = (aumento * salario)/100
novosalario = salario + bonus
print(f"salario atual: {salario}")
print(f"aumento: {aumento}%")
print(f"novo salario:{novosalario} ")
