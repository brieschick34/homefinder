var express = require('express');
var router = express.Router();
router.get('/', function(req, res, next) {
  res.render('tests', { pagetitle: 'Testing Backend Function' });
});
module.exports = router;