
aluno_media = {
    'Alice': 7.8, 'Bruno': 6.5, 'Carlos': 9.1, 'Diana': 5.4,
    'Eduardo': 8.3, 'Fernanda': 7.6, 'Gustavo': 5.9, 'Helena': 9.4,
    'Igor': 6.7, 'Julia': 8.0, 'Karen': 5.8, 'Lucas': 7.2,
    'Mariana': 9.0, 'Nicolas': 6.3, 'Olivia': 7.5
}
for aluno,media in aluno_media.items():
    if media >= 7:
        print(f'Aluno : {aluno}, Media :{media} - Aprovado')
    else:
        print(f'Aluno : {aluno}, Media {media} - Reprovado')