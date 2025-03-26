# Guia de Instalação

## Requisitos
Antes de iniciar, verifique se você possui os seguintes requisitos instalados:
- Python 3.8 ou superior
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome

## Instalação
1. Clone este repositório:
   ```sh
   git clone [https://github.com/seu-usuario/solenidades-liturgicas.git](https://github.com/Leandro-Rocha81/boot_whatsApp_qual_solenidade.git)
   ```
   
2. Acesse a pasta do projeto:
   ```sh
   cd solenidades-liturgicas
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

4. Instale as dependências:
   ```sh
   pip install -r requirements/requirements.txt
   ```

5. Configure o caminho do ChromeDriver no script `src/web_scraping.py`:
   ```python
   driver_path = "C:/chromedriver/chromedriver.exe"  # Altere conforme o local do seu ChromeDriver
   ```

## Execução do Script
Execute o script de coleta de dados:
```sh
python src/web_scraping.py
```
Os dados coletados serão salvos em `data/solenidades_liturgicas.json`.
