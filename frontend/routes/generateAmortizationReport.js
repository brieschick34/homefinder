var express = require('express');
var router = express.Router();
var http = require('http');


router.get('/', function(req, res, next) {
  const path = `/api/v1/generateAmortizationReport?principal=${req.query.principal}&extraPayment=${req.query.extraPayment}&mortgageAmount=${req.query.mortgageAmount}&interestRate=${req.query.interestRate}`
  console.log("PATH FROM JS: " + path)
  var options = {
    host: "localhost",
    port: 5000,
    path: path,
    method: "GET",
    headers: {
      'Content-Type': 'application/json'
    }
  }
  
    // Process the GET data here
    var request = http.get(options, function(res) {
      console.log('STATUS: ' + res.statusCode);
      console.log('HEADERS: ' + JSON.stringify(res.headers));
      // Buffer the body entirely for processing as a whole.
      var bodyChunks = [];
      res.on('data', function(chunk) {
        // You can process streamed parts here...
        bodyChunks.push(chunk);
      }).on('end', function() {
        var body = Buffer.concat(bodyChunks);
        console.log('BODY: ' + body);
        // res.send(body);
        // ...and/or process the entire body here.
      })
    });
});
module.exports = router;