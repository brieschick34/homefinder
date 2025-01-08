from flask import Flask
from flask import request

from getTermLength import getTermLength

app = Flask(__name__)

@app.route('/api/v1/generateAmortizationReport', methods=['POST'])
def generateAmortizationReport():
    principal = float(request.json["principal"])
    extraPayment = float(request.json["extraPayment"])
    mortgageAmount = float(request.json["mortgageAmount"])
    interestRate = float(request.json["interestRate"])
    getTermLength(principal, extraPayment, mortgageAmount, interestRate, True)
    return(request.json)

# def call_function(function_name: str):
#     function_to_call = getattr(functions, function_name)
#     body = request.json
#     return function_to_call(body)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

# curl --header "Content-Type: application/json" --request "POST" -d "{\"principal\":\"190000\",\"extraPayment\":\"750\",\"mortgageAmount\":\"2250\",\"interestRate\":\".0699\"}" http://localhost:5000/api/v1/generateAmortizationReport   