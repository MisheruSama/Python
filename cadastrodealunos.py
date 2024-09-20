resposta="sim"
soma=0
i=0
while(resposta=="sim" or resposta=="Sim"):
    nome=input("Digite o nome do aluno: ")
    idade=int(input("Digite a idade do aluno: "))
    soma+=idade
    resposta = input("Deseja continuar cadastrando ? Digite 'sim' ou 'não'\n")
    i+=1
print(f"Foram cadastrados {i} alunos.")
media = soma/i
print(f"A média da idade dos alunos é de {media:.0f} anos")
