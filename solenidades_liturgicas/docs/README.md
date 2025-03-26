# Solenidades Litúrgicas Web Scraper

Este é um projeto de web scraping que coleta as solenidades litúrgicas disponíveis no site do Vatican News. O script automatiza a extração dos dados, estruturando-os em um arquivo JSON para uso posterior.

## 📌 Funcionalidades
- Coleta de solenidades litúrgicas de todos os meses do ano
- Extração de nome, data e descrição de cada solenidade
- Gera um arquivo JSON organizado com os dados coletados
- Automatiza a navegação e seleção de meses no site

## 🚀 Tecnologias Utilizadas
- **Python**
- **Selenium** (Automatiza a coleta de dados na web)
- **BeautifulSoup** (Faz a extração e parsing do HTML)
- **JSON** (Para armazenar os dados coletados)

## 📂 Estrutura do Projeto
```
📂 boot_whatsapp_qual_solenidade
│── 📂 solenidades-liturgicas
│   │── 📂 data                # Pasta para armazenar os arquivos de saída (JSON, CSV, etc.)
│   │   ├── solenidades_liturgicas.json
│   │
│   │── 📂 src                 # Pasta com o código-fonte do projeto
│   │   ├── web_scraping.py    # Script principal de web scraping
│   │
│   │── 📂 docs                # Documentação do projeto
│   │   ├── README.md          # Descrição geral do projeto
│   │   │── LICENSE            # Licença do projeto
│   │   ├── guia_instalacao.md # Instruções para rodar o projeto
│   │
│   │── 📂 requirements        # Dependências do projeto
│   │   ├── requirements.txt   # Lista de bibliotecas necessárias
│   │
│   │── .gitignore             # Arquivos que devem ser ignorados no Git
```
## 📥 Instalação e Execução
As instruções de instalação e execução do projeto estão detalhadas no arquivo [guia_instalacao.md](docs/guia_instalacao.md).

## 📜 Licença
Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE.md](docs/LICENSE.md) para mais detalhes.