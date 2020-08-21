// import express module and routes file into app
// require function is a built-in Node function 
// which imports an object from another file or module
var express = require('express');
//const routes = require('./routes/index');


// creating a new Express app using the express function and assigning it to an app variable
// we tell the app that, whenever it receives a request from forward slash /anything, it should use routes file
var app = express();

app.set('port', process.env.PORT || 8080);

app.get('/', function(req, res){
	res.send('hello');
});

app.listen(app.get('port'));

module.exports = app;