var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const axios = require('axios');
// const cors = require('cors')

// create route objectsvar index
Router = require('./routes/index');
var aboutRouter = require('./routes/about');
var contactRouter = require('./routes/contact');
var testsRouter = require('./routes/tests');
var amortization = require('./routes/amortization');
var optimizeRouter = require('./routes/optimize');
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

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

// app.use((req, res, next) => {
//   res.header('Access-Control-Allow-Origin','*');
//   res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
//   res.header('Access-Control-Allow-Credentials', true);
//   res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH');
//   next();
// });

app.post('/generateAmortizationReport', (req, res) => {
  // Process the POST data here
  console.log(req.body); 
  axios.post("http://localhost:5000/api/v1/generateAmortizationReport", {
      principal: req.body.principal,
      extraPayment: req.body.extraPayment,
      mortgageAmount: req.body.mortgageAmount,
      interestRate: req.body.interestRate
    })
    .then((response) => console.log(response.data))
    .catch((err) => console.error(err));
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

module.exports = app;
