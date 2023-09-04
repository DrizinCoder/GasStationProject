'''*******************************************************************************
Autor: Guilherme Fernandes Sardinha
Componente Curricular: Algoritmos e programação I
Concluido em: 26/08/2023
Sistema Operacional: Windows 11
Versão Python: 3.9.5
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************'''
'''Primeira parte do código foi destinada a criação das variáveis necessárias para o andamento do código e 
a criação de inputs para os Postos'''
sair_do_loop = 0
gasolina_a = 0
etanol_a = 0
diesel_a = 0
Posto_a = str(input('Digite o nome do posto: ').strip())
while type(gasolina_a) != float:
  gasolina_a = input('Digite o valor da gasolina: ').replace(',', '.')
  if gasolina_a.count(',') > 1 or gasolina_a.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if gasolina_a.replace(',', '').replace('.', '').isnumeric():
      gasolina_a = float(gasolina_a)
    else:
      print('Caracter invalido! Digite um NÚMERO\n.')
while type(etanol_a) != float:
  etanol_a = input('Digite o valor do etanol: ').replace(',', '.')
  if etanol_a.count(',') > 1 or etanol_a.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if etanol_a.replace(',', '').replace('.', '').isnumeric():
      etanol_a = float(etanol_a)
    else:
      print('Caracter invalido! Digite um NÚMERO.\n')
while type(diesel_a) != float:
  diesel_a = input('Digite o valor do diesel: ').replace(',', '.')
  if diesel_a.count(',') > 1 or diesel_a.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if diesel_a.replace(',', '').replace('.', '').isnumeric():
      diesel_a = float(diesel_a)
    else:
      print('Caracter invalido! Digite um NÚMERO.\n')
gasolina_b = 0
etanol_b = 0
diesel_b = 0
Posto_b = str(input('Digite o nome do posto: ').strip())
while type(gasolina_b) != float:
  gasolina_b = input('Digite o valor da gasolina: ').replace(',', '.')
  if gasolina_b.count(',') > 1 or gasolina_b.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if gasolina_b.replace(',', '').replace('.', '').isnumeric():
      gasolina_b = float(gasolina_b)
    else:
      print('Caracter invalido! Digite um NÚMERO.\n')
while type(etanol_b) != float:
  etanol_b = input('Digite o valor do etanol: ').replace(',', '.')
  if etanol_b.count(',') > 1 or etanol_b.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if etanol_b.replace(',', '').replace('.', '').isnumeric():
      etanol_b = float(etanol_b)
    else:
      print('Caracter invalido! Digite um NÚMERO.\n')
while type(diesel_b) != float:
  diesel_b = input('Digite o valor do diesel: ').replace(',', '.')
  if diesel_b.count(',') > 1 or diesel_b.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if diesel_b.replace(',', '').replace('.', '').isnumeric():
      diesel_b = float(diesel_b)
    else:
      print('Caracter invalido! Digite um NÚMERO.\n')
gasolina_c = 0
etanol_c = 0
diesel_c = 0
Posto_c = str(input('Digite o nome do posto: ').strip())
while type(gasolina_c) != float:
  gasolina_c = input('Digite o valor da gasolina: ').replace(',', '.')
  if gasolina_c.count(',') > 1 or gasolina_c.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if gasolina_c.replace(',', '').replace('.', '').isnumeric():
      gasolina_c = float(gasolina_c)
    else:
      print('Caracter invalido! Digite um NÚMERO.\n')
while type(etanol_c) != float:
  etanol_c = input('Digite o valor do etanol: ').replace(',', '.')
  if etanol_c.count(',') > 1 or etanol_c.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if etanol_c.replace(',', '').replace('.', '').isnumeric():
      etanol_c = float(etanol_c)
    else:
      print('Caracter invalido! Digite um NÚMERO.\n')
