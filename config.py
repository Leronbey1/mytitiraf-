#################################
# itiraf Club Bot #
#################################
# Repo Sahibi - meyitzade47
# Telegram - t.me/meyitzade47 
# Support - t.me/hirasettr
# GitHub - 01-Meyitzade-01
#################################
#################################
# Bu repo sıfırdan yapıldı
# Başka github hesabına yüklüme olmaz
# Reponu kendi adına importla...!!!
#################################
#################################
#
import os
import heroku3
from telethon import TelegramClient, events
#
# Buranı kurcalama
# Yalnız deploy buttonuyla botunu yarat
# 
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
admin_qrup = int(os.environ.get("ADMIN_QRUP"))
etiraf_qrup = int(os.environ.get("ETIRAF_QRUP"))
kanal = os.environ.get("kanal")
log_qrup = int(os.environ.get("LOG_QRUP"))
botad = os.environ.get("BOT_AD")
etirafmsg = os.environ.get("etirafmsg")
startmesaj = os.environ.get("startmesaj")
etirafyaz = os.environ.get("etirafyaz")
qrupstart = os.environ.get("qrupstart")
gonderildi = os.environ.get("gonderildi")
support = os.environ.get("support")
sahib = os.environ.get("sahib")
#
# Hirasettr 
# Hirasettr 
# Hirasettr 

