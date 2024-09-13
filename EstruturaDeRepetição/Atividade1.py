"""Faça um programa que calcule a média de salários de uma empresa, pedindo ao usuário a quantidade de funcionários,
o nome e o salário de cada funcionário e devolvendo a média, 
o salário mais alto e o salário mais baixo."""

quantid=int(input("quantidade de funcionarios: "))
for contador in range (0,quantid,1):
    salario = float(input("Informe o salario: "))
    soma= soma+salario
    media= contador/salario
    print("contador= ",contador)
print("quantid= ",quantid)



