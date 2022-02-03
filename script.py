from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):
  ABOUT = """
🤖 **Adım:** {bot_name}

📝 **Dil:** [Python](https://www.python.org)

📚 **Kütüphane:** [Pyrogram](https://docs.pyrogram.org)

📡 **Sunucu:** [Heroku](https://heroku.com)

🧑‍💻 **Geliştirici:** [Kanal](https://t.me/trbotlistesi)

👥 **Destek:** [Grup](https://t.me/trbotlistesidestek)

📢 **Kanalım:** [Kanal](https://t.me/trbotlistesi)
"""

  HELP_USER = """
Ben **{bot_name}**

Yardım Kısmına Hoşgeldin

1.) Bir Video Dosyası Gönder.
2.) Bir Altyazı Dosyası Gönder. (ass Yada srt)
3.) Altyazı Türünü Seç!

Dosyaya özel ad vermek için url ile ayrılmış olarak gönderin.|
url|custom_name.mp4

Not :Hardmux'ta yalnızca İngilizce yazı tiplerinin desteklendiğini lütfen unutmayın, diğer komut dosyaları videoda boş bloklar olarak gösterilecektir! 

**Oluşturan 💕 @trbotlistesi**
"""

  START_TEXT = """
**Hey** {user_mention}

Hoşgeldin **{bot_name}**\n
Sana Videolara Altyazı Eklemen Konusunda Yardımcı Olacağım\n
**Oluşturan 💕 @trbotlistesi**
"""

    
    
