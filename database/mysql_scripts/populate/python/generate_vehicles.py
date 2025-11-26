import random
from datetime import datetime, timedelta
import string

# ----------------------------------------------------------------------------------------------------
# Variáveis configuráveis para execução
# ----------------------------------------------------------------------------------------------------
nome_banco = 'grao_mestre_db'
nome_tabela = 'vehicles'
nome_do_arquivo_final = 'populate_' + 'vehicles'
extensao_do_arquivo = '.sql'

observacoes = [
    "'Desgaste perceptível nas lâminas de corte após operação prolongada.'",
    "'Sensores laterais apresentaram leitura instável durante colheita em terreno irregular.'",
    "'Autonomia da bateria reduziu cerca de 12% após 18 meses de uso contínuo.'",
    "'Sistema de navegação precisou de recalibração após atualização de firmware.'",
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


used_client_ids = []
used_address_ids = []

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
linhas_sql = [f'USE {nome_banco};', f'INSERT INTO {nome_tabela} (status, chassis, observation, model_id, created_at, updated_at) VALUES']


print("Iniciando a geração dos registros variados...")
for i in range(1000):
    status = f"{random.choice(['in use', 'ready', 'decommissioned', 'not ready'])}"
    chassis = ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))
    observation = random.choice(observacoes)

    model_id = random.randint(1, 5)

    created_at, updated_at = random_timestamp()

    nova_linha = f"('{status}', '{chassis}', {observation}, '{model_id}', '{created_at}', '{updated_at}'),"
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
