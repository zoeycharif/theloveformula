// import express module and routes file into app
// require function is a built-in Node function 
// which imports an object from another file or module
const express = require('express');
const routes = require('./routes/index');


// creating a new Express app using the express function and assigning it to an app variable
// we tell the app that, whenever it receives a request from forward slash /anything, it should use routes file
const app = express();
app.use('/', routes);

module.exports = app;