n=int(input("Digite quantos elementos possui a lista: "))
lista = [0]*n
for i in range(n):
    lista[i] = int(input(f"Digite o {i+1}º valor: "))
print(sum(lista))
