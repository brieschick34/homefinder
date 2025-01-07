var express = require('express');
var router = express.Router();
router.get('/', function(req, res, next) {
  res.render('amortization', { pagetitle: 'Generate Amortization Report for Loan' });
});
module.exports = router;