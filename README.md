# ClimaObserver

Pipeline de ingestão de dados meteorológicos estruturado como Data Lake, com foco em automação de coleta e persistência de dados da UFU.

## Arquitetura de Dados

O projeto implementa o conceito de Data Lake, separando a ingestão da transformação:
- **Camada Raw**: Armazenamento de dados em seu formato original, garantindo a imutabilidade da fonte.
- **Ingestão**: Automatizada via Python e orquestrada por GitHub Actions.

## Pipeline de CI/CD e Automação

A operação do projeto é baseada em princípios de DevOps para garantir a continuidade da coleta:

- **Orquestração**: Utilização de `.github/workflows` para agendamento (cron jobs) da execução do `coletor.py`.
- **Infraestrutura como Código**: Definição de fluxos de trabalho versionados para deploy e execução de tarefas.
- **Persistência**: Fluxo automatizado de escrita de arquivos na estrutura `data_lake/raw/weather/ufu`.

## Estrutura do Repositório

```text
ClimaObserver/
├── .github/workflows/      # Definição dos pipelines de automação
├── data_lake/
│   └── raw/                # Camada de ingestão (Landing Zone)
│       └── weather/
│           └── ufu/        # Dataset bruto da UFU
└── coletor.py              # Serviço de ingestão de dados
```

## Leia mais sobre este projeto

Eu escrevi um artigo detalhando o processo de desenvolvimento e os desafios técnicos que enfrentei ao configurar a pipeline de automação deste repositório.

Você pode conferir o artigo completo aqui: **[ClimaObserver: Uma aplicação prática dos conceitos de Data
Lake para ingestão de dados meteorológicos](https://github.com/rafaelmelom-dev/ClimaObserver/blob/main/DataLake___BD_II.pdf)**

# Tecnologias
- Linguagem: Python 3.x
- CI/CD: GitHub Actions
- Versionamento: Git
# Execução Local
1. Clone o repositório:
git clone https://github.com/rafaelmelom-dev/ClimaObserver.git
cd ClimaObserver
2. Instale as dependências:
pip install -r requirements.txt
3. Execute o serviço de coleta:
python coletor.py
