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
    """ An API that runs the numbers and returns the fun fact"""
    number = request.args.get('number')

    if not number or not number.isdigit():
        return jsonify({"number": "alphabet", "error": True}), 400

    number = int(number)
    digit_sum = sum(int(d) for d in str(number))
    properties = ["even" if number % 2 == 0 else "odd"]

    if is_armstrong(number):
        properties.insert(0, "armstrong")

    response_data = OrderedDict([
        ("number", number),
        ("is_prime", is_prime(number)),
        ("is_perfect", is_perfect(number)),
        ("properties", properties),
        ("digit_sum", f"{digit_sum},  // sum of its digits"),
        ("fun_fact", get_fun_fact(number))
        ])

    return app.response_class(
        response=json.dumps(response_data, indent=4),  # Indentation for readability
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(debug=True)