while type(diesel_c) != float:
  diesel_c = input('Digite o valor do diesel: ').replace(',', '.')
  if diesel_c.count(',') > 1 or diesel_c.count('.') > 1:
    print("caracter inválido! Digite apenas uma ',' ou um '.'.\n")
  else:
    if diesel_c.replace(',', '').replace('.', '').isnumeric():
      diesel_c = float(diesel_c)
    else:
      print('Caracter invalido! Digite um NÚMERO.\n')
Beneficio_gas_a = 0
Beneficio_gas_b = 0
Beneficio_gas_c = 0
Beneficio_eta_a = 0
Beneficio_eta_b = 0
Beneficio_eta_c = 0
Beneficio_dsel_a = 0
Beneficio_dsel_b = 0
Beneficio_dsel_c = 0
consultas = 0
menor_valor_posto_a = 0
menor_valor_posto_b = 0
menor_valor_posto_c = 0
litros = 0
Litros_a = 0
Litros_b = 0
Litros_c = 0
'''Menu criado para facilitar a interação com o usuário'''
print('''
-------------------------------------------------------------------------------
1- Qual combustivel desejado, quantos litros deseja e resultado.
2- Lista de todos os postos e o valor de seus combustiveis.
3- Sair do programa.
-------------------------------------------------------------------------------
''')
'''Laço de repetição utilizado para efetuar as operações, armazenar dados, comparar e mostrar as melhores
opções na tela do usuário de acordo com a sua escolha em relação ao menu.'''
resposta_menu = 0
while resposta_menu != 3:
  while sair_do_loop == 0:
    resposta_menu = input('Digite o número equivalente a consulta que deseja realizar: ')
    if resposta_menu.isnumeric():
      resposta_menu = int(resposta_menu)
      sair_do_loop += 1
    else:
      print('Opção inválida''\n')
  sair_do_loop -= 1
  if resposta_menu == 1:
    consultas += 1
    while sair_do_loop == 0:
      litros = input('Digite a quantidade de litros desejada: ').replace(',', '.')
      if litros.count(',') > 1 or litros.count('.') > 1:
        print("Digite apenas uma ',' ou um '.'\n")
      else:
        if litros.replace(',', '').replace('.', '').isnumeric():
          litros = float(litros)
          sair_do_loop += 1
        else:
          print('Caracter invalido! Digite um NÚMERO.\n')
    sair_do_loop -= 1
    print('''
    1- gasolina
    2- etanol
    3- diesel
    ''')
    while sair_do_loop == 0:
      combustivel = input('Digite o número do combustivel desejado: ')
      if combustivel.isnumeric():
        combustivel = int(combustivel)
        sair_do_loop += 1
      else:
        print('opção inválida.\n')
    sair_do_loop -= 1
    if combustivel == 1:
      Beneficio_gas_a = float(litros * gasolina_a)
      Beneficio_gas_b = float(litros * gasolina_b)
      Beneficio_gas_c = float(litros * gasolina_c)
      if gasolina_a <= gasolina_b and gasolina_a <= gasolina_c:
        menor_valor_posto_a +=1
        Litros_a += litros
        print(f'''o posto mais barato é o posto {Posto_a} e o valor de {litros} litros de gasolina
nesse posto é {round(Beneficio_gas_a, 2)}\n''')
        print(f'Em relação ao {Posto_b} está R$ ', round(Beneficio_gas_b - Beneficio_gas_a, 2), ' mais barato.')
        print(f'Em relação ao {Posto_c} está R$ ', round(Beneficio_gas_c - Beneficio_gas_a), ' mais barato.\n')
      if gasolina_b <= gasolina_a and gasolina_b <= gasolina_c:
        menor_valor_posto_b +=1
        Litros_b += litros
        print(f'''o posto mais barato é o posto {Posto_b} e o valor de {litros} litros de gasolina
nesse posto é {round(Beneficio_gas_b, 2)}\n''')
        print(f'Em relação ao {Posto_a} está R$ ', round(Beneficio_gas_a - Beneficio_gas_b, 2), ' mais barato.')
        print(f'Em relação ao {Posto_c} está R$ ', round(Beneficio_gas_c - Beneficio_gas_b, 2), ' mais barato.\n')
      if gasolina_c <= gasolina_a and gasolina_c <= gasolina_b:
        menor_valor_posto_c +=1
        Litros_c += litros
        print(f'''o posto mais barato é o posto {Posto_c} e o valor de {litros} litros de gasolina
nesse posto é {round(Beneficio_gas_c, 2)}\n''')
        print(f'Em relação ao {Posto_a} está R$ ', round(Beneficio_gas_a - Beneficio_gas_c, 2), ' mais barato.')
        print(f'Em relação ao {Posto_b} está R$ ', round(Beneficio_gas_b - Beneficio_gas_c, 2), ' mais barato.\n')
    elif combustivel == 2:
      Beneficio_eta_a = float(litros * etanol_a)
      Beneficio_eta_b = float(litros * etanol_b)
      Beneficio_eta_c = float(litros * etanol_c)
      if etanol_a <= etanol_b and etanol_a <= etanol_c:
        menor_valor_posto_a +=1
        Litros_a += litros
        print(f'''o posto mais barato é o posto {Posto_a} e o valor de {litros} litros de etanol nesse
posto é {round(Beneficio_eta_a, 2)}\n''')
        print(f'Em relação ao {Posto_b} está R$ ', round(Beneficio_eta_b - Beneficio_eta_a, 2), ' mais barato.')
        print(f'Em relação ao {Posto_c} está R$ ', round(Beneficio_eta_c - Beneficio_eta_a, 2), ' mais barato.\n')
      if etanol_b <= etanol_a and etanol_b <= etanol_c:
        menor_valor_posto_b +=1
        Litros_b += litros
        print(f'''o posto mais barato é o posto {Posto_b} e o valor de {litros} litros de etanol nesse
posto é {round(Beneficio_eta_b, 2)}\n''')
        print(f'Em relação ao {Posto_a} está R$ ', round(Beneficio_eta_a - Beneficio_eta_b,2 ), ' mais barato.')
        print(f'Em relação ao {Posto_c} está R$ ', round(Beneficio_eta_c - Beneficio_eta_b, 2), ' mais barato.\n')
      if etanol_c <= etanol_b and etanol_c <= etanol_a:
        menor_valor_posto_c +=1
        Litros_c += litros
        print(f'''o posto mais barato é o posto {Posto_c} e o valor de {litros} litros de etanol nesse
posto é {round(Beneficio_eta_c, 2)}\n''')
        print(f'Em relação ao {Posto_a} está R$ ', round(Beneficio_eta_a - Beneficio_eta_c, 2), ' mais barato.')
        print(f'Em relação ao {Posto_b} está R$ ', round(Beneficio_eta_b - Beneficio_eta_c, 2), ' mais barato.\n')
    elif combustivel == 3:
      Beneficio_dsel_a = float(litros * diesel_a)
      Beneficio_dsel_b = float(litros * diesel_b)
      Beneficio_dsel_c = float(litros * diesel_c)
      if diesel_a <= diesel_b and diesel_a <= diesel_c:
        menor_valor_posto_a +=1
        Litros_a += litros
        print(f'''o posto mais barato é o posto {Posto_a} e o valor de {litros} litros de diesel nesse
posto é {round(Beneficio_dsel_a, 2)}.\n''')
        print(f'Em relação ao {Posto_b} está R$ ', round(Beneficio_dsel_b - Beneficio_dsel_a, 2), ' mais barato.')
        print(f'Em relação ao {Posto_c} está R$ ', round(Beneficio_dsel_c - Beneficio_dsel_a, 2), ' mais barato.\n')
      if diesel_b <= diesel_a and diesel_b <= diesel_c:
        menor_valor_posto_b +=1
        Litros_b += litros
        print(f'''o posto mais barato é o posto {Posto_b} e o valor de {litros} litros de diesel nesse
posto é {round(Beneficio_dsel_b, 2)}\n''')
        print(f'Em relação ao {Posto_a} está R$ ', round(Beneficio_dsel_a - Beneficio_dsel_b, 2), ' mais barato.')
        print(f'Em relação ao {Posto_c} está R$ ', round(Beneficio_dsel_c - Beneficio_dsel_b, 2), ' mais barato.\n')
      if diesel_c <= diesel_b and diesel_c <= diesel_a:
        menor_valor_posto_c +=1
        Litros_c += litros
        print(f'''o posto mais barato é o posto {Posto_c} e o valor de {litros} litros de diesel nesse
posto é {round(Beneficio_dsel_c, 2)}\n''')
        print(f'Em relação ao {Posto_a} está R$ ', round(Beneficio_dsel_a - Beneficio_dsel_c, 2), ' mais barato.')
        print(f'Em relação ao {Posto_b} está R$ ', round(Beneficio_dsel_b - Beneficio_dsel_c, 2), ' mais barato.\n')
    else: 
      print('opção inválida. Consulta desconsiderada, realize uma nova consulta.\n')
      consultas -= 1
  elif resposta_menu == 2:
    consultas += 1
    print(f'''
    -------------------------------------------------------------------------------
    {Posto_a}
    Valor da gasolina: R$ {gasolina_a}
    Valor do etanol: R$ {etanol_a}
    Valor do diesel: R$ {diesel_a}

    {Posto_b}
    Valor da gasolina: R$ {gasolina_b}
    Valor do etanol: R$ {etanol_b}
    Valor do diesel: R$ {diesel_b}

    {Posto_c}
    Valor da gasolina: R$ {gasolina_c}
    Valor do etanol: R$ {etanol_c}
    Valor do diesel: R$ {diesel_c}
    -------------------------------------------------------------------------------
    ''')
  elif resposta_menu == 3:
    print('Aqui está o relatório das pesquisas:\n')
  else:
    print('Opção inválida. Digite uma opção presente na tabela.''\n')
