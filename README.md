# ClimaObserver

Projeto para a coleta e monitoramento de dados meteorológicos, estruturado para organizar informações em camadas de Data Lake, com foco em dados da UFU.

## Funcionalidades

- Coleta de dados climáticos através do script `coletor.py`.
- Armazenamento de dados brutos (raw) em estrutura de Data Lake.
- Monitoramento de dados meteorológicos da UFU.

## Estrutura do Projeto

```text
ClimaObserver/
├── .github/workflows/      # Fluxos de automação
├── data_lake/
│   └── raw/
│       └── weather/
│           └── ufu/        # Dados brutos da UFU
└── coletor.py              # Script de coleta
Tecnologias
- Python 3.x
- GitHub Actions
Instalação e Execução
1. Clone o repositório:
git clone https://github.com/rafaelmelom-dev/ClimaObserver.git
cd ClimaObserver
2. Instale as dependências:
pip install -r requirements.txt
3. Execute o script de coleta:
python coletor.py
