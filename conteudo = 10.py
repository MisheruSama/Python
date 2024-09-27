n = int(input("Quanto produtos serão cadastrados: "))
suf=ale=abid=0
for i in range(1,n+1):
    prod=input("Digite o nome do produto: ")
    quantprod=int(input("Digite a quantidade de itens do produto cadastrado: "))
    if quantprod>=100:
        print(f"A quantidade de itens do produto {prod} é suficiente no estoque.")
        suf+=1
    elif quantprod>=50:
        print(f"A quantidade de itens do produto {prod} está em alerta.")
        ale+=1
    else:
        print(f"A quantidade de itens do produto {prod} está abaixo do ideal.")
        abid+=1
print(f"A quantidade de produtos com itens suficientes foram {suf}, a quantidade de produtos em que os itens estavam em alerta {ale} e a quantidade de produtos que estavam abaixo do ideal foram {abid}")