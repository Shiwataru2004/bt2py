from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL API (sử dụng bản demo hoặc bạn có API key thật thì thay vào)
GOLD_API_URL = 'https://metals-api.com/api/latest?access_key=YOUR_GOLD_API_KEY&base=USD&symbols=XAU'
WEATHER_API_URL = 'https://api.open-meteo.com/v1/forecast?latitude=21.0285&longitude=105.8542&current_weather=true'
CURRENCY_API_URL = 'https://v6.exchangerate-api.com/v6/YOUR_CURRENCY_API_KEY/latest/USD'

@app.route('/')
def index():
    # Gọi API (có thể cần xử lý lỗi nếu API bị lỗi hoặc thiếu key)
    try:
        gold_data = requests.get(GOLD_API_URL).json()
        weather_data = requests.get(WEATHER_API_URL).json()
        currency_data = requests.get(CURRENCY_API_URL).json()
    except:
        gold_data = weather_data = currency_data = {}

    return render_template('index.html',
                           gold=gold_data,
                           weather=weather_data,
                           currency=currency_data)

if __name__ == '__main__':
    app.run(debug=True)
