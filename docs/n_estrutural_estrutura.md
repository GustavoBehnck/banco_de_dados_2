# Banco Não Relacional (InfluxDB 2)


## Como o Influx estrutura seu dados?!

Esse são exemplos de como o Influx estrutura seus dados em forma de colunas:

```rb
airSensor,sensorId=B0120,station=Place humidity=32.7908,temperature=21.667 1636729543000000000
airSensor,sensorId=A0100,station=Harbor humidity=35.0658,temperature=22.149 1534149818000000000
waterQualitySensor,sensorId=W0101,station=Harbor pH=6.1,temperature=16.103 1472515200000000000
```

Eles são separados em 4 partes:
- **`measurement`** - A "tabela" (primeiro dado da linha)
- **`tags`** - "Colunas" de características, normalmente strings (Próximos valores separados por vírgulas)
- **`fields`** - "Colunas" de dados, serão os dados medidos (Semarados por um espaço das `tags` e dividido por vírgulas entre sí)
- **`timestemp`** - Será o tempo exato que o dado foi coletado (Último valor da linha)

## Measurement (tabelas)

### `localization`

- `tags`:
  - vihicle
- `fields`:
  - latitude
  - longitude
  - altitude
