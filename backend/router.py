from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

from getTermLength import getTermLength


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/v1/generateAmortizationReport', methods=['GET', 'POST'])
@cross_origin(origin='localhost',headers=['Content-Type','application/json'])
def generateAmortizationReport():
    print("MADE IT TO PYTHON!")
    if request.method == 'POST':
        print("POST REQUEST!")
        principal = float(request.json["principal"])
        extraPayment = float(request.json["extraPayment"])
        mortgageAmount = float(request.json["mortgageAmount"])
        interestRate = (float(request.json["interestRate"]) / 12 )
        getTermLength(principal, extraPayment, mortgageAmount, interestRate, True)
    elif request.method == 'GET':
        print("GET REQUEST!")
        query_string = request.query_string
        print("QUERY STRING" + str(query_string))
        principal = float(request.args["principal"])
        extraPayment = float(request.args["extraPayment"])
        mortgageAmount = float(request.args["mortgageAmount"])
        interestRate = (float(request.args["interestRate"]) / 12 )
        return json.dumps(getTermLength(principal, extraPayment, mortgageAmount, interestRate, False)[2])
    else:
        print("METHOD NOT SUPPORTED")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

# curl --header "Content-Type: application/json" --request "POST" -d "{\"principal\":\"190000\",\"extraPayment\":\"750\",\"mortgageAmount\":\"2250\",\"interestRate\":\".0699\"}" http://localhost:5000/api/v1/generateAmortizationReport   