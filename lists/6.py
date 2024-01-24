medias_alunos = []
for i in range(10):
    notas = [float(input(f"Informe a {j + 1}ª nota do aluno {i + 1}: ")) for j in range(4)]
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
