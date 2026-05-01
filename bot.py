import sqlite3
import logging
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# --- အရေးကြီးသွင်းကုန်များ (သင့်ဆီက ဖိုင်တွေဖြစ်ရပါမယ်) ---
try:
    from gatet import Tele
    from hit_sender import send
except ImportError:
    print("Error: 'gatet.py' သို့မဟုတ် 'hit_sender.py' ကို မတွေ့ပါ။")

# --- CONFIGURATION ---
BOT_TOKEN = '' 
ADMIN_ID = 7954343626              

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            credits INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# --- HELPER FUNCTIONS ---
def get_db_connection():
    return sqlite3.connect('bot_database.db')

# --- BOT COMMANDS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 မင်္ဂလာပါ! Yagmi Light Checker မှ ကြိုဆိုပါတယ်။\n\n"
        "သုံးလို့ရတဲ့ Command များ -\n\n"
        "/register - အကောင့်ဖွင့်ပြီး Credit 10 ယူမယ်\n"
        "/balance - လက်ကျန် Credit စစ်မယ်\n"
        "/au - Card စစ်မယ် (1 Credit ကျသင့်)\n"
        "/help - အကူအညီတောင်းမယ်\n\n"
        "ဆက်သွယ်ရန် - @strawhatchannel69"
    )

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    if cursor.fetchone():
        await update.message.reply_text("❌ သင် register လုပ်ပြီးသားပါ။")
    else:
        cursor.execute("INSERT INTO users (user_id, credits) VALUES (?, ?)", (user_id, 10))
        conn.commit()
        await update.message.reply_text("✅ Register အောင်မြင်ပါတယ်။ လက်ဆောင် 10 Credits ရရှိပါတယ်။")
    conn.close()

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT credits FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        await update.message.reply_text(f"💰 သင့်ရဲ့လက်ကျန် Credit: {result[0]}")
    else:
        await update.message.reply_text("⚠️ ကျေးဇူးပြု၍ အရင် /register လုပ်ပါ။")

# --- အဓိက /gay Command (Credit စနစ်ဖြင့်) ---
async def gay_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "NoUsername"
    
    # ၁။ Credit ရှိမရှိ အရင်စစ်မယ်
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT credits FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    
    if not result:
        await update.message.reply_text("⚠️ ကျေးဇူးပြု၍ အရင် /register လုပ်ပါ။")
        conn.close()
        return
    
    if result[0] <= 0:
        await update.message.reply_text("❌ သင့်မှာ Credit မလုံလောက်တော့ပါ။")
        conn.close()
        return

    # ၂။ Argument ပါမပါ စစ်မယ်
    if not context.args:
        await update.message.reply_text("⚠️ Card format လိုအပ်သည်။ ဥပမာ- `/au cc|mm|yy|cvc`", parse_mode="Markdown")
        conn.close()
        return

    cc = context.args[0]
    msg = await update.message.reply_text("Checking your card...")
    start_time = time.time()

    try:
        # ၃။ Card Checker ကို ခေါ်မယ်
        last = str(Tele(cc))
        if "Successfully" in last:
            last = "Charged 💥"
        else:
            last = f"Unknown Response: {last}"
        
        time_taken = round(time.time() - start_time, 2)
        
        # ၄။ Hit Sender နဲ့ ပို့မယ်
        send_response = send(cc, last, username, time_taken)

        # ၅။ Credit ၁ ခု လျှော့မယ်
        new_credits = result[0] - 1
        cursor.execute("UPDATE users SET credits = ? WHERE user_id = ?", (new_credits, user_id))
        conn.commit()

        # ၆။ ရလဒ်ပြန်ပြမယ်
        await msg.edit_text(send_response, parse_mode="HTML")

    except Exception as e:
        logging.error(f"Error: {e}")
        await msg.edit_text("An error occurred during processing.")
    
    conn.close()

# Admin Command
async def add_credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    try:
        target_id, amount = int(context.args[0]), int(context.args[1])
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET credits = credits + ? WHERE user_id = ?", (amount, target_id))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"✅ User {target_id} ဆီသို့ {amount} Credits ထည့်ပြီးပါပြီ။")
    except:
        await update.message.reply_text("Usage: /addcredit [ID] [Amount]")

# --- MAIN ---
if __name__ == '__main__':
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("au", gay_check))
    app.add_handler(CommandHandler("add", add_credit))
    
    print("Bot is running with Credit System...")
    app.run_polling()
