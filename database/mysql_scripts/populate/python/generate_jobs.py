import random
from datetime import datetime, timedelta

# ----------------------------------------------------------------------------------------------------
# Variáveis configuráveis para execução
# ----------------------------------------------------------------------------------------------------
nome_banco = 'grao_mestre_db'
nome_tabela = 'jobs_log'
nome_do_arquivo_final = 'populate_' + 'jobs'
extensao_do_arquivo = '.sql'

observacoes = [
    "'Módulo de navegação autônoma registrou pequenas divergências de rota em áreas com sinal GPS instável.'",
    "'Relatórios de telemetria indicam necessidade de recalibração dos sensores de proximidade após 300 horas de operação.'",
    "'Atualização remota do software de controle melhorou a eficiência do trajeto, mas exigiu reinicialização inesperada durante um ciclo de trabalho.'",
    "'Sistema de detecção de obstáculos apresentou atraso de resposta ao operar próximo a vegetação densa.'",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL",
    "NULL"
]

used_vehicle_ids = []

def random_timestamp(start_year=2022, end_year=2025, delta_days_max=365):
    start = datetime(start_year, 1, 1, 0, 0, 0)
    end = datetime(end_year, 12, 31, 23, 59, 59)
    delta_total_seconds = int((end - start).total_seconds())
    
    created_dt = start + timedelta(seconds=random.randint(0, delta_total_seconds))
    updated_dt = created_dt + timedelta(seconds=random.randint(0, int(timedelta(days=delta_days_max).total_seconds())))
    
    return created_dt.strftime('%Y-%m-%d %H:%M:%S'), updated_dt.strftime('%Y-%m-%d %H:%M:%S')


# ----------------------------------------------------------------------------------------------------
# Define um array de linhas para o script de inserção dos registros e insere as duas primeiras linhas
# ----------------------------------------------------------------------------------------------------
linhas_sql = [f'USE {nome_banco};', f'INSERT INTO {nome_tabela} (vehicle_id, observation, started_date, finished_date, created_at, updated_at) VALUES']


print("Iniciando a geração dos registros variados...")
for i in range(1000):
    # VEHICLE ID
    while True:
        vehicle_id = random.randint(1, 1000)
        if vehicle_id not in used_vehicle_ids:
            used_vehicle_ids.append(vehicle_id)
            break

    observation = random.choice(observacoes)

    started_date, finished_date = random_timestamp()

    created_at, updated_at = random_timestamp()

    nova_linha = f"('{vehicle_id}', {observation}, '{started_date}', '{finished_date}', '{created_at}', '{updated_at}'),"
    linhas_sql.append(nova_linha)
print("Registros gerados!")



# ----------------------------------------------------------------------------------------------------
# Transforma o array em um aqruivo de script SQL
# ----------------------------------------------------------------------------------------------------

# Substitui a vírgula no final do último registro por ponto e vírgula para encessar o SQL
linhas_sql[-1] = linhas_sql[-1].rstrip(',') + ';'

# Junta todas as linhas (mantendo a quebra de linhas entre elas) em um único texto
script_sql = "\n".join(linhas_sql)

# Cria um arquivo com o script de sql pronto para usar
with open(f"{nome_do_arquivo_final}{extensao_do_arquivo}", "w") as f:
    f.write(script_sql)

print(f"Arquivo {nome_do_arquivo_final}{extensao_do_arquivo} criado com os INSERTs")
