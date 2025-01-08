var express = require('express');
var router = express.Router();
router.get('/', function(req, res, next) {
  // res.set('Access-Control-Allow-Origin', 'http://localhost:5000');
  res.render('amortization', { pagetitle: 'Generate Amortization Report for Loan' });
});
module.exports = router;