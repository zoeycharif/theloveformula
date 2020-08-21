// importing the Express app created in app.js
var app = require('./app');

// tell our app to listen on port 3000 for incoming connection 
// and output a message to the terminal to indicate server is running
 
http.createServer(app).listen(app.get('port'),
  function(){
    console.log(`Express is running on port ${server.address().port}`);
});