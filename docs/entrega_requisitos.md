# Documentação dos requisitos

- [Documentação dos requisitos](#documentação-dos-requisitos)
  - [Introdução (Sinopse)](#introdução-sinopse)
  - [Definições Conceituais](#definições-conceituais)
    - [Requisitos Funcionais](#requisitos-funcionais)
    - [Requisitos não Funcionais](#requisitos-não-funcionais)
  - [Escopo do Projeto](#escopo-do-projeto)
  - [Requisitos Funcionais:](#requisitos-funcionais-1)
  - [Requisitos Não Funcionais:](#requisitos-não-funcionais-1)


## Introdução (Sinopse)

A companhia `Grão Mestre` se especializou em veículos autônomos em 2032, migrando para o ramo de tratores agrícolas em 2035, quando adotou o nome atual. O serviço oferecido pela empresa consiste em disponibilizar veículos de grande porte para trabalho agrícola em fazendas para pessoas jurídicas.

Mais do que fornecer o hardware das máquinas, oferecemos o sistema que as gerencia, para que realizem da maneira mais inteligente os trabalhos agendados. Além disso, as máquinas são preparadas para permitir que não apenas executem o trabalho nas rotas planejadas, mas que as melhorem, através de análise dos dados coletados sobre o esforço realizado no trajeto.

O outro foco dos `Tratores Grão Mestre` é evitar o trabalho desnecessário por parte de contratantes e contratados. Os veículos são capazes de ler os dados analisados sobre seus componentes internos, antecipando e resolvendo problemas relacionados a falta de combustível, falhas internas e disponibilidade de recursos (sementes, água, fertilizante, etc).

![tractor_image](/docs/images/interestelar%20tractor.webp)

## Definições Conceituais

### Requisitos Funcionais

- Haverá uma plataforma de monitoramento em tempo real dos tratores
- Deverá ser possível analisar estatísticas de consumo e danos dos tratores

### Requisitos não Funcionais

- O sistema deve ser responsivo, nada acima de 4 segundos de tempo de espera das queries é aceitável
- Para o usuário, não deverá transparecer o uso de dois banco de dados separados. A integração entre ambos não deve conter atrito

## Escopo do Projeto

- No MySQL (relacional):
  - Dados dos veículos
  - Dados dos clientes e suas fazendas
  - Dados de negócio como contratação e tempo de serviço
- No InfluxDB (não relacional):
  - Métricas de estado do veículo (sensores, cargas, GPS)
  - Métricas da via (temperatura, umidade, luminosidade)

## Requisitos Funcionais:

O sistema deverá ter os recursos necessários para responder as seguintes perguntas:

1. Qual região se há o maior uso dos tratores em 2038?
2. Quais os componentes com melhor e pior arrefecimento?
3. Qual o consumo médio de energia de cada componente?
4. Qual a duração da bateria em horas de um trator durante seu uso constante?
5. Qual o modelo de caminhão mais utilizado?
6. Qual a porcentagem de batidas (impactos) que resultam em uma ordem de manutenção?
7. Qual a média de quedas da conectividade dos tratores por mês?
8. Quais tipos de via acarretam mais manutenções?


## Requisitos Não Funcionais:

9. O tempo de resposta de qualquer consulta não deverá passar de 4 segundos para grandes volumes de dados
10. O InfluxDB deve suportar inserção de pelo menos 50.000 novos registros por segundo.
11. O InfluxDB deverá aceitar dados retroativos caso o trator fique sem sinal
12. A interação entre ambos os bancos deve ser invisível ao usuário