# 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.

# O Desafio

O CEO Guerra foi recém contratado e precisa entender melhor o negócio
para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards, a partir dessas análises, para responder
às seguintes perguntas:

## Geral:

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## País:

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária
distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Cidades:

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
aceitam pedidos online?

## Restaurantes:

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os
restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
possuem um valor médio de prato para duas pessoas maior que as churrascarias
americanas (BBQ)?

## Tipos de Culinárias:

1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
online e fazem entregas?

# 2. Premissas assumidas para análise

### 1. O conjunto de dados que representa o contexto está disponível na plataforma Kaggle.

### 2. Ao observar os dados, inicialmente, foram tomadas as seguintes ações:

1. As 4 principais visões do negócio foram: Visão geral, visão países, visão cidades e visão cozinhas.
2. Colocar o nome dos países com base no código de cada país.
3. Criar a categoria do tipo de comida com base no range de valores.
4. Renomear as colunas do Dataframe.

# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem
as 4 principais visões do modelo de negócio da empresa:

1. Visão geral da empresa.
2. Visão dos países.
3. Visão das cidades.
4. Visão dos tipos de culinárias.

Cada visão é representada pelo seguinte conjunto de métricas:

1. Visão geral
    1. Quantidade de restaurantes cadastrados no dataframe.
    2. Quantidade de países cadastrados no dataframe.
    3. Quantidade de cidades cadastradas no dataframe.
    4. Quantidade de avaliações feitas na plataforma.
    5. Quantidade dos tipos de culinárias no dataframe.
    6. Mapa interativo de geolocalização mostrando os restaurantes cadastrados na plataforma e seus dados.
2. Visão dos países
    1. Quantidade de restaurantes registrados por país.
    2. Quantidade de cidades registradas por país.
    3. Média de avaliações feitas por país.
    4. Média de preço de um prato para duas pessoas por país.
    5. Filtro para selecionar todos os países.
3. Visão das cidades
    1. Top 10 cidades com mais restaurantes na base de dados.
    2. Top 7 cidades com restaurantes que possuem a média de avaliação acima de 4.
    3. Top 7 cidades com restaurantes que possuem a média de avaliação abaixo de 2.5.
    4. Top 10 cidades que possuem mais restaurantes com tipos culinários distintos.
4. Visão tipos de cozinhas
    1. Métrica dos restaurantes mais bem avaliados por tipo de culinária.
    2. Filtro interativo dos restaurantes mais bem avaliados.
    3. Filtro interativo dos melhores tipos de culinárias.
    4. Filtro interativo dos piores tipos de culinárias.

# 4. Top Insights dos dados

1. Indonésia é o país, na média, com maior nota média de avaliações.
2. Indonésia é o país com o maior custo médio de um prato para duas pessoas.
3. Brasil é o país com menor nota na média de avaliações, apesar de estar entre os países que mais possuem restaurantes.
4. Índia é o país que mais possui restaurantes cadastrados, melhores notas de avaliação e com mais tipos de culinárias.
5. A cidade que possui restaurantes com as melhores avaliações é Londres.
6. A cidade que possui restaurantes com as piores avaliações é Gangtok.
7. Adelaide é a cidade que possui o maior custo de um prato para dois.
8. O restaurante que possui a maior nota média de avaliação é o "Mendokoro Ramenba", do tipo de culinária japonesa.
9. O restaurante que possui o maior custo de um prato para dois é "d'Arry's Verandah Restaurant".
10. Restaurantes que aceitam pedidos online são os que mais possuem avaliações registradas.
11. Restaurantes que fazem reservas são os que possuem o maior custo de um prato para duas pessoas.
12. O tipo de culinária que possui o maior custo de prato para dois é o "Modern Australian"

# 5. O produto final do projeto

O painel pode ser acessado através desse link: https://projeto-final-ftc-brunno.streamlit.app

# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas interativas que
exibam essas métricas da melhor forma possível para o CEO.