continua="s"
idade=[]
while(continua == "s" or continua == "S"):
    id=int(input(f"Digite a idade do aluno: "))
    idade.append(id)
    continua = input("Deseja continuar cadastrando? Digite 's' para sim e 'n' para não: ")
soma_idade=0
n=len(idade)
for i in range(n):
    soma_idade+=idade[i]
media_idade=soma_idade/n
print(f"Esta turma possui {n} alunos e a média de idade é: {media_idade:.1f}")
qmaior=qmenor=0
for i in range(n):
    if idade[i]>=18:
        qmaior+=1
    else:
        qmenor+=1
print(f"Na turma temos {qmaior} alunos maiores de idade e {qmenor} alunos menores de idade")