import tanjun
import requests

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command('bruh', 'register bruh moment')
async def bruh(ctx: tanjun.abc.Context) -> None:
    # request
    r = requests.get('https://fl4il.eu/bruh_counter/add/bruh')

    if r.status_code == 200:
        await ctx.respond(f'bruh moment (total={r.text})')
    else:
        await ctx.respond('the api is having a bruh moment')


@component.with_slash_command
@tanjun.as_slash_command('prototype', 'register prototype moment')
async def prototype(ctx: tanjun.abc.Context) -> None:
    # request
    r = requests.get('https://fl4il.eu/bruh_counter/add/lmp')

    if r.status_code == 200:
        await ctx.respond(f'prototype moment (total={r.text})')
    else:
        await ctx.respond('the api is having a bruh moment')


@component.with_slash_command
@tanjun.as_slash_command('oohshit', 'register ooh shit moment')
async def oohshit(ctx: tanjun.abc.Context) -> None:
    # request
    r = requests.get('https://fl4il.eu/bruh_counter/add/ooh_shit')

    if r.status_code == 200:
        await ctx.respond(f'ooh shit moment (total={r.text})')
    else:
        await ctx.respond('the api is having a bruh moment')


@component.with_slash_command
@tanjun.as_slash_command('yeet', 'register yeet moment')
async def yeet(ctx: tanjun.abc.Context) -> None:
    # request
    r = requests.get('https://fl4il.eu/bruh_counter/add/yeet')

    if r.status_code == 200:
        await ctx.respond(f'yeet moment (total={r.text})')
    else:
        await ctx.respond('the api is having a bruh moment')


@component.with_slash_command
@tanjun.as_slash_command('reset', 'reset all counters')
async def reset(ctx: tanjun.abc.Context) -> None:
    # request
    r = requests.get('https://fl4il.eu/bruh_counter/admin/reset')

    if r.status_code == 200:
        await ctx.respond('counters reset')
    else:
        await ctx.respond('the api is having a bruh moment')


@tanjun.as_loader
def load(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())