from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Đây chỉ là giá trị ví dụ, bạn nên thay bằng dữ liệu lấy từ API
    weather = "Nắng, 34°C"
    gold_price = "68.500.000 VND/lượng"
    usd_rate = "25.200 VND/USD"

    return render_template("index.html", weather=weather, gold_price=gold_price, usd_rate=usd_rate)

if __name__ == '__main__':
    app.run(debug=True)
