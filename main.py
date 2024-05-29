from media import*
from verificacao import ano
def sistema():
    nome = input('Digite seu nome \n')
    Ano= input('Digite sua Serie \n')

    notas = []
    while len(notas) < 5:
     notas.append  (int(input('Digite a sua nota \n')))
    media1 = media2(notas)
    print('A media do aluno é:', media1)
    print(f'O aluno {nome}')
    ano(media1)


sistema()