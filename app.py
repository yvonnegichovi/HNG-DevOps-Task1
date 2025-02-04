from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def is_prime(n):
    """ Checks if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    """ Checks if a number is a perfect number """
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n


def is_armstrong(n):
    """ Checks if a number is an Armstrong number """
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n


def get_fun_fact(n):
    """ Returns a fun fact from Numbers API """
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return f"{n} is an Armstrong number because {' + '.join(f'{d}^{len(str(n))}' for d in str(n))} = {n} //gotten from the numbers API"
        return "No fact available."
    except requests.RequestException:
        return "Could not retrieve a fact."


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
    
    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": get_fun_fact(number)
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
