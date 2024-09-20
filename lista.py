lista = [0]*10
soma = 0
for i in range(10):
    lista[i] = int(input(f"Digite o {i+1}º numero: "))
    soma+=lista[i]
print("Os números digitados foram: ")
print(lista)
print(f"O somatório é {soma}") 