# Boas Vindas ao Repositório do Projeto TING!

 # O que foi desenvolvido 
 
 O objetivo deste projeto foi desenvolver um programa que simule um algoritmo de indexação de documentos semelhante ao utilizado pelo Google. O programa é capaz de identificar ocorrências de termos em arquivos TXT, proporcionando uma funcionalidade de busca eficiente.

O projeto será dividido em dois módulos principais:

## Módulo de Gerenciamento de Arquivos:

- Este módulo permite o anexo de arquivos de texto no formato TXT.
- Será responsável pelo armazenamento e organização dos arquivos anexados.

## Módulo de Buscas:

- O módulo de buscas opera as funções de busca nos arquivos anexados.
- É capaz de identificar ocorrências de termos específicos nos documentos.

O foco principal do projeto é a indexação e a busca por ocorrências exatas de termos nos arquivos TXT. Não é abordada a análise de significados ou busca por sinônimos.

## Habilidades que foram necessárias:

- Manipular Pilhas;
- Manipular Deque;
- Manipular Nó & Listas Ligadas;
- Manipular Lista Duplamente Ligadas;

<details><summary> Para Clonar e Testar a Aplicação</summary>
<br>

1. Para clonar a aplicação:

```
git clone git@github.com:georgia-rocha/TING.git
```

2. Para entrar no diretório do projeto:
```
 cd TING
```

3.  Para criar um ambiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Executar os testes:
```
python3 -m pytest
```
O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

```bash
python3 -m pytest -s -vv
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nome_do_arquivo.py
```

Caso precise executar apenas uma função de testes basta executar o comando:

```bash
python3 -m pytest -k nome_da_func_de_tests
```

Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

```bash
python -m pytest -x tests/test_jobs.py
```

Para executar um teste específico de um arquivo, basta executar o comando:

```bash
python -m pytest -x tests/nome_do_arquivo.py::test_nome_do_teste
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).
</details>


## Requisitos 100%

- [x] 1 - Implementar uma fila para armazenar os arquivos que serão lidos.
- [x] 2 - Implementar uma função txt_importer dentro do módulo file_management capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.
- [x] 3 - Implementar a função process no módulo file_process. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função txt_importer em um dicionário que será armazenado dentro da Queue.
- [x] 4 - Implementar uma função remove dentro do módulo file_process capaz de remover o primeiro arquivo processado
- [x] 5 - Implementar uma função file_metadata dentro do módulo file_process capaz de apresentar as informações superficiais de um arquivo processado.
- [x] 6 - Implementar os testes para a classe PriorityQueue capaz de armazenar arquivos pequenos de forma prioritária
- [x] 7 - Implementar uma função exists_word, dentro do módulo word_search, que verifique a existência de uma palavra em todos os arquivos processados.
- [x] 8 - Implementar uma função search_by_word dentro do módulo word_search, que busque uma palavra em todos os arquivos processados.
