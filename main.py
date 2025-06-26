from extrator_vocabulario import extrator_vocabulario

caminho_arquivo = 'data/input/texto.txt'
caminho_saida = 'data/output/vocabulario.txt'

extrator = extrator_vocabulario(caminho_arquivo, caminho_saida)
extrator.extrair_vocabulario()
