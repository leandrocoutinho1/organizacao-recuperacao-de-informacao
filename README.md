# Extrator de Vocabulário e Bag of Words

Este projeto em Python realiza a extração de um vocabulário a partir de um texto de entrada e gera uma representação **Bag of Words** para um documento com base nesse vocabulário.

## 📁 Estrutura de Arquivos

```bash
├── main.py
├── extrator_vocabulario.py
├── data
│ ├── input
│ │ ├── texto.txt # Texto usado para gerar o vocabulário
│ │ └── documento.txt # Documento a ser representado como Bag of Words
│ └── output
│ └── vocabulario.txt # Vocabulário extraído
```

## 🚀 Como Funciona

### 1. Geração do Vocabulário

- O conteúdo de `texto.txt` é lido.
- Os acentos são removidos e as letras são convertidas para minúsculas.
- Palavras repetidas são eliminadas.
- O vocabulário resultante é ordenado e salvo em `vocabulario.txt`.

### 2. Geração da Bag of Words

- O conteúdo de `documento.txt` é lido e processado da mesma forma.
- Para cada palavra do vocabulário, é verificado se ela está presente no documento.
- Um vetor binário é gerado: `1` se a palavra estiver presente, `0` caso contrário.

### Exemplo de Saída

```python
[1, 0, 0, 1, 1, 0, 0, 1, ...]
```
### 📌 Como Executar
Certifique-se de que você tenha os arquivos necessários em data/input e execute:

```python
python main.py
```

🛠️ Dependências
- unidecode

Para instalar, use:

```bash
pip install unidecode
```

### ✍️ Autor
Leandro Coutinho Cesário Júnior - 12421BSI355
