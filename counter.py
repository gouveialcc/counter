from encodings import utf_8
import encodings

f = open('contador.txt', 'r')
conteudo = f.readlines()

print(conteudo)

contagem = len(conteudo.split())

print(f"Existe(m) ", str(contagem) ," palavra(s) no seu arquivo.")