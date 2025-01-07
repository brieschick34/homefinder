var express = require('express');
var router = express.Router();
router.get('/', function(req, res, next) {
  res.render('optimize', { pagetitle: 'Optimizing Home Loan Costs' });
});
module.exports = router;