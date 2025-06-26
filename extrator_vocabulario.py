from unidecode import unidecode

class extrator_vocabulario:
    def __init__(self, caminho_arquivo, caminho_saida):
        self.caminho_arquivo = caminho_arquivo
        self.caminho_saida = caminho_saida

    def ler_arquivo(self):
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return conteudo
        
    def salvar_arquivo(self, vetor_palavras):
        with open(self.caminho_saida, 'w', encoding='utf-8') as arquivo:
            for palavra in vetor_palavras:
                arquivo.write(palavra + '\n')
    
    def extrair_vocabulario(self):
        texto_extraido = unidecode(self.ler_arquivo()).replace("\n", " ").lower().split(" ")
        vetor_palavras = list(set(texto_extraido))
        vetor_palavras.sort()

        self.salvar_arquivo(vetor_palavras)



caminho_arquivo = 'data/input/texto.txt'
caminho_saida = 'data/output/vocabulario.txt'

extrator = extrator_vocabulario(caminho_arquivo, caminho_saida)
extrator.extrair_vocabulario()