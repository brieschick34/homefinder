from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

from getTermLength import getTermLength

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/v1/generateAmortizationReport', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type','application/json'])
def generateAmortizationReport():
    # print("Start")
    # print(request.json)
    principal = float(request.json["principal"])
    extraPayment = float(request.json["extraPayment"])
    mortgageAmount = float(request.json["mortgageAmount"])
    interestRate = (float(request.json["interestRate"]) / 12 )
    return(getTermLength(principal, extraPayment, mortgageAmount, interestRate, True))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

# curl --header "Content-Type: application/json" --request "POST" -d "{\"principal\":\"190000\",\"extraPayment\":\"750\",\"mortgageAmount\":\"2250\",\"interestRate\":\".0699\"}" http://localhost:5000/api/v1/generateAmortizationReport   