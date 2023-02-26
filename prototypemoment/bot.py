import hikari
import tanjun
import os


def build_bot() -> hikari.GatewayBot:
    token = os.environ.get('DISCORD_TOKEN')
    bot = hikari.GatewayBot(token)

    make_client(bot)

    return bot


def make_client(bot: hikari.GatewayBot) -> tanjun.Client:
    client = tanjun.Client.from_gateway_bot(
        bot,
        declare_global_commands=True
    )

    client.load_modules('prototypemoment.plugins.bruh')

    return client
