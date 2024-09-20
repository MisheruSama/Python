soma=0
n = int(input("Quantos alunos tem na turma: "))
for i in range(1,n+1):
    nome = input(f"Digite o nome do {i}º aluno: ")
    idade = int(input(f"Digite a idade do {i}º aluno: "))
    soma+=idade
media=soma/n
print(f"A média da idade da turma é {media:.0f} anos")
