# 🚀 NexusLedger - Digital Goods Transaction Tracker

![Status](https://img.shields.io/badge/Status-In_Active_Development-yellow?style=for-the-badge)

An asynchronous, decoupled backend system designed to log, manage, and calculate profit for digital goods transactions (e-wallet top-ups, mobile credit) via an interactive **Discord Bot UI** powered by a **FastAPI** backend and **PostgreSQL** database.

## 🏗️ System Architecture & Data Flow

```
+-------------------+       HTTP Request (JSON)       +-------------------+
|  Discord Channel  | ------------------------------> | Wishpbyte (Cloud) |
|  (User Interface) |                                 |  (Discord Bot)    |
+-------------------+                                 +-------------------+
          ^                                                     |
          |                                      REST API (POST/GET/PUT/DELETE)
          |                                                     v
          |         HTTP Response (JSON)        +-------------------+
          +------------------------------------ |   Vercel (Cloud)  |
                                                |   (FastAPI / API) |
                                                +-------------------+
                                                  ^               |
                                    SQLAlchemy    |               | Data/Status
                                     (Query)      |               v  Response
                                                +-------------------+
                                                | Supabase (Cloud)  |
                                                | (PostgreSQL DB)   |
                                                +-------------------+
```
## 🛠️ Tech Stack & Services
- **Core Backend:** Python 3, FastAPI, Pydantic, SQLAlchemy
- **Database:** PostgreSQL (Hosted on Supabase)
- **API Deployment:** Vercel (Serverless Function)
- **Client Interface:** Discord Bot (discord.py, aiohttp) hosted on Wishpbyte Cloud
- **Architecture Pattern:** Decoupled Client-Server (Separation of Concerns)
## ✨ Features
⚡ **Asynchronous REST API:** High-performance API with interactive Swagger UI documentation.

📊 **Automated Profit Calculation:** Real-time computation of net profit per transaction.

🤖 **Interactive Cashier Bot:** Complete CRUD operations executed via chat commands.

🗄️ **Cloud Data Persistence:** Relational database storage with schema safety.

🌱 **In Active Development:**
- **Dual-Environment Architecture:** Implementing a isolated Development Bot (Staging) to test features locally without affecting Production data.
- **Enhanced UI/UX:** Upgrading text-based commands to Discord Interactive Modals & Buttons.

## 📌 REST API Endpoints Overview
- 📝(`POST /transactions/`): Create a new transaction record

- 📖(`GET /transactions/`): Fetch transaction history

- 💰(`GET /profit/`): Calculate dynamic total profit

- ✏️(`PUT /transactions/{transaction_id}`): Update existing transaction record

- 🗑️(`DELETE /transactions/{transaction_id}`): Remove a transaction

## ⚙️ Environment Configuration (.env)
Configure the `.env` file locally before running the bot client:
```
API_URL=http://127.0.0.1:8000/transactions/
DISCORD_TOKEN=your_discord_bot_token_here
BOT_PREFIX=?
```
## 👤 Author
Developed with passion by **alterremz**:D
