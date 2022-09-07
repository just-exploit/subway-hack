import re, os

valor = str(input('Digite o valor desejado, de moedas: '))

padrao = r'\\"1\\":{\\"value\\":[0-9]*'
novopadrao = r'\\"1\\":{\\"value\\":' + valor

with open('original_files/wallet.json', 'r') as file:
  conteudo = file.read()
  file.close()

novoconteudo = re.sub(padrao, novopadrao, conteudo)

with open('modified_files/wallet.json', 'w') as file:
  file.write(novoconteudo)
  file.close()


