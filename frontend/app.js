var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const axios = require('axios');
var http = require('http');
// const cors = require('cors')

// create route objectsvar index
Router = require('./routes/index');
var aboutRouter = require('./routes/about');
var contactRouter = require('./routes/contact');
var testsRouter = require('./routes/tests');
var amortization = require('./routes/amortization');
var optimizeRouter = require('./routes/optimize');
var generateAmortizationReport = require('./routes/generateAmortizationReport');

var indexRouter = require('./routes/index');

var app = express();
app.use(express.static(path.join(__dirname, 'public')));

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// app.use(cors())
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

// tell the app to use these routes
app.use('/', indexRouter);
app.use('/about', aboutRouter);
app.use('/contact', contactRouter);
app.use('/tests', testsRouter);
app.use('/amortization', amortization);
app.use('/optimize', optimizeRouter);

// API Communication
app.use('/generateAmortizationReport', generateAmortizationReport);

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// app.get('/generateAmortizationReport', (req, res) => {
//   var options = {
//     host: "127.0.0.1",
//     port: 5000,
//     path: "/api/v1/generateAmortizationReport",
//     method: "GET"
//   }

//   // Process the GET data here
//   var req = http.get(options, function(res) {
//     console.log('STATUS: ' + res.statusCode);
//     console.log('HEADERS: ' + JSON.stringify(res.headers));
//     // Buffer the body entirely for processing as a whole.
//     var bodyChunks = [];
//     res.on('data', function(chunk) {
//       // You can process streamed parts here...
//       bodyChunks.push(chunk);
//     }).on('end', function() {
//       var body = Buffer.concat(bodyChunks);
//       console.log('BODY: ' + body);
//       // ...and/or process the entire body here.
//     })
//   });
//   let headers = ["Payment #", "Payment Amount", "Interest", "Principal Paid", "Remaining Balance"]
//   let tableHTML = '<table><thead><tr>';
  
//   console.log("----------------------------------------------------------------------------------")
//   console.log(response)
//   for (const header in headers) {
//     tableHTML += `<th>${header}</th>`;
//   }
//   tableHTML += '</tr></thead><tbody>';

//   for (const row of data) {
//     tableHTML += '<tr>';
//     for (const key in row) {
//       tableHTML += `<td>${row[key]}</td>`;
//     }
//     tableHTML += '</tr>';
//   }

//   tableHTML += '</tbody></table>';

//   res.send(tableHTML);
// });

// app.post('/generateAmortizationReport', (req, res) => {
//   // Process the POST data here
//   console.log(req.body); 
//   const response = axios.post("http://localhost:5000/api/v1/generateAmortizationReport", {
//       principal: req.body.principal,
//       extraPayment: req.body.extraPayment,
//       mortgageAmount: req.body.mortgageAmount,
//       interestRate: req.body.interestRate
//     })
//     .then((response) => console.log(response.data))
//     .catch((err) => console.error(err));
//   const data = response.data;
  
//   let headers = ["Payment #", "Payment Amount", "Interest", "Principal Paid", "Remaining Balance"]
//   let tableHTML = '<table><thead><tr>';
  
//   console.log("----------------------------------------------------------------------------------")
//   console.log(response)
//   for (const header in headers) {
//     tableHTML += `<th>${header}</th>`;
//   }
//   tableHTML += '</tr></thead><tbody>';

//   // for (const row of data) {
//   //   tableHTML += '<tr>';
//   //   for (const key in row) {
//   //     tableHTML += `<td>${row[key]}</td>`;
//   //   }
//   //   tableHTML += '</tr>';
//   // }

//   tableHTML += '</tbody></table>';

//   res.send(tableHTML);
// });

// // catch 404 and forward to error handler
// app.use(function(req, res, next) {
//   next(createError(404));
// });

module.exports = app;
