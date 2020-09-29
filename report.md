# Novel Mining

## Data (.txt file)
- One Hundred Years of solitude, Gabriel G. Marquez


# Projeto final de programação





# Proposta de dissertação

## Introdução

- importancia da visualização
    - visualização para dados numericos, categoricos, mapas, etc
    - livros são umas das fontes de dados mais abundantes, porém não temos visualizaçoes adequadas
- Definir narrativa literaria
    - Estrutura da narração: personagens, tempo, espaço e conflito. https://pt.wikipedia.org/wiki/Modo_narrativo
- Caracteristicas
    - Numero de personagens, diferentes relacoes
- Progressão do conhecimento
- Relacionamentos dinamicos temporais
- Narrativas complexas em diferentes dimensoes (personagens, relacionamentos, nomes, informacoes)
- Divisão atual de narritivas por paginas, capitulo, posição é ineficiente
- Dificuldade de encontrar informaçoes -> marcações
- Text mining para extrair informaçoes do livro e apresentar ao leitor de forma a facilitar a procura por informaçoes desejadas
- Grafo de relacionamentos dinamico seguindo a progressao do livro
- Informacoes relevantes sobre os personagens
- Modelo genérico que deve funcionar para qualquer livro
- Extração de informações da narrativa sem necessidade de consulta a dados externos e curadoria manual

Escrever um livro é uma das maneiras mais antigas de se armazenar e compartilhar conhecimento que perdura até os dias de hoje. De acordo com um estudo feito por L. Taycher em 2010, existiam pelo menos 129 milhões de livros publicados no mundo inteiro \cite{noauthor_books_nodate} e, apenas no ano de 2012, foram publicados mais de 57 mil novos livros no Brasil \cite{noauthor_books_2020}.

Mais especificamente, livros de narrativas literárias são uma das formas de mídia física mais consumidas pelas pessoas, sendo de extrema importância no desenvolvimento sociocultural dos indivíduos. Estes permitem que histórias de qualquer pessoa atravessem as barreiras sociais, de distancia e tempo.

Apesar dos números anteriormente mencionados, a forma em que consumimos este material pouco mudou nos últimos anos. Estamos no processo de digitalização do livro físico, aumentando a acessibilidade e praticidade, mas a interação com a narrativa ainda é limitada pelas páginas que lemos.

Uma narrativa literária costuma conter diversos personagens que participam de uma história e se relacionam de diferentes maneiras. Relações familiares, de amizade e inimizade, entre outras, surgem ao longo da narrativa e possuem caráter dinâmico, podendo se alterar com o decorrer dos acontecimentos narrados.

Dadas essas características, podemos imaginar uma narrativa como uma rede de relacionamentos que pode ser modelada e apresentada visualmente. Com isso, podemos alias os estudos e técnicas das áreas de mineração e visualização de texto para extrair, processar e representar novas informações a partir das páginas de livros, tendo como objetivo enriquecer a experiência da leitura de um romance e engajar mais ainda o leitor na história em que ele se encontra.

Para alcançar tal objetivo, a ideia do projeto é criar uma ferramenta que possibilite a extração do grafo de relacionamentos de um texto literário, modelando de tal maneira que os nós e arestas do grafo são os personagens e seus relacionamentos respectivamente. O grafo poderá ser visualizado de forma dinâmica, acompanhando o momento da narrativa em que o usuário se encontra. Além dos relacionamentos, também será possível interagir com as entidades apresentadas no grafo para obter mais informações sobre a mesma, facilitando a descoberta e recuperação de conteúdo relevante sobre a história.

## Especificação

Neste capítulo, será apresentada a especificação do projeto com os requisitos propostos, casos de uso, informações sobre os dados utilizados, além de exemplos.

- Requisitos

Nesta seção, descrevemos os principais requisitos do projeto. Os requisitos do ponto de vista do usuário do sistema são os seguintes apresentados na tabela 1: visualização do grafo de relacionamentos de uma narrativa pré-definida; interface para escolha da página do livro na qual o usuário deseja consultar as informações; e a possibilidade de interação com as entidades do grafo para consulta de informações relevantes. Estes requisitos descrevem as funcionalidades que o sistema oferece ao usuário final.

Para que estes sejam alcançados, estabelecemos requisitos voltados para o processamento e mineração de texto que irão extrair e prover as informações a partir de uma narrativa. Estes requisitos são os seguintes apresentados na tabela 2: processamento do texto para que possa ser tratado no formato de páginas; extração de entidades do texto; desambiguação das entidades extraídas; estabelecimento das relações existentes entre as eentidades reconhecidas;agregação de informações relevantes para cada entidade; e associação das informações extraídas às páginas referentes.


- Casos de uso


- Dados utilizados


- Modelagem do grafo


- Exemplos

## Projeto
    - Arquitetura 
    - Processamento de texto
    - API (backend)
    - Visualizador (Frontend)
    Para cada um: objetivo, funcionamento, classes
    - Resultados

## Testes
    - Testes unitários
    - Teste de entrada e saida

## Conclusões

## Referencias
    - Livro
    - pandas
    - spacy
    - networkx
    - NOVEL2GRAPH

## Anexos



# Exemplo Alysson
- Introdução
- Especificação
    - Requisitos funcionais
    - Arquitetura
    - Sequencia de interaçoes
- Testes
    - Testes unitarios
    - Testes de entrada e saida
- Instalação do sistema
- Conclusoes
- Anexos



# Roteiro de PFP
- especificação do programa
    - objetivos, requisitos
    - especificação, por exemplo use-cases.
- projeto do programa
    - arquitetura
    - critérios de projeto utilizados
    - diagramas de arquitetura e/ou segmentação do programa, por exemplo UML.
    - organização do programa (componentes, módulos, classes,...), por exemplo
    diagramas de classe UML.
    - diagramas de organização dos dados, por exemplo diagramas de modelagem de dados, ou entidade e relacionamentos.
- código fonte cuidadosamente comentado
    - comentário inicial de cada módulo, identificando o autor
    - comentários cabeçalho de módulos, classes e funções
    - assertivas para dados e procedimentos, procure utilizar design by contract
    - pseudo instruções
    - procure estabelecer e/ou adotar padrões de programação.
- roteiro de teste efetuado, composto de:
    - critérios de teste utilizados
    - descrição dos casos de teste
    - na medida do possível procure utilizar testes automatizados, neste caso
    adicione os scripts de teste e os logs gerados pelo teste automatizado
- documentação para o usuário