continua="s"
lista=[]
while(continua == "s" or continua == "S"):
    n=eval(input("Digite um número: "))
    lista.append(n)
    continua=input("Deseja continuar? Digite 's' para sim e 'n' para não: ")
print(lista)