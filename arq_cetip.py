#-----------------------------------------------------------------------------------
# PROJETO: OTIMIZAR A EXTRAÇÃO DOS ARQUIVOS REF. A CUSTÓDIA DOS ATIVOS 
# Data Criação: 2023-09-15
# Autor: Dieggo Henrique
#-----------------------------------------------------------------------------------

# ETAPA 00 -------------------------------------------------------------------------
# Leitura das bibliotecas
from pathlib import Path  # --> Navegar dentro das pastas
import zipfile            # --> Manipulação de arquivos .zip
import os                 # --> Navegação entre as pastar no computador


# ETAPA 01 -------------------------------------------------------------------------
# Lista com todos os nomes dos arquivos que serão extraídos do arquivo ZIP
diretorio = Path(".")
arquivos_zip = diretorio.glob("**/*.zip")
# Diretório relativo onde estão os arquivos sem extensão
diretorio_destino = Path(r'01_CETIP\Base_CETIP')


 # Extraindo todos os arquivos no diretório para o diretório destino
for arquivo in arquivos_zip:
    zip = zipfile.ZipFile(f"{arquivo}", "r")
    zip.extractall(diretorio_destino)
    zip.close()


# ETAPA 02 -------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
# Lembre-se de que este código renomeará os arquivos no diretório especificado. 
# Certifique-se de ter um backup ou de estar seguro de que deseja realizar essa 
# ação antes de executar o código.
#-----------------------------------------------------------------------------------

# Extensão que você deseja adicionar
extensao = ".txt"  # Substitua ".txt" pela extensão desejada

# Liste os arquivos no diretório
arquivos_no_diretorio = os.listdir(diretorio_destino)

# Itere sobre os arquivos e renomeie-os com a extensão desejada
for nome_do_arquivo_sem_extensao in arquivos_no_diretorio:
    # Certifique-se de que o arquivo não possui uma extensão
    if not nome_do_arquivo_sem_extensao.endswith(extensao):
        # Renomeia o arquivo incluindo a extenção
        novo_nome_do_arquivo = nome_do_arquivo_sem_extensao + extensao
        # antigo caminho --> renomeando o arquivo no diretorio e 
        # novo caminho --> arquivos já renomeado no temporário
        antigo_caminho = os.path.join(diretorio_destino, nome_do_arquivo_sem_extensao)
        novo_caminho = os.path.join(diretorio_destino, novo_nome_do_arquivo)
        # Executando a substituição
        os.rename(antigo_caminho, novo_caminho)

print("Arquivos extraídos e extensão adicionada aos arquivos com sucesso!")

# ********************************** FIM *******************************************