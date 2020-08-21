// importing express into our routes file
const express = require('express');

// then grabbing the router from it
const router = express.Router();

router.get('/', (req, res) => {
	res.send('It works!');
});

module.exports = router;