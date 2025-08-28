# Estrutura dos Bancos

## Banco Relacional (MySql)

### `clients`

| Columna      | Tipo                                  | NotNull? | PK? | FK? | AutIncre? | unique? |
| ------------ | ------------------------------------- | -------- | --- | --- | --------- | ------- |
| id           | int                                   | yes      | yes | no  | yes       | yes     |
| cnpj         | VARCHAR                               | yes      | no  | no  | no        | yes     |
| status       | ENUM("active","inactive","suspended") | yes      | no  | no  | no        | no      |
| trade_name   | VARCHAR                               | yes      | no  | no  | no        | no      |
| company_name | VARCHAR                               | yes      | no  | no  | no        | yes     |
| created_at   | TIMESTEMP                             | yes      | no  | no  | no        | no      |
| updated_at   | TIMESTEMP                             | yes      | no  | no  | no        | no      |

### `farms`

| Columna    | Tipo                                  | NotNull? | PK? | FK?               | AutIncre? | unique? |
| ---------- | ------------------------------------- | -------- | --- | ----------------- | --------- | ------- |
| id         | int                                   | yes      | yes | no                | yes       | yes     |
| name       | VARCHAR                               | yes      | no  | no                | no        | no      |
| client_id  | int                                   | yes      | no  | yes -> clients.id | no        | no      |
| cep        | VARCHAR                               | yes      | no  | no                | no        | no      |
| address    | VARCHAR                               | no       | no  | no                | no        | no      |
| area       | float                                 | yes      | no  | no                | no        | no      |
| status     | ENUM("active","inactive","suspended") | yes      | no  | no                | no        | no      |
| created_at | TIMESTEMP                             | yes      | no  | no                | no        | no      |
| updated_at | TIMESTEMP                             | yes      | no  | no                | no        | no      |

### `vehicles`

| Columna     | Tipo                                                | NotNull? | PK? | FK?             | AutIncre? | unique? |
| ----------- | --------------------------------------------------- | -------- | --- | --------------- | --------- | ------- |
| id          | int                                                 | yes      | yes | no              | yes       | yes     |
| status      | ENUM("in use","ready","decommissioned","not ready") | yes      | no  | no              | no        | no      |
| chassis     | VARCHAR                                             | yes      | no  | no              | no        | no      |
| observation | VARCHAR                                             | no       | no  | no              | no        | no      |
| model       | int                                                 | yes      | no  | yes -> model.id | no        | no      |
| created_at  | TIMESTEMP                                           | yes      | no  | no              | no        | no      |
| updated_at  | TIMESTEMP                                           | yes      | no  | no              | no        | no      |

### `contracts`

| Columna    | Tipo      | NotNull? | PK? | FK?               | AutIncre? | unique? |
| ---------- | --------- | -------- | --- | ----------------- | --------- | ------- |
| id         | int       | yes      | yes | no                | yes       | yes     |
| client_id  | int       | yes      | no  | yes -> clients.id | no        | no      |
| status     | boolean   | yes      | no  | no                | no        | no      |
| start_date | TIMESTEMP | yes      | no  | no                | no        | no      |
| end_date   | TIMESTEMP | yes      | no  | no                | no        | no      |
| created_at | TIMESTEMP | yes      | no  | no                | no        | no      |
| updated_at | TIMESTEMP | yes      | no  | no                | no        | no      |

### `services`

### `jobs`

### `maintenances`

| Columna        | Tipo      | NotNull? | PK? | FK? | AutIncre? | unique? |
| -------------- | --------- | -------- | --- | --- | --------- | ------- |
| id             | int       | yes      | yes | no  | yes       | yes     |
| date           | TIMESTEMP | yes      | no  | no  | no        | no      |
| reason         | VARCHAR   | yes      | no  | no  | no        | no      |
| link_to_ticket | VARCHAR   | yes      | no  | no  | no        | no      |
| created_at     | TIMESTEMP | yes      | no  | no  | no        | no      |
| updated_at     | TIMESTEMP | yes      | no  | no  | no        | no      |

### `model`

| Columna          | Tipo                                     | NotNull? | PK? | FK? | AutIncre? | unique? |
| ---------------- | ---------------------------------------- | -------- | --- | --- | --------- | ------- |
| id               | int                                      | yes      | yes | no  | yes       | yes     |
| types            | ENUM("planting","spraying","harvesting") | yes      | no  | no  | no        | no      |
| batery_capacity  | float                                    | yes      | no  | no  | no        | no      |
| fabrication_year | int                                      | yes      | no  | no  | no        | no      |
| batery_capacity  | float                                    | yes      | no  | no  | no        | no      |
| charging_time    | float                                    | yes      | no  | no  | no        | no      |
| created_at       | TIMESTEMP                                | yes      | no  | no  | no        | no      |
| updated_at       | TIMESTEMP                                | yes      | no  | no  | no        | no      |

## Banco **Não** Relacional (InfluxDB)


