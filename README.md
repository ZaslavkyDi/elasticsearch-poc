# ElasticSearch-POC

Proof of concept of using ElasticSearch

## Project Requirements

- Python 3.12
- pydantic-settings
- elasticsearch 8.11

## Project Setup

1. Create and activate **venv**

> - python -m venv /path/to/new/virtual/environment
> - source venv/bin/activate

2. Upgrade pip to the latest version

> pip install --upgrade pip

3. Install and init **poetry**

> - pip install poetry
> - poetry install

4. Create **.env** file from ****[example.local.env](example.local.env)**** and place it on the same level. Populate *
   *OPENAI_API_KEY** variable.