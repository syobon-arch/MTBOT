﻿'''
ルールなど
Python上級者の方で「ここはこうしたほうがいい」というものがありましたら追記・変更ご自由にどうぞ。


'''

# 設定　よほどのことがなければ変更しないこと
import discord
import re
from discord.ext import commands
bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')
token = 'NjIwOTYxMTQ0NjU5NzcxMzky'
token += '.XXetZQ.6xDmzGmjS21b_30fQLMqRgjWJPA'
import numpy as np

# ここからコマンド

#ヘルプコマンド。コマンドを追加した場合、周りに従って追記すること。
@bot.command()
async def help(ctx, tohelp='all'): #tohelpにはヘルプを表示するコマンド名が入る
    if tohelp == 'all':
        embed = discord.Embed(title='現在利用可能なコマンドは以下のとおりです。', description='', color=0xffffff)
        embed.add_field(name='!!say', value='任意のテキストを送信します。', inline=False)
        embed.add_field(name='!!isprime', value='素数かどうか判定します。数値以外の入力には対応していません。', inline=False)
        embed.add_field(name='!!say', value='BOTに喋らせることができます', inline=False)

        #!!helpの説明は一番最後に
        embed.add_field(name='!!help', value='この一覧を表示します。', inline=False)
        await ctx.send(embed=embed)
    if tohelp == 'say':
        embed = discord.Embed(title='使用方法 ： `!!say <文字列>`', description='BOTに喋らせることができます。', color=0xffffff)
        await ctx.send(embed=embed)

    if tohelp == 'isprime':
        embed = discord.Embed(title='使用方法 ： `!!say <数値>`', description='素数かどうか判定します。数値以外の入力には対応していません。', color=0xffffff)
        await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, message='使用方法 ： `!!say 文字列`'):
    if message.startswith('delete') == True:
        await discord.ext.commands.bot.discord.message.Message.delete(ctx.message)
        message = message.split()
        message[0] = ''
        message = ' '.join(message)
        message = message.strip()

    await ctx.send(message)

@bot.command()
async def isprime(ctx, *, message='0'):
    returning = ""
    is_composite = False

    num = int(message)
    if num == 57:
        returning = "#57は素数"
    elif num < 2 or (num % 2 == 0 and num > 2) :
        returning = str(num) + "は素数ではありません"
    else:
        lim = int(np.sqrt(num)) + 1
        for i in range(3, lim, 2):
            if num % i == 0:
                is_composite = True
                break
        if is_composite:
            returning = str(num) + "は素数ではありません"
        else:
            returning = str(num) + "は素数です"
    await ctx.send(returning)


# 接続　絶対に書き換えない。
bot.run(token)
