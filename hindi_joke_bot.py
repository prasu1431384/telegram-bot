import telebot
import requests

# अपना Telegram Bot Token और Hindi Jokes API कुंजी यहां डालें
BOT_TOKEN = '7770287881:AAEKXrrbtjkurbl-6OZCzFTnNNeYn71Q_fk'
API_KEY = 'c00c56ddb8559cb98ddd56fc1883'

# बॉट को इनिशियलाइज़ करें
bot = telebot.TeleBot(BOT_TOKEN)

# जब कोई /start कमांड भेजे
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "नमस्ते! मैं आपको हिंदी में मजेदार जोक्स सुनाऊंगा। जोक सुनने के लिए /joke लिखिए।")

# जब कोई /joke कमांड भेजे
@bot.message_handler(commands=['joke'])
def send_joke(message):
    try:
        # API से जोक प्राप्त करें
        response = requests.get(f'https://hindi-jokes-api.onrender.com/jokes?api_key={API_KEY}')
        joke_data = response.json()
        if joke_data['status'] == 'Success':
            joke = joke_data['jokeContent']
        else:
            joke = "माफ़ कीजिए, इस समय जोक प्राप्त नहीं हो सका।"
    except Exception as e:
        joke = "माफ़ कीजिए, इस समय जोक प्राप्त नहीं हो सका।"
    bot.reply_to(message, joke)

print("बॉट चल रहा है...")
bot.polling()