'''Primeira parte do relatório onde são mostradas as consultas e o número de vezes que o posto possuiu menor
valor de combustivel.'''
print(f'Você realizou {consultas} consultas.''\n')
print(f'{Posto_a} teve o menor valor de combustivel {menor_valor_posto_a} vezes.')
print(f'{Posto_b} teve o menor valor de combustivel {menor_valor_posto_b} vezes.')
print(f'{Posto_c} teve o menor valor de combustivel {menor_valor_posto_c} vezes.''\n')
'''Parte do relatório que mostra a média de litros consultados por posto e resolvendo o erro 
da divisão por 0.'''
if menor_valor_posto_a == 0:
  menor_valor_posto_a += 1
  print(f'média de litros do {Posto_a} é 0')
else:
  print(f'A média de litros do {Posto_a} é igual a', round(Litros_a / menor_valor_posto_a, 2))
if menor_valor_posto_b == 0:
  menor_valor_posto_b += 1
  print(f'média de litros do {Posto_b} é 0')
else:
  print(f'A média de litros do {Posto_b} é igual', round(Litros_b / menor_valor_posto_b, 2))
if menor_valor_posto_c == 0:
  menor_valor_posto_c += 1
  print(f'média de litros do {Posto_c} é 0')
else:
  print(f'A média de litros do {Posto_c} é igual', round(Litros_c / menor_valor_posto_c, 2), '\n')

