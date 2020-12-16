# PF Estágio
Este arquivo contém as explicações dos algoritmos elaborados como solução para os problemas dados

## Problema 1
Dado uma lista de dicionários (chave/valor) Python, verifique se existe a chave 'nome', e caso exista, salve o valor dessa chave em uma segunda lista, de modo que não haja repetição de valores na segunda lista.

### Solução

#### A lógica consiste em:
- Iterar sobre a lista;
- Se tiver a chave adiciona o contéudo da chave num set;
- Retorna uma lista criada a partir do set;

### Pontos chave:
- 
```python
if "nome" in x
```
garante que só os dicts que tiverem a chave "nome" terão o contéudo adicionado ao set.
- O set evita repetições.

## Problema 2
Dado um arquivo csv com delimitador ';' e com o seguinte cabeçalho: id;nome;telefone;idade. 
Retorne uma lista com os registro ordenados por nome.

### Solução
#### A lógica consiste em:
- Abrir o arquivo;
- Ler a primeira linha do arquivo e jogar fora;
- Ler o restante das linhas do arquivo até o EOF;
- Para cada linha:
    - Substituir os ';' por '\n'
    - Dividir a linha em uma lista de strings cada
    - Inserir os elementos dessa lista num dict
    - Inserir o dict na lista de resposta
- Fechar o arquivo
- Ordenar a lista utilizando o nome como chave de ordenação
- Retornar a lista de resposta

#### Pontos chave:

- A função retorna uma lista de dicionários em que cada dicionário possui as mesmas chaves referente ao cabeçalho do arquivo