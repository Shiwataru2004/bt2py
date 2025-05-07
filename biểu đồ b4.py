from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # === 1. Giả lập dữ liệu thời tiết, giá vàng, tỷ giá đô ===
    today = datetime.datetime.now().strftime('%d/%m/%Y')
    weather = {
        "ngay": today,
        "nhiet_do": "34°C",
        "mo_ta": "Trời nắng nóng",
        "do_am": "60%",
        "gio": "15 km/h"
    }

    gold_price = 6850000  # VND/lượng
    usd_rate = 24500  # VND/USD

    # === 2. Dữ liệu biểu đồ (giá lập theo tháng) ===
    months = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6']
    gold_prices = [6750000, 6780000, 6800000, 6820000, 6840000, 6850000]
    usd_rates =   [24300,   24500,   24400,   24420,   24540,   24500]

    return render_template("index1.html",
                           weather=weather,
                           gold_price=gold_price,
                           usd_rate=usd_rate,
                           months=months,
                           gold_prices=gold_prices,
                           usd_rates=usd_rates)

if __name__ == '__main__':
    app.run(debug=True)
