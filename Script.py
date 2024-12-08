import csv
import re
from bs4 import BeautifulSoup

# Caminho do arquivo HTML
file_path = 'principal.html'

# Carregar o arquivo HTML
with open(file_path, 'r', encoding='windows-1252') as file:
    html_content = file.read()

# Analisar o HTML usando BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Localizar a tag <pre> contendo os dados
pre_tag = soup.find('pre')

# Extrair as linhas de texto da tag <pre>
if pre_tag:
    lines = pre_tag.get_text().splitlines()
else:
    lines = []

# Expressão regular para dividir cada linha em colunas
pattern = r'\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|'

# Processar cada linha e extrair as colunas
data = []
for line in lines:
    match = re.match(pattern, line)
    if match:
        # Adicionar os valores das colunas como uma lista
        data.append([col.strip() for col in match.groups()])

# Caminho para salvar o arquivo CSV
output_path = '/Data/dados_extraidos.csv'

# Salvar os dados no formato CSV
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Escrever cabeçalho
    csv_writer.writerow(['final_CPF', 'nome', 'nota_Mat', 'nota_Fis', 'nota_Qui', 'nota_Ing', 'media', 'presenca'])
    # Escrever os dados
    csv_writer.writerows(data)

print(f'Dados extraídos e salvos em: {output_path}')
