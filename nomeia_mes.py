import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def cria_pasta_mes(month_list):
    for month in month_list:
        output_dir = f'./output/figs/{month}'
        os.makedirs(output_dir, exist_ok=True)

def converte_num_mes(month_number):
    month_dict = {
        1: 'jan',
        2: 'fev',
        3: 'mar',
        4: 'abr',
        5: 'mai',
        6: 'jun',
        7: 'jul',
        8: 'ago',
        9: 'set',
        10: 'out',
        11: 'nov',
        12: 'dez'
    }
    month_abbreviation = month_dict.get(month_number)
    return f'{month_abbreviation}_{year}'
def plot_sinasc_data(year, month_list):
    for month_number in month_list:
        month_abbreviation = converte_num_mes(month_number)
        file_name = f'SINASC_RO_{year}_{month_number}.csv'
        sinasc = pd.read_csv(file_name)

        output_dir = f'./output/figs/{month_abbreviation}'
        os.makedirs(output_dir, exist_ok=True)

        # Converter a coluna 'DTNASC' para o formato de data
        sinasc['DTNASC'] = pd.to_datetime(sinasc['DTNASC'])

        # Agrupar os dados por mês
        sinasc_grouped = sinasc.groupby('IDADEMAE')['DTNASC'].mean().reset_index()

        # Código para gerar os gráficos para o mês atual
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='DTNASC', y='IDADEMAE', data=sinasc_grouped)
        plt.title(f'Gráfico para o mês de {month_abbreviation}')
        plt.xlabel('Idade da mãe')
        plt.ylabel('Data de nascimento')
        plt.savefig(f'{output_dir}/grafico-{month_abbreviation}.png')
        plt.close()

# Definir a lista de meses como números de 1 a 12
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Definir o ano desejado
year = 2019

# Criar as pastas para os meses
cria_pasta_mes(months)

# Gerar os gráficos para os meses
plot_sinasc_data(year, months)
