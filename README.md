# Data Lakehouse Moderno
Este projeto simula um ambiente moderno de Data Lakehouse em uma máquina local, permitindo estudar conceitos de ingestão, transformação (dbt), orquestração (Airflow) e visualização (Metabase).

A stack é ideal para cenários de dados estáticos (sem necessidade de ingestão incremental) ou para a criação de provas de conceito (POCs) voltadas à exploração e análise de dados, antes de uma eventual migração para a nuvem.

O pipeline segue a abordagem ELT (Extract, Load, Transform): os dados são extraídos e carregados no Lake (MinIO) e no Warehouse (DuckDB). As transformações são então aplicadas diretamente no DuckDB, com o dbt atuando como camada de orquestração e governança dos modelos SQL, seguindo a arquitetura em camadas (Bronze → Silver → Gold).
# Arquitetura Local

- MinIO → Utilizado como storage simulando o papel de um Data Lake.

- DuckDB → Atua como data warehouse local e motor de processamento SQL.

- dbt → Responsável por direcionar a transformação dos dados seguindo a arquitetura medalhão em camadas (Bronze → Silver → Gold).

- Metabase → Ferramenta de self-service BI, possibilitando a exploração e visualização dos dados refinados.

- Airflow + Cosmos -> Orquestração

- Docker -> Conteinerização dos serviços 

    ![arquitetura Local](./misc/arquitetura_local.drawio.png)

## Como executar  

### Pré-requisitos  
- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/install/) 
- [Astronomer CLI](https://www.astronomer.io/docs/astro/cli/install-cli) 

### Passos  
1. Clone este repositório:

   ```
   git clone https://github.com/vinitg96/elt-data-lakehouse.git
   cd elt-data-lakehouse
   ```
2. Suba os serviços do MinIO, Metabase e Postgres:
    ```
    make infra
    ```
3. Suba o airflow:
    ```
    make airflow
    ````

4. Acesse o Airflow em http://localhost:8080
    - As DAGs **extract_load_minio** e **transformation_dbt** serão executadas automaticamente, com as dependências entre elas definidas pelo TriggerDagRunOperator.
    - Aguarde a conclusão da DAG **transformation_dbt**. Ao final da execução, será gerado o arquivo **dw.duckdb** no diretório **./services/dbt_workflow/datawarehouse/.**
    - Um detalhe interessante é que o pacote [Cosmos](https://github.com/astronomer/astronomer-cosmos) permite visualizar cada modelo SQL definido no dbt como uma task, conforme ilustrado no GIF abaixo.
     
![Airflow_UP](./misc/airflow_up_video.gif)

5. Acesse o Metabase em http://localhost:80 
    - Na etapa 4 da criação do usuário ("Adicione seus Dados"), busque por DuckDB e no campo **"Database File"** informe o caminho **/app/datawarehouse/dw.duckdb**
    - Após a conexão ser estabelecida com sucesso, será possível interagir com as tabelas pelo Metabase, conforme demonstrado no GIF abaixo. 

   
![Metabase UP](./misc/metabase_up_video.gif)

6. O MiniIO console pode ser acessado em http://localhost:9001
    - usuario: minio123
    - senha: minio123


# Observações
- O MinIO e o banco de aplicação do Metabase (postgres) fazem usos de volumes nomeados. Dessa forma os dados, configurações, queries, dashboards, etc irão persistir mesmo com os containers sendo removidos ou desligados.
- O duckdb não permite acessos simultaneos, logo, caso queira executar a DAG **transformation_dbt**  após a configuração do metabase, é necessário desligar o container metaduck)

# Próximos Passos
- Implementar testes e documentação dos modelos SQL com o dbt
- Melhorar logs
- Migrar arquitetura para nuvem usando os seguintes serviços:
    - S3 como storage (lake)
    - Motherduck: substitui o duckDB como warehouse eliminando o problema da concorrencia
    - EC2 para subir o metabase
    - RDS como banco de aplicação do metabse, garantindo a persistencia
