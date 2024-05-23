define(function (require){
    let fs = require('fs');
    fs.readFile('output.txt', 'hello', (err) =>{
        if (err) throw err;
    })
})