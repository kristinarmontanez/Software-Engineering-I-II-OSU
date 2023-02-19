//||||||||||||||||||||||||||||||||||||||| INDEX.JS |||||||||||||||||||||||||||||||||||||||||




//__________________________________ EXPRESS SETUP ___________________________________________

const express = require('express')
var app = express()
app.use(express.json())
app.use(express.urlencoded({extended: true}))
const path = require('path')
PORT = 3113
var db = require('./database/db-connector')






//____________________________________ HANDLEBARS SETUP ________________________________________

var exphbs = require('express-handlebars')
app.engine('.hbs', exphbs
    ({extname: ".hbs"}))
app.set('view engine', '.hbs')
app.use(express.static('public'))




//___________________________________ INTRO ROUTES _______________________________________________


app.get('/', function (req, res) {
  res.render("index", {
      title: 'Secret Pen Pal',
      indexActive: true})})



app.get('/About', (req, res) => {
  res.render('About', {
      title: 'About Secret Pen Pal',
      AboutActive: true})})


app.get('/Contact', (req, res) => {
  res.render('Contact', {
      title: 'Contact Secret Pen Pal',
      AboutActive: true})})





//____________________________________BOARD MESSAGE ROUTES________________________________________


  // BOARD MESSAGE CRUD FUNCTIONS:
  const getAllSavedMessages = `SELECT messageID, sendTo, message FROM SavedMessages ORDER BY messageID`
  const insertSavedMessages = "INSERT INTO SavedMessages (`sendTo`, `message`) VALUES (?, ?)"
  const updateSavedMessages = `UPDATE SavedMessages SET sendTo=?, message=?, WHERE messageID=?`
  const deleteSavedMessages = `DELETE FROM SavedMessages WHERE messageID=?`
  
  
  // Function to return all the date from the existing table
  function SavedMessagesTableData(res, next) 
      {db.pool.query(getAllSavedMessages, function(err, rows, fields) 
        {if(err) 
            {next(err)
                return}
        res.send({rows})})}
  

  //-----------------GET FUNCTION-------------------
  app.get('/get-SavedMessages', (req, res) =>
        {SavedMessagesTableData(res)})

  
  // ---------------INSERT FUNCTION----------------
  app.post('/insert-SavedMessages', (req, res, next) =>
      {const { sendTo, message, messageID} = req.body
      db.pool.query(insertSavedMessages, [sendTo, message, messageID], (err, result) =>
      {if(err) 
          {next(err) 
              return}
        SavedMessagesTableData(res)})})

    // -----------------UPDATE FUNCTION-------------
    app.put('/update-SavedMessages', (req, res, next) => 
    {const {sendTo, message, messageID} = req.body
        db.pool.query(updateSavedMessages, [sendTo, message, messageID], (err, result) =>
        {if(err) 
            {next(err)
                return}
        SavedMessagesTableData(res)})})
  
  // -----------------DELETE FUNCTION-------------
  app.delete('/delete-SavedMessages', (req, res, next) =>
        {db.pool.query(deleteSavedMessages, [req.body.messageID], (err, result) =>
            {if(err) 
                {next(err)
                return}
        SavedMessagesTableData(res)})})









        
//---------------------------------------LISTENER-----------------------------------------
 app.listen(PORT, function()
    {console.log('Express started on http://localhost:' + PORT + '; press Ctrl-C to terminate.')})
