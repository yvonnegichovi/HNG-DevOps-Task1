from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from collections import OrderedDict

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_perfect(n):
    if n < 2:
        return False
    total = 1  # 1 is always a proper divisor (if n > 1)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d)**power for d in digits) == n

def digit_sum(n):
    return sum(int(d) for d in str(n))

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num_str = request.args.get('number')

    if not num_str or not num_str.isdigit():
        return jsonify({"number": "alphabet", "error": True}), 400

    number = int(num_str)

    prime = is_prime(number)
    perfect = is_perfect(number)
    armstrong = is_armstrong(number)
    d_sum = digit_sum(number)
    parity = "odd" if number % 2 != 0 else "even"

    properties = ["armstrong", parity] if armstrong else [parity]

    try:
        response = requests.get(f"http://numbersapi.com/{number}/math?json", timeout=5)
        fun_fact = response.json().get("text", "No fun fact available.") if response.status_code == 200 else "No fun fact available."
    except Exception:
        fun_fact = "No fun fact available."

    if armstrong and "armstrong" not in fun_fact.lower():
        fun_fact = f"{number} is an Armstrong number because " + " + ".join(f"{d}^{len(str(number))}" for d in str(number)) + f" = {number}"

    result = {
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": d_sum,
        "fun_fact": fun_fact
    }

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)
