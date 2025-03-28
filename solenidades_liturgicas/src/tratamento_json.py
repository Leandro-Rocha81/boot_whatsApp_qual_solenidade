import json
import os

# Caminho do arquivo JSON
file_path = os.path.join(os.path.dirname(__file__), 'solenidades_liturgicas/data/solenidades_liturgicas.json')

# Mapeamento dos meses para números
meses = {
    "Janeiro": "01",
    "Fevereiro": "02",
    "Março": "03",
    "Abril": "04",
    "Maio": "05",
    "Junho": "06",
    "Julho": "07",
    "Agosto": "08",
    "Setembro": "09",
    "Outubro": "10",
    "Novembro": "11",
    "Dezembro": "12"
}

# Função para formatar a data no formato desejado (DD-MM)
def formatar_data(data):
    dia, mes = data.split(" ")
    mes_formatado = meses.get(mes, "00")
    return f"{mes_formatado}-{dia.zfill(2)}"

# Função para converter as datas no arquivo JSON
def converter_datas():
    try:
        # Carregar o arquivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            solenidades = json.load(file)

        # Converter as datas para o formato desejado
        for solenidade in solenidades:
            solenidade["Data"] = formatar_data(solenidade["Data"])

        # Salvar o arquivo com as datas convertidas
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(solenidades, file, ensure_ascii=False, indent=4)

        print("✅ Datas convertidas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao converter datas: {e}")

# Executando a função
converter_datas()