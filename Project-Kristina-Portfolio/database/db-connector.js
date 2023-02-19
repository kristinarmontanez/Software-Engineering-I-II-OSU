//____________________________________ DATABASE SETUP ________________________________________

// MySQL is used for engr.oregonstate database.
var mysql = require('mysql')

var pool = mysql.createPool({
    connectionLimit : 10,
    host            : 'classmysql.engr.oregonstate.edu',
    user            : 'cs361_montanek',
    password        : '________________',
    database        : '________________'
})



// Export it for use in our applicaiton
module.exports.pool = pool;
