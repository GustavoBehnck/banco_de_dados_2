import random
from datetime import datetime, timedelta

# ----------------------------------------------------------------------------------------------------
# Variáveis configuráveis para execução
# ----------------------------------------------------------------------------------------------------
nome_banco = 'grao_mestre_db'
nome_tabela = 'farms'
nome_do_arquivo_final = 'populate_farms'
extensao_do_arquivo = '.sql'

arraynomes = ["Fazenda", "Sítio", "Chácara", "Estância", "Haras"]
arraysobrenomes1 = ["Do Milho", "Da Soja", "Do Trigo", "Do Café", "Do Gado", "Do Leite", "Da Pecuária", "Dos Cavalos", "Do Pasto", "Do Curral", "Do Algodão", "Da Cana", "Do Arroz", "Da Lavoura", "Do Cerrado", "Da Terra Vermelha", "Do Capim", "Do Eucalipto", "Do Pomar", "Do Laticínio", "Da Semente", "Do Transporte", "Da Ração", "Do Celeiro", "Da Colheita", "Do Trator", "Do Arado", "Da Plantação", "Do Campo", "Do Estábulo", "Da Pecuária Leiteira", "Dos Suínos", "Das Ovelhas", "Da Horta", "Do Viveiro", "Do Lago", "Da Granja", "Do Engenho", "Do Silo", "Do Galpão"]
arraysobrenomes2 = ["Alta", "Verde", "Nova", "Antiga", "Bonita", "Produtiva", "Grande", "Pequena", "Do Vale", "Da Serra", "Do Sol", "Da Lua", "Da Mata", "Da Colina", "Do Horizonte", "Do Rio", "Da Lagoa", "Da Montanha", "Do Morro", "Do Planalto", "Do Luar", "Da Neblina", "Do Vento", "Da Chuva", "Da Esperança", "Da União", "Da Vitória", "Da Harmonia", "Da Paz", "Do Amanhecer", "Do Entardecer", "Do Cerrado", "Da Aurora", "Da Várzea", "Da Pradaria", "Do Vale Dourado", "Da Folha Verde", "Do Caminho", "Do Entorno"]


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
linhas_sql = [f'USE {nome_banco};', f'INSERT INTO {nome_tabela} (name, client_id, address_id, area, status, created_at, updated_at) VALUES']


print("Iniciando a geração dos registros variados...")
for i in range(1000):
    name = f"{random.choice(arraynomes)} {random.choice(arraysobrenomes1)} {random.choice(arraysobrenomes2)}"

    # CLIENT ID
    while True:
        client_id = random.randint(1, 1008)
        if client_id not in used_client_ids:
            used_client_ids.append(client_id)
            break

    # ADDRESS ID
    while True:
        address_id = random.randint(1, 1000)
        if address_id not in used_address_ids:
            used_address_ids.append(address_id)
            break

    area = round(random.uniform(0.5, 5000), 2)
    status = f"{random.choice(['active', 'inactive', 'suspended'])}"

    created_at, updated_at = random_timestamp()

    nova_linha = f"('{name}', '{client_id}', '{address_id}', {area}, '{status}', '{created_at}', '{updated_at}'),"
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