'''Parte do relatório que mostra o posto que possui o valor mais caro e mais barato de cada combustivel.'''
if gasolina_a >= gasolina_b >= gasolina_c:
  print(f'''A gasolina mais cara é a do {Posto_a} custando R$ {gasolina_a},
entretando a gasolina mais barata é a do {Posto_c} custando R${gasolina_c}.\n''')
elif gasolina_a >= gasolina_c >= gasolina_b:
  print(f'''A gasolina mais cara é a do {Posto_a} custando R$ {gasolina_a},
entretando a gasolina mais barata é a do {Posto_b} custando R$ {gasolina_b}.\n''')
elif gasolina_b >= gasolina_a >= gasolina_c:
  print(f'''A gasolina mais cara é a do {Posto_b} custando R$ {gasolina_b},
entretando a gasolina mais barata é a do {Posto_c} custando R$ {gasolina_c}.\n''')
elif gasolina_b >= gasolina_c >= gasolina_a:
  print(f'''A gasolina mais cara é a do {Posto_b} custando R$ {gasolina_b},
entretando a gasolina mais barata é a do {Posto_a} custando R$ {gasolina_a}.\n''')
elif gasolina_c >= gasolina_a >= gasolina_b:
  print(f'''A gasolina mais cara é a do {Posto_c} custando R$ {gasolina_c},
entretando a gasolina mais barata é a do {Posto_b} custando R$ {gasolina_b}.\n''')
elif gasolina_c >= gasolina_b >= gasolina_a:
  print(f'''A gasolina mais cara é a do {Posto_c} custando R$ {gasolina_c},
entretando a gasolina mais barata é a do {Posto_a} custando R$ {gasolina_a}.\n''')

