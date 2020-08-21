// importing express into our routes file
var express = require('express');

// then grabbing the router from it
var router = express.Router();

router.get('/', (req, res) => {
	res.send('It works!');
});

module.exports = router;