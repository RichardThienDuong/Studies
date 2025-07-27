require('dotenv').config();
// to load the environment variables

let express = require('express');
// require function is a part of Node.js and is used to import modules , Node.js will look 
// for the Express.js module in your "node_modules" directory, and will return the exports of that module. 
// now that all the access of the exports of the express.js module can be accessed with variable express.

let app = express(); 
// we calling express variable with parentheses will result in a new instance of an Express application, 
// which has methods for routing HTTP requests, configuring middleware, rendering HTML views, and more. 
// now we can use app variable to interact with the express application. 


/*  
    app.METHOD(PATH, HANDLER) 
    - app is the new express application we can interact with
    - METHOD is where the http methods go 
    - PATH is a relative path on the server (it can be a string, or even a regular expression)
    - HANDLER is a function that express calls when the rout is matched. 
        Handlers take the form "function(req, res) {...}" 
        Like an Example : 
            function(req, res){
                res.send('Response String');
            }
        the handler will serve the string 'Response String' when the route is matched.

*/

app.get('/', function(req, res) {
    res.send('Hello Express');
});
// once we got the path '/' root directory then we send a response Hello express 

absolutePath = __dirname + '/views/index.html';
app.get('/', function(req, res) {
    res.sendFile(absolutePath);
});
// __dirname is a built-in Node.js variable that gets the directory name of the current module,
// it's the path to the folder where your current Javascript file is located.
// '/views/index.html' is the path to the HTML file you want to send,
// relative to the directory of your current Javascript file. 

app.use("/public", express.static(__dirname + "/public"));
// app.use is a function call that sets up middleware for your application.
// Middleware are functions that have access to the request object(req), the responcse object(res),
// and the next middle finction in the application's request-response cycle. 
// These functions can execute any code, make changes to the request and the response objects,
// end the request-response cycle, or call the next middleware function in the stack. 
// If no path specified. it defaults to "/" (the root path). 
// express.static() make static assets needed by your application in more directories possible

app.get("/json", function(req, res){
    res.json({
        "message": "Hello json"
    });
});
// respond with json format info 

app.get("/json", function(req, res) {
    let response = {"message": "Hello json"};
        if(process.env['MESSAGE_STYLE'] === "uppercase"){
          response["message"] = "Hello json".toUpperCase();
        };
    res.send(response);
  });
// working with env variables , they are variables only admin can see, usually used for
// api keys, database URI, store configuration options 
// ( which can change the behavior of your application, without the need to rewrite some code.)

app.use(function(req, res, next){
    const method = req.method;
    const path = req.path;
    const ip = req.ip;
  
    console.log(`${method} ${path} - ${ip}`);
    next();
  });
  // this should usually be placed right after the express variable is created

  app.get('/now', function(req, res, next) {
    req.time = new Date().toString();
    next();
  }, function(req, res) {
    res.json({time: req.time});
  });
// using app (express application) get (method) to the path '/now' and sending the universal time currently.
// mounted middleware function , chained middleware to create a time server 

app.get('/:word/echo', function(req, res, next) {
    next();
  }, function(req, res) {
    res.json({echo: req.params.word})
  });
  // getting route parameter input from the client 

  app.route('/name').get(function(req, res) {
    let firstName = req.query.first;
    let lastName = req.query.last;
    let responseObject = {name: firstName + " " + lastName};
    res.json(responseObject);
  });
  // get query input parameters from clients 

  app.use(bodyParser.urlencoded({extended: false}));
  // for parsing body info from post request to our server from client , 

  app.post('/name', function(req, res) {
    res.send({name: `${req.body.first} ${req.body.last}`});
  });
  // grabs parsed data and post it on the browser ( i think )

  