if etanol_a >= etanol_b >= etanol_c:
  print(f'''o etanol mais caro é o do {Posto_a} custando R$ {etanol_a},
entretando o etanol mais barato é a do {Posto_c} custando R$ {etanol_c}.\n''')
elif etanol_a >= etanol_c >= etanol_b:
  print(f'''o etanol mais caro é o do {Posto_a} custando R$ {etanol_a},
entretando o etanol mais barato é a do {Posto_b} custando R$ {etanol_b}.\n''')
elif etanol_b >= etanol_a >= etanol_c:
  print(f'''o etanol mais caro é o do {Posto_b} custando R$ {etanol_b},
entretando o etanol mais barato é a do {Posto_c} custando R$ {etanol_c}.\n''')
elif etanol_b >= etanol_c >= etanol_a:
  print(f'''o etanol mais caro é o do {Posto_b} custando R$ {etanol_b},
entretando o etanol mais barato é a do {Posto_a} custando R$ {etanol_a}.\n''')
elif etanol_c >= etanol_a >= etanol_b:
  print(f'''o etanol mais caro é o do {Posto_c} custando R$ {etanol_c},
entretando o etanol mais barato é a do {Posto_b} custando R$ {etanol_b}.\n''')
elif etanol_c >= etanol_b >= etanol_a:
  print(f'''o etanol mais caro é o do {Posto_c} custando R$ {etanol_c},
entretando o etanol mais barato é a do {Posto_a} custando R$ {etanol_a}.\n''')

if diesel_a >= diesel_b >= diesel_c:
  print(f'''o diesel mais caro é o do {Posto_a} custando R$ {diesel_a},
entretando o diesel mais barato é a do {Posto_c} custando R$ {diesel_c}.\n''')
elif diesel_a >= diesel_c >= diesel_b:
  print(f'''o diesel mais caro é o do {Posto_a} custando R$ {diesel_a},
entretando o diesel mais barato é a do {Posto_b} custando R$ {diesel_b}.\n''')
elif diesel_b >= diesel_a >= diesel_c:
  print(f'''o diesel mais caro é o do {Posto_b} custando R$ {diesel_b},
entretando o diesel mais barato é a do {Posto_c} custando R$ {diesel_c}.\n''')
elif diesel_b >= diesel_c >= diesel_a:
  print(f'''o diesel mais caro é o do {Posto_b} custando R$ {diesel_b},
entretando o diesel mais barato é a do {Posto_a} custando R$ {diesel_a}.\n''')
elif diesel_c >=diesel_a >= diesel_b:
  print(f'''o diesel mais caro é o do {Posto_c} custando R$ {diesel_c},
entretando o diesel mais barato é a do {Posto_b} custando R$ {diesel_b}.\n''')
elif diesel_c >= diesel_b >= diesel_a:
  print(f'''o diesel mais caro é o do {Posto_c} custando R$ {diesel_c},
entretando o diesel mais barato é a do {Posto_a} custando R$ {diesel_a}.\n''')
#Fim do Código