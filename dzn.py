import discord
from discord.ext import commands
import pylast
import time

config = {
    "prefixo": "-", 
    "TOKEN": "YOUR_TOKEN_HERE",
    "CHAVE_API": "YOUR_API_KEY_HERE",
    "KEY_SECRET": "YOUR_SECRET_KEY_HERE",
    "donoID": "YOUR_OWNER_ID_HERE",
    "login": "YOUR_LOGIN_HERE(USERNAME)",
    "senha": "YOUR_PASSWORD_HERE"
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config["prefixo"], intents=intents)

network = pylast.LastFMNetwork(api_key=config["CHAVE_API"], api_secret=config["KEY_SECRET"],
                               username=config["login"], password_hash=pylast.md5(config["senha"]))

@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user.name}')
    
@bot.command(name='scrobbler', help='Scrobble a música no Last.fm')
async def scrobbler(ctx, artista=None, musica=None, total_scrobbles: int=None):
    if artista is None or musica is None or total_scrobbles is None:
        await ctx.reply('Uso correto: `-scrobbler Artista Música Quantidade de Scrobbles`\n Exemplo: -scrobbler Bones SleepMode 100')
        return

    if ctx.author.id != int(config["donoID"]):
        await ctx.reply('evita dog')
        return

    if total_scrobbles < 1 or total_scrobbles > 3000:
        await ctx.reply('O número total de scrobbles deve estar entre 1 e 3000 (máximo diário).')
        return

    user = ctx.author
    perfil_lastfm = f'[{config["login"]}](https://www.last.fm/user/{config["login"]})'

    await ctx.reply(f'Iniciando o scrobble de {total_scrobbles} scrobbles de "{musica}" por "{artista}" para {user.mention}.')
    
    contador = 0

    while contador < total_scrobbles:
        try:
            network.scrobble(artist=artista, title=musica, timestamp=int(time.time()))
            contador += 1
        except pylast.WSError as e:
            await ctx.reply(f'Erro ao scrobble: {str(e)}')

    await ctx.reply(f'Scrobble concluído! Total de {total_scrobbles} scrobbles para {user.mention}. Perfil Last.fm: {perfil_lastfm}')
    
bot.run(config["TOKEN"])
