function CheckCreateNewuser(){
    document.getElementById("newuser").submit();
    console.log(username);





};

function temp(){



    

    var mysql = require('mysql');

    var conn = mysql.createConnection({
        host: "ec2-34-237-89-96.compute-1.amazonaws.com",
        user: "rhjtenpwhdlbjl",
        password: "4d3153a71d04ee752de8aab6fb6ac3baaff5fe615aa7a6223845aab661e0c6af",
        database: "d1l8p7t7cs19l8"
    });
    console.log(username);
    conn.connect((err)=>{
        if (err) throw err;
  
        var sql = 'select * from profiles where username = ' + username;
        conn.query(sql, (err, result, fields)=>{
        if (err) throw err;
    console.log(result);
  });
});
}
