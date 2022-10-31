"""
Faça um programa que leia o nome e 3 notas de vários alunos e guarde em uma lista 
composta. No final mostre um boletim contendo a média de cada aluno e permita que 
sejam consultadas todas as notas parciais de cada aluno.
"""

lista = [] 
while True:
    nome = input('Nome do aluno: ')
    nota1 = float(input('Digite a 1° nota: '))
    nota2 = float(input('Digite a 2° nota: '))
    nota3 = float(input('Digite a 3° nota: ')) 
    lista_aluno = [nome, nota1, nota2, nota3]
    lista.append(lista_aluno)
    cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
        
print('-'*40) 
print('-=' *5,' Média dos alunos ','-='*5) 
print('-'*40)
print(f'{"NOME":^15} {"MÉDIA":>15}')
print('-'*40)
for pos,n in enumerate(lista):
    media = (n[1] + n[2] + n[3]) / 3
    print(f'{pos+1} > {n[0]:<15}{media:>10}')
print('-'*40)

while True:
    p = int(input('Mostrar notas de qual aluno? [999 para encerrar] '))
    if p == 999:
        print('Encerrando...')
        print('-=' *5,' Volte sempre! ','-='*5)  
        break
    if len(lista) >= p > 0:
        print(len(lista), p) 
        print(f'{lista[p-1][0]} tirou notas {lista[p-1][1]}, {lista[p-1][2]}, {lista[p-1][3]}')
    else:
        print('  Aluno não encontrado  ') 
