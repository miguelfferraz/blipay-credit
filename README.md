# blipay-credit

# Descrição
API HTTP para análise de crédito.

## Requisitos
Para rodar o aplicativo é necessário o Python versão 3.10 ou superior.

- [Python >= 3.10](https://www.python.org/downloads/)
- [venv](https://docs.python.org/3/library/venv.html) (recomendado)

Opcionalmente é possível executar utilizando o Docker:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/) (recomendado)

## Como executar

### Instalação local

1 - Clonar o repositório:

```bash
git clone https://github.com/miguelfferraz/blipay-credit.git
cd blipay-credit
```

2 - Criar um ambiente virtual *(opcional)*:

```bash
python3 -m venv venv
source venv/bin/activate
```

3 - O projeto pode ser executado utilizando o `hatch` para rodar os scripts definidos no `pyproject.toml`:

```bash
pip install hatch
hatch run start
```

4 - Também é possível executar sem utilizar o `hatch`:

```bash
pip install -r requirements.txt
python3 -m src.main.py
```
5 - Com isso o servidor deve estar rodando na porta 8080 *(padrão)*, é possível especificar outra porta como argumento:
```bash
python3 -m src.main --port 1234
```
```bash
hatch run start --port 1234
```

### Utilizando Docker

É possível executar a aplicação utilizando um container Docker, para isso é necessário construir a imagem e executar:

```bash
docker build -t blipay-credit .
docker run -p 8080:8080 blipay-credit
```

Também é possível executar utilizando o `docker-compose.yml`:
```bash
docker compose up server
```

## Variáveis de Ambiente

A aplicação usa variáveis de ambiente para configurar o acesso à API OpenWeatherMap. Essa variáveis podem ser definidas criando um arquivo `.env` antes de executar a aplicação.

Um exemplo de um arquivo `.env`:

```bash
OPEN_WEATHER_BASE_URL=http://api.openweathermap.org/data/2.5
OPEN_WEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0 # Para acessar a API é necessário criar uma conta e gerar uma chave de acesso.
```

Executando pelo Docker é possível passar as variáveis de ambiente pela linha de comando, sem criar o arquivo `.env`:

```bash
docker run -e OPEN_WEATHER_BASE_URL=http://api.openweathermap.org/data/2.5 -e OPEN_WEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0 blipay-credit
```

Também é possível modificar o `docker-compose.yml` para incluir as variáveis de ambiente.

## Como rodar os testes

Para rodar os testes unitários é possível utilizar o `hatch`, ele irá instalar as depêndencias necessárias:

```bash
pip install hatch
hatch run test:test
```

Para obter a cobertura de código: 

```bash
hatch run test:cov
```

Caso deseje executar sem o `hatch`, será necessário instalar as depêndencias:

```bash
pip install -r requirements-test.txt
python3 -m pytest .
```

Também é possível utilizar o `docker-compose.yml` para executar os testes:

```bash
docker compose up tests
```

## Contato

Para suporte você pode entrar em contato pelo email <miguelfigueiraferraz@gmail.com>.

