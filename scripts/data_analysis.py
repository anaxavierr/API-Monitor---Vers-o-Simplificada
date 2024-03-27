import pandas as pd

# Função para carregar dados do arquivo CSV
def load_data(filename):
    return pd.read_csv(filename)

# Função para analisar dados e gerar relatórios
def analyze_data(data):
    summary_stats = data.describe()
    error_rate = (data['STATUS_CODE'] != 200).mean() * 100
    print("Resumo Estatístico:")
    print(summary_stats)
    print("\nTaxa de Erro das APIs do Spotify: {:.2f}%".format(error_rate))

if __name__ == "__main__":
    spotify_api_data = load_data('spotify_api_data.csv')
    analyze_data(spotify_api_data)
