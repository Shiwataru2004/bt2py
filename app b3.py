from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # === 1. Thời tiết (sử dụng API của open-meteo.com miễn phí) ===
    weather = {}
    try:
        weather_url = "https://api.open-meteo.com/v1/forecast?latitude=21.03&longitude=105.85&current_weather=true"
        response = requests.get(weather_url)
        data = response.json()
        weather_data = data.get('current_weather', {})
        weather = f"{weather_data.get('temperature', '?')}°C, gió {weather_data.get('windspeed', '?')} km/h"
    except Exception as e:
        weather = "Không lấy được dữ liệu thời tiết."

    # === 2. Giá vàng (giả lập vì chưa có API miễn phí tốt cho VN) ===
    gold_price = "68.500.000 VNĐ/lượng"  # Có thể thay bằng web scraping hoặc API nếu có

    # === 3. Tỷ giá đô la (sử dụng API của exchangerate.host) ===
    usd_rate = ""
    try:
        usd_api = "https://api.exchangerate.host/latest?base=USD&symbols=VND"
        response = requests.get(usd_api)
        rate = response.json().get('rates', {}).get('VND', None)
        usd_rate = f"{rate:,.0f} VNĐ/USD" if rate else "Không có dữ liệu"
    except Exception as e:
        usd_rate = "Không lấy được tỷ giá đô."

    return render_template("index.html", weather=weather, gold_price=gold_price, usd_rate=usd_rate)

if __name__ == '__main__':
    app.run(debug=True)
