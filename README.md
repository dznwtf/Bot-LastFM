# Criando um Bot no Discord e Ativando Intents

## Passo 1: Criar uma Conta no Discord

- Crie uma conta no Discord em https://discord.com/register.

## Passo 2: Criar um Servidor (opcional)

- Crie um servidor no Discord se você ainda não tiver um onde deseja adicionar o bot. Você pode criar um servidor em [este link](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-).

## Passo 3: Acesso ao Portal de Desenvolvedores

- Acesse o portal de desenvolvedores do Discord em https://discord.com/developers/applications.

## Passo 4: Criar um Aplicativo

- Clique em "New Application".
- Dê um nome ao seu aplicativo e clique em "Create".

## Passo 5: Criar um Bot

- No painel do seu aplicativo, vá para a seção "Bot" no menu lateral.
- Clique em "Add Bot" e confirme quando solicitado.

## Passo 6: Ativar Intents

- No painel do bot, vá para a seção "Bot" no menu lateral.
- Role para baixo até a seção "Privileged Gateway Intents".
- Ative os intents que seu bot precisará, como "PRESENCE INTENT" e "SERVER MEMBERS INTENT". Esses intents são necessários para que o bot acesse informações sobre membros e presença no servidor.

## Passo 7: Adicionar o Bot ao seu Servidor

- Na seção "OAuth2" do painel do bot, vá para "OAuth2 URL Generator".
- Selecione as permissões necessárias e copie a URL gerada.
- Cole a URL em um navegador e siga as instruções para adicionar o bot ao seu servidor.

# Criando um Aplicativo no Last.fm e Obtendo Chaves de API

## Passo 1: Criar uma Conta no Last.fm

- Crie uma conta no Last.fm em https://www.last.fm/join.

## Passo 2: Acessar a Página de Desenvolvedores

- Faça login na sua conta Last.fm.
- Acesse https://www.last.fm/api/account/create para criar um aplicativo na plataforma Last.fm.

## Passo 3: Preencher os Detalhes do Aplicativo

- Preencha os detalhes do seu aplicativo, incluindo nome, descrição e URL do site.
- Defina "Permissões" de acordo com as ações que deseja realizar com a API do Last.fm.

## Passo 4: Obter as Chaves de API

- Após criar o aplicativo, você verá as chaves de API: "API Key" (chave de API) e "Shared Secret" (chave secreta).
- Anote essas chaves, pois você precisará delas para autenticar seu bot ao usar a API do Last.fm.

Agora você tem um bot no Discord com intents ativadas e as chaves de API necessárias do Last.fm para autenticar seu bot e acessar os recursos da API do Last.fm. Certifique-se de proteger suas chaves de API, pois elas são sensíveis e não devem ser compartilhadas publicamente.
