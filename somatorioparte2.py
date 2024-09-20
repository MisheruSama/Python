somatorio=0
i = int(input("Quantos numeros serão digitados: "))
for i in range(1, i+1):
    num=int(input(f"Digite o {i}º numero: "))
    somatorio+=num
print(f"O somatorio foi {somatorio}")