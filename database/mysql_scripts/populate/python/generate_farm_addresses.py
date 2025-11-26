import random
from datetime import datetime, timedelta

# ----------------------------------------------------------------------------------------------------
# Variáveis configuráveis para execução
# ----------------------------------------------------------------------------------------------------
nome_banco = 'grao_mestre_db'
nome_tabela = 'farm_addresses'
nome_do_arquivo_final = 'populate_farm_addresses'
extensao_do_arquivo = '.sql'

array1 = ["Rua", "Avenida", "Estrada", "Rodovia", "Alameda"]
array2 = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "João", "Karen", "Lucas", "Marina", "Nicolas", "Olivia", "Paulo", "Quésia", "Rafael", "Sara", "Tiago", "Ursula", "Valter", "Wesley", "Xavier", "Yara", "Zenaide", "Clara", "Miguel", "Sônia", "Rogério"]
array3 = ["Silva", "Souza", "Costa", "Oliveira", "Pereira", "Rodrigues", "Almeida", "Nascimento", "Lima", "Araújo","Fernandes", "Gomes", "Martins", "Barros", "Cardoso", "Reis", "Cavalcante", "Dias", "Teixeira", "Moreira","Correia", "Ramos", "Melo", "Freitas", "Borges", "Campos", "Farias", "Sales", "Monteiro", "Rocha"]

array4 = ["Parque", "Vila", "Vale", "Morro", "Encosta", "Alto", "Monte", "Serra", "Bosque","Floresta", "Planalto", "Planície", "Colinas", "Campos", "Gramado", "Veredas"]
array5 = ["Cedro", "Carvalho", "Jacarandá", "Ipê", "Sândalo", "Cristal", "Quartzo", "Granito", "Riacho", "Lago", "Fonte", "Pedra", "Amanhecer", "Horizonte", "Caminho", "Neblina", "Orvalho", "Raiz", "Folhagem", "Ventania", "Trilha", "Aroeira", "Limoeiro", "Pinheiro","Jatobá", "Bambu", "Cerrado", "Trigal", "Palmeira", "Cedrilho"]
array6 = ["Dourado", "Verde", "Claro", "Escuro", "Sereno", "Silvestre", "Antigo", "Novo", "Profundo", "Aberto", "Brilhante", "Frondoso", "Sublime", "Calmo", "Vivo", "Resistente","Forte", "Suave", "Puro", "Radiante", "Natural", "Harmonioso", "Longo", "Distante","Alto", "Baixo", "Rico", "Raro", "Sagrado", "Pleno"]

cidades_brasil = [["São Paulo", "São Paulo"], ["Rio de Janeiro", "Rio de Janeiro"], ["Belo Horizonte", "Minas Gerais"],["Brasília", "Distrito Federal"], ["Salvador", "Bahia"], ["Fortaleza", "Ceará"], ["Recife", "Pernambuco"],["Curitiba", "Paraná"], ["Porto Alegre", "Rio Grande do Sul"], ["Manaus", "Amazonas"],["Belém", "Pará"], ["Goiânia", "Goiás"], ["Campinas", "São Paulo"], ["Niterói", "Rio de Janeiro"], ["Florianópolis", "Santa Catarina"],["Santos", "São Paulo"], ["Maceió", "Alagoas"], ["Natal", "Rio Grande do Norte"], ["Vitória", "Espírito Santo"], ["João Pessoa", "Paraíba"],["Campo Grande", "Mato Grosso do Sul"], ["Cuiabá", "Mato Grosso"], ["Teresina", "Piauí"], ["Aracaju", "Sergipe"],["Uberlândia", "Minas Gerais"], ["Ribeirão Preto", "São Paulo"], ["Sorocaba", "São Paulo"], ["Londrina", "Paraná"], ["Maringá", "Paraná"], ["Caxias do Sul", "Rio Grande do Sul"],["Pelotas", "Rio Grande do Sul"], ["Joinville", "Santa Catarina"], ["Blumenau", "Santa Catarina"], ["Chapecó", "Santa Catarina"],["Foz do Iguaçu", "Paraná"], ["Macapá", "Amapá"], ["Boa Vista", "Roraima"], ["Porto Velho", "Rondônia"], ["Palmas", "Tocantins"], ["Imperatriz", "Maranhão"]]
cidades_usa = [["New York", "New York"], ["Los Angeles", "California"], ["Chicago", "Illinois"],["Houston", "Texas"], ["Phoenix", "Arizona"], ["Philadelphia", "Pennsylvania"],["San Antonio", "Texas"], ["San Diego", "California"], ["Dallas", "Texas"], ["San Jose", "California"]]

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
linhas_sql = [f'USE {nome_banco};', f'INSERT INTO {nome_tabela} (cep, street, number, complement, neighborhood, city, country_subdivision, country, created_at, updated_at) VALUES']


print("Iniciando a geração dos registros variados...")
for i in range(1000):
    cep = f"{''.join([str(random.randint(0, 9)) for _ in range(5)])}-{str(i).zfill(3)}"
    street = f"{random.choice(array1)} {random.choice(array2)} {random.choice(array3)}"
    number = "S/ Nº" if random.random() < 0.01 else str(random.randint(10, 3500))
    complement = random.choice(["'Chácara'", "'Sítio'", "'Fazenda'", "NULL"])
    neighborhood = f"{random.choice(array4)} {random.choice(array5)} {random.choice(array6)}"

    # Escolhe se será Brasil ou EUA (80% Brasil, 20% EUA)
    if random.random() < 0.8:
        city, country_subdivision = random.choice(cidades_brasil)
        country = "Brazil"
    else:
        city, country_subdivision = random.choice(cidades_usa)
        country = "USA"

    created_at, updated_at = random_timestamp()

    nova_linha = f"('{cep}', '{street}', '{number}', {complement}, '{neighborhood}', '{city}', '{country_subdivision}', '{country}', '{created_at}', '{updated_at}'),"
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
