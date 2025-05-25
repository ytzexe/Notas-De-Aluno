
# AQUI CRIAMOS UM DICIONÁRIO E ADICIONAMOS OS ALUNOS E SUAS NOTAS 
alunos = {
    "Lucas": {'matematica': [8.4, 10.0], 'portugues': [9.8, 7.0], 'ingles': [3.0, 8.0]},
    "Eduardo": {'matematica': [9, 10.0], 'portugues': [10.0, 8], 'ingles': [9.5, 10.0]},
    "Pedro": {'matematica': [2.0, 1.0], 'portugues': [3.5, 6.0], 'ingles': [4.0, 3.0]}
}
# AQUI ESTÁ A NOSSA FUNÇÃO DAS MÉDIAS DAS MATÉRIAS PROPORCIONADAS
def media_materia():
    for aluno, materias in alunos.items():
        print(f"\nAluno: {aluno}")
        for materia, notas in materias.items():
            media = sum(notas) / len(notas)
            print(f"Matéria: {materia} | Média: {media:.2f}")
# AQUI ESTÁ A NOSSA FUNÇÃO DA MÉDIA GERAL DOS ALUNOS 
def media_geral_aluno():
    medias_gerais = {}
    for aluno, materias in alunos.items():
        soma_total = 0
        quantidade_notas = 0
        for notas in materias.values():
            soma_total += sum(notas)
            quantidade_notas += len(notas)
        media_geral = soma_total / quantidade_notas
        medias_gerais[aluno] = media_geral
        print(f"\nAluno: {aluno} | Média Geral: {media_geral:.2f}")
    return medias_gerais
# CRIAMOS UMA FUNÇÃO DE MELHOR ALUNO 
def melhor_aluno(medias_gerais):
    aluno_top = max(medias_gerais, key=medias_gerais.get)
    maior_media = medias_gerais[aluno_top]
    print(f"\nO aluno com a maior média geral é {aluno_top}, com a média {maior_media:.2f}.")
# AQUI ESTÁ A NOSSA MÉDIA POR MATÉRIA DOS ALUNOS QUE NO CASO SÃO AS NOTAS FINAIS 
def media_por_materia():
    materias_totais = {}
    for materias in alunos.values():
        for materia, notas in materias.items():
            if materia not in materias_totais:
                materias_totais[materia] = []
            materias_totais[materia].extend(notas)

    print("\nMédia geral por matéria:")
    for materia, notas in materias_totais.items():
        media = sum(notas) / len(notas)
        print(f"{materia}: {media:.2f}")
# CRIAMOS TAMBÉM UMA FUNÇÃO PARA ADICIONAR AS NOTAS DOS ALUNOS, QUE JÁ ESTÃO CADASTRADOS 
def adicionar_notas():
    aluno = input("\nDigite o nome do aluno: ").strip().capitalize()
    if aluno not in alunos:
        print("Aluno não encontrado! Verifique o nome e tente novamente.")
        return

    materia = input("Digite o nome da matéria: ").strip().lower()
    if materia not in alunos[aluno]:
        print("Matéria não encontrada! Verifique o nome e tente novamente.")
        return

    try:
        nota = float(input("Digite a nota para adicionar: "))
        if 0 <= nota <= 10:
            alunos[aluno][materia].append(nota)
            print(f"Nota {nota:.2f} adicionada para {aluno} em {materia}.")
        else:
            print("A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Certifique-se de digitar um número.")

# CRIAMOS UM MENU DE OPÇÕES, SEJA PARA, ESCOLHER O ALUNO, VER AS NOTAS, INCLUSIVE AS NOTAS GERAIS E POR FIM ADICIONAR AS NOTAS DE ALUNOS
def menu():
    while True:
        print("\nMenu de Opções:")
        print("1 - Exibir média de cada matéria por aluno")
        print("2 - Exibir média geral de cada aluno")
        print("3 - Exibir aluno com maior média geral")
        print("4 - Exibir média geral por matéria")
        print("5 - Adicionar nota a um aluno")
        print("6 - Sair")
# AQUI CRIAMOS UM "INPUT" PARA ESCOLHER UMA OPÇÃO DE MÉDIA POR NOTAS, MATÉRIAS, MELHOR ALUNO E POR FIM ADICIONAR NOTAS 
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            media_materia()
        elif opcao == "2":
            medias_gerais = media_geral_aluno()
        elif opcao == "3":
            medias_gerais = media_geral_aluno()
            melhor_aluno(medias_gerais)
        elif opcao == "4":
            media_por_materia()
        elif opcao == "5":
            adicionar_notas()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executando o menu
menu()


"""PARTICIPANTES DO GRUPO:"""
#RAFAEL MARTINS 
#KAUÃ LUCAS
#EDUARDO HENRIQUE FERNANDES FERREIRA