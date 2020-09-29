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


A visualização de dados é um dos métodos mais importantes parar se compor uma argumentação, documentar fatos, entre muitas outras tarefas que envolvem todo tipo de dados. Apesar da recente e crescente importância que tem se dado à área, existem registros de que os primeiros gráficos foram feitos por volta do século XV \cite{Friendly_06_hbook} e foram se desenvolvendo de acordo com o crescimento das áreas das ciências ao longo dos séculos seguintes.

Hoje, quando falamos de visualização de dados, logo pensamos em gráficos de funções, histogramas, gráficos em barras, além de muitos outros que tratam de dados numéricos e categóricos. Grande parte do acervo de visualizações é justamente voltada para esse tipo de dado, muito devido sua facilidade de representação considerandos as dimensões de grandeza, quantidade, proporção, e posição.

Por outro lado, quando começamos a estudar outros tipos de dados, como o textual, já não encontramos essa grande variedade e riqueza de métodos de visualização. Devido a sua natureza, dados textuais são muito mais dificeis de representar pois o seu valor está na semântica das palavras e conceitos. Uma das técnicas de visualização de texto mais conhecidas, a Nuvem de Palavras, começou a ser usada por volta dos anos 90, tendo como um dos primeiros registros um texto sobre tecnologias da época, por Douglas Coupland \cite{noauthor_tag_2020}. A Nuvem de Palavras, apesar de impactante, tem a sua capacidade de representação limitada, devido a sua forma e construção. Apesar de resolver parte do problema de representação de grandezas de dados textuais, esta técnica é limitada pois não consegue representar toda a riqueza de informações que um texto possui.

Desde então, outras técnicas foram desenvolvidas a fim de aumentar a capacidade de representação de informação textual. No estudo de Kucher et al. \cite{kucher_text_nodate}, foram categorizados diversas técnicas de vizualização de texto, criando-se uma taxonomia de técnicas que podem ser escolhidas de acordo com a necessidade e objetivos que devem ser alcançados. Uma das categorias de técnicas mencionda no estudo é a utilização de grafos, que, devido a sua construção, consegue fornecer novas dimensões de representação.

Para melhor representar a ideia de sequência e relação entre pedaços de informação, as técnicas com base em visualização de grafos começaram a ser utilizadas. Estas técnicas permitem a representação de entidades de informação textual, atreladas a relações que existem entre elas de maneiro simples de se visualizar. Além disso, elas também permitem a representação de grandezas, tanto para entidades, quanto para relacionamentos, incrementando o uso das Nuvens de Palavras.



Uma narrativa literária contém personagens que participam de uma história e se relacionam de diferentes maneiras. Relações familiares, de amizade e inimizade, entre outras, surgem ao longo da narrativa e possuem caráter dinâmico, podendo se alterar com o decorrer dos acontecimentos narrados.

A ideia do projeto criar uma ferramenta que possibilite a extração do grafo de relacionamentos de um texto literário, onde os nós e arestas do grafo são os personagens e seus relacionamentos respectivamente. O grafo poderá ser visualizado de forma dinâmica, acompanhando o momento da narrativa em que o usuário se encontra.