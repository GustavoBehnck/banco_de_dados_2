# Projeto de Banco de Dados 2

O projeto é divido em algumas partes, a baixo há a explicação dele por completo

- [Projeto de Banco de Dados 2](#projeto-de-banco-de-dados-2)
  - [Tema: `Telemetria de Veículos Autônomos`](#tema-telemetria-de-veículos-autônomos)
  - [Sinopse](#sinopse)
  - [Integrantes](#integrantes)
  - [Estrutura do projeto](#estrutura-do-projeto)
    - [Modelagem do Banco não relacional](#modelagem-do-banco-não-relacional)
    - [Modelagem do Banco relacional](#modelagem-do-banco-relacional)
    - [SQL de criação do banco](#sql-de-criação-do-banco)
    - [Script de inserção de dados no InfluxDB](#script-de-inserção-de-dados-no-influxdb)
    - [Grafana - Visualização do InfluxDB](#grafana---visualização-do-influxdb)


## Tema: `Telemetria de Veículos Autônomos`

Em específico, sobre tratores agrículos

## Sinopse

A companhia `Grão Mestre` se especializou em veículos autônomos em 2032, migrando para o ramo de tratores agrícolas em 2035, quando adotou o nome atual. O serviço oferecido pela empresa consiste em disponibilizar veículos de grande porte para trabalho agrícola em fazendas para pessoas jurídicas.

Mais do que fornecer o hardware das máquinas, oferecemos o sistema que as gerencia, para que realizem da maneira mais inteligente os trabalhos agendados. Além disso, as máquinas são preparadas para permitir que não apenas executem o trabalho nas rotas planejadas, mas que as melhorem, através de análise dos dados coletados sobre o esforço realizado no trajeto.

O outro foco dos `Tratores Grão Mestre` é evitar o trabalho desnecessário por parte de contratantes e contratados. Os veículos são capazes de ler os dados analisados sobre seus componentes internos, antecipando e resolvendo problemas relacionados a falta de combustível, falhas internas e disponibilidade de recursos (sementes, água, fertilizante, etc).

![tractor_image](/database/docs/images/interestelar%20tractor.png)

## Integrantes

- Gustavo Behnck Cardoso
  - RA: `02310735`
- Mateus Takamatsu
  - RA: `02310341`
- Flávio Monteiro
  - RA: `02310091`
- João Victor Britto Vichoski Ben Carloto
  - RA: `02310275`

## Estrutura do projeto

O repositório do Github é divido em duas principais partes:
- [/database](https://github.com/GustavoBehnck/banco_de_dados_2/tree/main/database) - onde guardamos qualquer arquivo referente à documentação do projeto, scripts e modelagem.
- qualquer outro arquivo ou pasta desse reposório é referente ao site feito em Django que atualmente está sendo 'hosteado' em nossa VPS (Virtual Private Server) na URL [extensao.sjc.br:8001](http://extensao.sjc.br:8001/)

Agora vamos passar mais a fundo em cada parte do projeto e seus principais arquivos.

### Modelagem do Banco não relacional

Localizado em [database/docs/influxdb_estrutura.md](https://github.com/GustavoBehnck/banco_de_dados_2/blob/main/database/docs/influxdb_estrutura.md)

Nesse arquivo é onde organizamos como seria a estrutura do influxdb, além de uma pequena documentação de como o influx estrutura seus próprios registros.

### Modelagem do Banco relacional

Localizado em [database/docs/mysql_estrutura.md](https://github.com/GustavoBehnck/banco_de_dados_2/blob/main/database/docs/mysql_estrutura.md)

Nesse arquivo é onde organizamos como seria a estrutura do banco de dados relacional, nesse caso estamos usando o mysql. Nele está contido não apenas a modelagem em forma de tabela com dados mais a fundo, mas também em forma de gráfico em mermaid com seus relacionamentos.

### SQL de criação do banco

Localizado em [database/scripts/create_tables.sql](https://github.com/GustavoBehnck/banco_de_dados_2/blob/main/database/scripts/create_tables.sql)

Código em sql da criação do nosso banco

### Script de inserção de dados no InfluxDB

Primeiramente foi criado um script de insersão de dados no InfluxDB de forma serial.

Localizado em [database/scripts/influxdb.py](https://github.com/GustavoBehnck/banco_de_dados_2/blob/main/database/scripts/influxdb.py)

Porém, para a quantidade de dados que desejávamos inserir, fazer a inserção de forma serial é inviável. Por conta disso criamos um script de inserção de dados de forma paralela, isso é possível por que cada inserção de um trator é idependente entre si, sendo possível criar um thread para cara `truck_id`

Localizado em [database/scripts/influxdb_paralle.py](https://github.com/GustavoBehnck/banco_de_dados_2/blob/main/database/scripts/influxdb_paralle.py)

Com esse novo script, foi possível fazer a seguinte inserção no banco:

```rb
Launching 20 parallel processes...
Truck 6 finished! Generated 3448815 points.
Truck 12 finished! Generated 3447660 points.
Truck 8 finished! Generated 3441915 points.
Truck 3 finished! Generated 3445290 points.
Truck 11 finished! Generated 3447900 points.
Truck 10 finished! Generated 3451665 points.
Truck 9 finished! Generated 3450045 points.
Truck 5 finished! Generated 3446070 points.
Truck 4 finished! Generated 3452130 points.
Truck 7 finished! Generated 3446385 points.
Truck 1 finished! Generated 3447225 points.
Truck 2 finished! Generated 3444165 points.
Truck 18 finished! Generated 3455880 points.
Truck 16 finished! Generated 3441720 points.
Truck 20 finished! Generated 3446520 points.
Truck 19 finished! Generated 3449865 points.
Truck 15 finished! Generated 3452760 points.
Truck 14 finished! Generated 3448170 points.
Truck 17 finished! Generated 3453195 points.

Simulation Complete in 1001.10 seconds.
Total Points Across Fleet: 65517375
```

(Arquivo de log completo em [database/scripts/insert_20_trucks_production.log](https://github.com/GustavoBehnck/banco_de_dados_2/blob/main/database/scripts/insert_20_trucks_production.log))

Totalizando mais de 65.5 **Milhões** de dados inseridos no banco em 16.685 minutos, isso é aproximadamente `65445.4` inserções por segundo

### Grafana - Visualização do InfluxDB

Para a visualizações desses 65.5 milhões de dados, foi utilizado o Grafana, um software open-source para criação de dashboards, muito utilizado para facilitar a visualizações de grandes volumes de dados.

O Grafana de produção pode ser acesso por qualquer um na URL [httpextensao.sjc.br:3000](http://extensao.sjc.br:3000/d/fffce2ab-b3e6-48ed-a4d6-0013458e97cc/grao-mestre-dashboard?orgId=1&from=1763434800000&to=1763866799000&var-measurement=battery&var-field=current&var-truck=1&var-truck=12&showCategory=Panel+options&theme=light)

Ou pelo site em Django: [extensao.sjc.br:8001/colaborador/dashboard](http://extensao.sjc.br:8001/colaborador/dashboard)