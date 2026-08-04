import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🔥 Bot berhasil online sebagai: {bot.user}")

# Command untuk mencatat transaksi
@bot.command(name="catat")
async def catat_transaksi(ctx, nama: str, produk: str, modal: int, jual: int):
    payload = {
        "customer_name": nama,
        "product_description": produk,
        "capital_price": modal,
        "selling_price": jual,
        "status": "SUCCESS"
    }

    try:
        # Menembak data ke API FastAPI secara Asynchronous
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, json=payload) as response:
                
                if response.status == 200:
                    data = await response.json()
                    profit = data['selling_price'] - data['capital_price']
                    await ctx.send(
                        f"✅ **Transaksi Berhasil Dicatat!**\n"
                        f"• ID: `{data['id']}`\n"
                        f"• Pelanggan: **{data['customer_name']}**\n"
                        f"• Produk: {data['product_description']}\n"
                        f"• Untung: **Rp {profit:,}**"
                    )
                else:
                    # Ambil pesan error dari FastAPI jika ada
                    error_detail = await response.text()
                    await ctx.send(f"❌ Gagal menyimpan transaksi. Status code: {response.status}\nDetail: `{error_detail}`")

    except Exception as e:
        print(f"Error Koneksi: {e}")
        await ctx.send(f"⚠️ Terjadi error koneksi ke API: {e}")

# command untuk melihat total profit
@bot.command(name="profit")
async def cek_profit(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://127.0.0.1:8000/profit/") as response:

                if response.status == 200:
                    data = await response.json()
                    await ctx.send(
                        f"📊 **Laporan Keuangan Saat Ini**\n"
                        f"Total Keuntungan Bersih: **Rp {data['total_profit']:,}**"
                    )

                else:
                    await ctx.send(f"❌ Gagal mengambil data. Status: {response.status}")

    except Exception as e:
        print(f"Error Koneksi: {e}")
        await ctx.send(f"⚠️ Terjadi error saat menghubungi API: {e}")

if TOKEN is None:
    print("Error: Token Discord tidak di temukan di file .env!")
else:
    bot.run(TOKEN)
