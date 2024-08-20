# Sistema onde é pedido o salário por horas trabalhadas e a horas trabalhadas no mês e no fim 
# mostra o salário final a ser recebido no mês
salario=float(input("Digite o valor recebido por hora: "))
hora=int(input("Digite a quantidade de horas trabalhadas no mês: "))
totsalario = salario*hora
print("Seu salário total no mês foi de",totsalario,"reais")
