from unidecode import unidecode

class extrator_vocabulario:
    def __init__(self, caminho_arquivo, caminho_saida):
        self.caminho_arquivo = caminho_arquivo
        self.caminho_saida = caminho_saida

    def ler_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return conteudo
        
    def salvar_arquivo(self, vetor_palavras):
        with open(self.caminho_saida, 'w', encoding='utf-8') as arquivo:
            arquivo.write('\n'.join(vetor_palavras))


    def extrair_vocabulario(self):
        texto_extraido = unidecode(self.ler_arquivo(self.caminho_arquivo)).replace("\n", " ").lower().split(" ")
        if(texto_extraido[-1] == ""):
            texto_extraido.pop()
        vetor_palavras = list(set(texto_extraido))
        vetor_palavras.sort()

        self.salvar_arquivo(vetor_palavras)

    def gerar_bag_of_words(self, caminho_documento):
        bag_of_words = []

        documento = unidecode(self.ler_arquivo(caminho_documento)).lower()

        vocabulario = self.ler_arquivo(self.caminho_saida)
        vocabulario = vocabulario.split("\n")

        for palavra in vocabulario:
            bag_of_words.append(1 if palavra in documento else 0)
        
        print(bag_of_words)
