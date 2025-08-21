# Estrutura dos Bancos

## Banco Relacional (MySql)

### `clients`

| Columna      | Tipo      | NotNull? | PK? | FK? | AutIncre? | unique? |
| ------------ | --------- | -------- | --- | --- | --------- | ------- |
| id           | int       | yes      | yes | no  | yes       | yes     |
| CNPJ         | VARCHAR   | yes      | no  | no  | no        | yes     |
| trade_name   | VARCHAR   | yes      | no  | no  | no        | no      |
| company_name | VARCHAR   | yes      | no  | no  | no        | yes     |
| created_at   | TIMESTEMP | yes      | no  | no  | no        | no      |
| updated_at   | TIMESTEMP | yes      | no  | no  | no        | no      |

### `farms`

### `vehicles`

| Columna | Tipo                                     | NotNull? | PK? | FK? | AutIncre? | unique? |
| ------- | ---------------------------------------- | -------- | --- | --- | --------- | ------- |
| types   | ENUM("planting","spraying","harvesting") | yes      | no  | no  | no        | no      |

### `contracts`

### `jobs`

### `maintenances`


## Banco **Não** Relacional (InfluxDB)


