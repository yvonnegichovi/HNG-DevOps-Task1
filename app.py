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

    if not num_str:
        return jsonify({"number": "alphabet", "error": True}), 400

    try:
        number = float(num_str)  # Allow floating-point numbers
    except ValueError:
        return jsonify({"number": "alphabet", "error": True}), 400

    # Check if the number is an integer
    is_integer = number.is_integer()
    properties = []

    if is_integer:
        int_number = int(number)
        if is_armstrong(int_number):
            properties.append("armstrong")
        properties.append("odd" if int_number % 2 != 0 else "even")

    # Get a fun fact (Numbers API works for all numbers)
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math?json", timeout=5)
        fun_fact = response.json().get("text", "No fun fact available.") if response.status_code == 200 else "No fun fact available."
    except Exception:
        fun_fact = "No fun fact available."

    # Custom Armstrong message
    if is_integer and is_armstrong(int_number) and "armstrong" not in fun_fact.lower():
        fun_fact = f"{int_number} is an Armstrong number because " + " + ".join(f"{d}^{len(str(int_number))}" for d in str(abs(int_number))) + f" = {int_number}"

    result = {
        "number": number if "." in num_str else int(number),  # Keep floats as floats, integers as integers
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number) if is_integer else None,  # Only for integers
        "fun_fact": fun_fact
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
