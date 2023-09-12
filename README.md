# Configurando e Executando o Bot de Scrobble

Este guia fornece instruções detalhadas sobre como configurar e executar um bot de scrobble no Discord, que usa a API do Last.fm para registrar scrobbles de músicas.

## Configurando o Bot no Discord

### Passo 1: Crie uma Conta no Discord

- Crie uma conta no Discord em https://discord.com/register.

### Passo 2: Crie um Servidor (opcional)

- Crie um servidor no Discord onde você deseja adicionar o bot (opcional). Você pode criar um servidor em [este link](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-).

### Passo 3: Acesso ao Portal de Desenvolvedores

- Acesse o [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).

### Passo 4: Crie um Aplicativo

- Clique em "New Application".
- Dê um nome ao seu aplicativo e clique em "Create".

### Passo 5: Crie um Bot

- No painel do seu aplicativo, vá para a seção "Bot" no menu lateral.
- Clique em "Add Bot" e confirme quando solicitado.

### Passo 6: Ative Intents

- No painel do bot, vá para a seção "Bot" no menu lateral.
- Role para baixo até a seção "Privileged Gateway Intents".
- Ative os intents que seu bot precisará, como "PRESENCE INTENT" e "SERVER MEMBERS INTENT". Esses intents são necessários para que o bot acesse informações sobre membros e presença no servidor.

### Passo 7: Adicione o Bot ao seu Servidor

- Na seção "OAuth2" do painel do bot, vá para "OAuth2 URL Generator".
- Selecione as permissões necessárias e copie a URL gerada.
- Cole a URL em um navegador e siga as instruções para adicionar o bot ao seu servidor.


## Configurando o Aplicativo no Last.fm

### Passo 1: Crie uma Conta no Last.fm

- Crie uma conta no Last.fm em https://www.last.fm/join.

### Passo 2: Acesso à Página de Desenvolvedores

- Faça login na sua conta Last.fm.

- Acesse a [página de desenvolvedores do Last.fm](https://www.last.fm/api/account/create) para criar um aplicativo.

### Passo 3: Preencha os Detalhes do Aplicativo

- Preencha os detalhes do seu aplicativo, incluindo nome, descrição e URL do site.

### Passo 4: Obtenha as Chaves de API

- Após criar o aplicativo, você verá as chaves de API: "API Key" (chave de API) e "Shared Secret" (chave secreta).
- Anote essas chaves, pois você precisará delas para autenticar seu bot ao usar a API do Last.fm.

## Configurando o Bot

### Passo 1: Edite o arquivo `dzn.py`

1. Abra o arquivo `dzn.py` em um editor de texto.

2. Localize a seção chamada `config`, que se parece com isto:

```python
config = {
    "prefixo": "-", 
    "TOKEN": "YOUR_TOKEN_HERE",
    "CHAVE_API": "YOUR_API_KEY_HERE",
    "KEY_SECRET": "YOUR_SECRET_KEY_HERE",
    "donoID": "YOUR_OWNER_ID_HERE",
    "login": "YOUR_LOGIN_HERE(USERNAME)",
    "senha": "YOUR_PASSWORD_HERE"
}
```

1. Preencha as informações necessárias no lugar de "YOUR_TOKEN_HERE", "YOUR_API_KEY_HERE", "YOUR_SECRET_KEY_HERE", "YOUR_OWNER_ID_HERE", "YOUR_LOGIN_HERE(USERNAME)", e "YOUR_PASSWORD_HERE" conforme explicado no README.

2. Salve as alterações no arquivo dzn.py.


**Parte 4 - Executando o Bot**

```markdown
## Executando o Bot

### Passo 1: Execute os scripts `instalar.bat` e `start.bat`

1. Execute o arquivo `instalar.bat` para instalar as dependências necessárias. Você pode fazer isso clicando duas vezes no arquivo ou usando o prompt de comando:

```

