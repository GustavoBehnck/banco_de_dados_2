# Requisitos
- [Requisitos](#requisitos)
  - [Objetivo](#objetivo)
  - [Perguntas a serem respondidas através da interface](#perguntas-a-serem-respondidas-através-da-interface)
  - [Informações necessárias nos bancos de dados](#informações-necessárias-nos-bancos-de-dados)
    - [Banco não relacional (Dados de Telemetria)](#banco-não-relacional-dados-de-telemetria)
    - [Banco relacional (Dados de Negócio)](#banco-relacional-dados-de-negócio)

## Objetivo

O objetivo deste projeto é desenvolver um sistema para monitorar dados de rastreamento, históricos e atuais, dos serviços de aluguel de tratores autônomos. A plataforma incluirá o monitoramento de informações como trajetória, manutenções, consumo de energia, entre outros.

Adicionalmente, serão armazenados dados de negócio, que serão correlacionados aos dados de monitoramento para gerar relatórios e responder a questões pertinentes à operação.

## Perguntas a serem respondidas através da interface

1. Qual região se há o maior uso dos caminhões em 2025?
2. Qual os componentes com melhor e pior arrefecimento?
3. Qual o consumo médio de energia de cada componente?
4. Qual a duração da bateria em horas de um trator durante seu uso constante?
5. Qual o modelo de caminhão mais utilizados?
6. Qual a relação em porcentágem que uma batida gera uma manutenção?
7. Qual a média de quedas da conectividade dos tratores por mês?
8. Quais tipos de via acarretam e mais manutenções?

## Informações necessárias nos bancos de dados

### Banco não relacional (Dados de Telemetria)

- localização (GPS)
- temperatura dos componentes internos
- consumo de energia dos componentes
- bateria (tensão, corrente, vida útil)
- dados do ambiente da trajetória (temperatura, umidade e luz)
- odômetro
- sensor de impacto
- sensor de proximidade
- dados dos atuadores (freio, motor, pressão das rodas etc.)
- status da conectividade
- dados da via


### Banco relacional (Dados de Negócio)

- ID do veículo autônomo
- data de fabricação
- chassi
- Marca
- dados do dono
- serviço (Oque está levando)
- log de manutenção
