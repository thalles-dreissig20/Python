"""Um programa que leia o nome, ano de nascimento e a carteira de trabalho
e cadastreo com a (idade) em um dicionario se por acaso o ctps for diferente
de zero, o dicionario receberá tambem o ano de contratação e o salario. Calcule
e acrescente além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import datetime

dados = {}
dados['nome'] = str(input("digite o nome: "))
nasc = int(input("idade: "))
dados['nasc'] = datetime.now().year - nasc
dados['ctps'] = int(input("carteira de trabalho: "))
if dados['ctps'] != 0:
    dados['contratacão'] = int(input("ano de contrato: "))
    dados['salario'] = float(input("salario: R$"))
    dados['aposentadoria'] = dados['nasc'] + ((dados['contratacão'] + 35) - datetime.now().year)
print("="*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
