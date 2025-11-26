import random
from datetime import datetime, timedelta
import string

# ----------------------------------------------------------------------------------------------------
# Variáveis configuráveis para execução
# ----------------------------------------------------------------------------------------------------
nome_banco = 'grao_mestre_db'
nome_tabela = 'contracts'
nome_do_arquivo_final = 'populate_' + 'contracts'
extensao_do_arquivo = '.sql'

used_client_ids = []

def random_timestamp(start_year=2022, end_year=2025, delta_days_max=365):
    start = datetime(start_year, 1, 1, 0, 0, 0)
    end = datetime(end_year, 12, 31, 23, 59, 59)
    delta_total_seconds = int((end - start).total_seconds())
    
    created_dt = start + timedelta(seconds=random.randint(0, delta_total_seconds))
    updated_dt = created_dt + timedelta(seconds=random.randint(0, int(timedelta(days=delta_days_max).total_seconds())))
    
    return created_dt.strftime('%Y-%m-%d %H:%M:%S'), updated_dt.strftime('%Y-%m-%d %H:%M:%S')

def random_timestamp_to_contract(start_year=2022, end_year=2025, delta_days_min=30, delta_days_max=365):
    start = datetime(start_year, 1, 1, 0, 0, 0)
    end = datetime(end_year, 12, 31, 23, 59, 59)
    delta_total_seconds = int((end - start).total_seconds())
    
    created_dt = start + timedelta(seconds=random.randint(0, delta_total_seconds))
    updated_dt = created_dt + timedelta(seconds=random.randint(int(timedelta(days=delta_days_min).total_seconds()), int(timedelta(days=delta_days_max).total_seconds())))
    
    return created_dt.strftime('%Y-%m-%d %H:%M:%S'), updated_dt.strftime('%Y-%m-%d %H:%M:%S')


# ----------------------------------------------------------------------------------------------------
# Define um array de linhas para o script de inserção dos registros e insere as duas primeiras linhas
# ----------------------------------------------------------------------------------------------------
linhas_sql = [f'USE {nome_banco};', f'INSERT INTO {nome_tabela} (lease_deed, client_id, status, start_date, end_date, created_at, updated_at) VALUES']


print("Iniciando a geração dos registros variados...")
for i in range(1000):
    # CLIENT ID
    while True:
        client_id = random.randint(1, 1008)
        if client_id not in used_client_ids:
            used_client_ids.append(client_id)
            break

    lease_deed = lease_deed = f"s3://graomestre-prod-assets/contracts/leases/{client_id}.pdf"

    status = random.choice(["TRUE", "FALSE"])

    start_date, end_date = random_timestamp_to_contract()
    created_at, updated_at = random_timestamp()

    nova_linha = f"('{lease_deed}', '{client_id}', {status}, '{start_date}', '{end_date}', '{created_at}', '{updated_at}'),"
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
