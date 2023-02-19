//|||||||||||||||||||||||||||||||| SAVEDMESSAGES JAVASCRIPT |||||||||||||||||||||||||||||||||||||







//_____________________________________ GET HTML BUTTONS ___________________________________________
//2) grab both of our forms. 
const updateForm = document.getElementById('update-form')
const postForm = document.getElementById('post-form')

//3) add event listeners for both the insert and update forms.
postForm.addEventListener('submit', postData)
updateForm.addEventListener('submit', updateData)


 //4) create buttons-both insert and update forms.
const postButton = document.getElementById('save_to_board')
const updateButton = document.getElementById('save_to_board')
const resetButton = document.getElementById('reset-button')








//______________________________________ ENABLE CLICK TABLE _______________________________________

// this will check the table for available button clicks. 
function clickTable(event) 
    {let target = event.target
    
    
    
    // For the editing button.
    if (target.getAttribute('id') == 'edit-button')   
        {var id = target.parentNode.className.split("-")[1]
        var toUpdate = document.getElementsByClassName(`id-${id}`)
        var contentToUpdate = []
        // '-2' in order to exclude edit and delete buttons
        for (var i = 0; i < toUpdate.length - 2; i++) 
            {contentToUpdate.push(toUpdate[i].textContent)}
        editData(contentToUpdate)}
     
     
     
    // For the delete button.
    if (target.getAttribute('id') == 'delete-button') 
        // each row has a class based on the ID value; e.g. 'id-5'
        {var id = target.parentNode.className.split("-")[1]
        deleteData(id)}}








//__________________________________________ MAKE TABLE __________________________________________

// Create the table headers for each message row.
function generate_table(data) 
    {var table = document.getElementById("Big-table")
    if (table) 
        {table.removeEventListener('click', clickTable)
        table.parentNode.removeChild(table)}
    var container = document.getElementById("all-table")
    var table = document.createElement("table")
    table.setAttribute("id", "Big-table")
    table.setAttribute("class", "board")
    var tableBody = document.createElement("tbody")
    tableBody.setAttribute("class", "pill-nav")
    var tableHead = document.createElement("thead")
    var columns = ["ID", "Send To", "Message", "Edit", "Delete"]
    var headerRow = document.createElement("tr")
    for (var c = 0; c < columns.length; c++) 
        {var headerCell = document.createElement("th")
        var cellText = document.createTextNode(columns[c])
        headerCell.appendChild(cellText)
        headerRow.appendChild(headerCell)}
    tableHead.appendChild(headerRow)
    table.appendChild(tableHead)
     
     
     
     
     
    // build the table with the data that comes in.
    for (var i = 0; i < data.length; i++) 
        {var row = document.createElement("tr")
        var id = data[i]["messageID"]
        row.setAttribute("messageID", `id-${id}`)
        for (const property in data[i]) 
            {var cell = document.createElement("td")
            cell.setAttribute("class", `id-${id}`)
            var text = data[i][property]
        var cellText = document.createTextNode(text)
        cell.appendChild(cellText)
        row.appendChild(cell)}
         
         
         
         
        // create edit button for each row
        var cell = document.createElement("td")
        cell.setAttribute("class", `id-${id}`)
        var cellText = document.createTextNode("Edit")
        var editButton = document.createElement("button")
        editButton.setAttribute("id", "edit-button")
        editButton.appendChild(cellText)
        cell.appendChild(editButton)
        row.appendChild(cell)
         
         
         
         
        // create delete button for each row
        var cell = document.createElement("td")
        cell.setAttribute("class", `id-${id}`)
        var cellText = document.createTextNode("Delete")
        var deleteButton = document.createElement("button")
        deleteButton.setAttribute("id", "delete-button")
        deleteButton.appendChild(cellText)
        cell.appendChild(deleteButton)
        row.appendChild(cell)
        tableBody.appendChild(row)}
        table.appendChild(tableBody)
        container.appendChild(table)
        table.addEventListener('click', clickTable)}







//_____________________________________ GET MESSAGES ___________________________________________

// 1) Grab our data.
function getData()  
    {var req = new XMLHttpRequest()
        req.open('GET', '/get-SavedMessages', true)
        req.addEventListener('load', function () 
            {if (req.status >= 200 && req.status < 400)
                {var response = JSON.parse(req.responseText)
                var data = response.rows
                generate_table(data)
                console.log(JSON.stringify(data))} 
            else   
                {console.log("Error: " + req.statusText)}})
            req.send(null)}










//_____________________________________ INSERT MESSAGES ________________________________________

 // generate table with updated data upon insert SQL.
function postData(event) 
    {var req = new XMLHttpRequest()
    var newTableItem = {messageID: null, sendTo: null, message: null}
    newTableItem.messageID = document.getElementById('update-messageID').value
    newTableItem.sendTo = document.getElementById('to-whom').value
    newTableItem.message = document.getElementById('myText').value
    req.open('POST', '/insert-SavedMessages', true)
    req.setRequestHeader('Content-Type', 'application/json')
    req.addEventListener('load', function () 
        {if (req.status >= 200 && req.status < 400) 
            {var response = JSON.parse(req.responseText)
            var data = response.rows
            generate_table(data)} 
        else 
            {console.log("Error: " + req.statusText)}})
    req.send(JSON.stringify(newTableItem))
    event.preventDefault()}










//_____________________________________ UPATE MESSAGES ________________________________________

// updates an entry in the table when user submits the update or edit form.
function updateData(event) 
    {var req = new XMLHttpRequest()
    var updatedTableItem = {messageID: null, sendTo: null, message: null}
    updatedTableItem.messageID = document.getElementById('update-messageID').value
    updatedTableItem.sendTo = document.getElementById('to-whom').value
    updatedTableItem.message = document.getElementById('myText').value
    req.open('PUT', '/update-SavedMessages', true)
    req.setRequestHeader('Content-Type', 'application/json')
    req.addEventListener('load', function () 
        {if (req.status >= 200 && req.status < 400) 
            {var response = JSON.parse(req.responseText)
            var data = response.rows
            generate_table(data)}     
        else 
            {console.log("Error: " + req.statusText)}})
    req.send(JSON.stringify(updatedTableItem))
    event.preventDefault()}








//_____________________________________ EDITING ___________________________________________

// populate the 'Update' form with the values given by the user.
function editData(contentToUpdate) 
    { document.getElementById('update-messageID').value = contentToUpdate[0]
    document.getElementById('to-whom').value = contentToUpdate[1]
    document.getElementById('myText').value = contentToUpdate[2]}











//___________________________________ DELETE MESSAGES ________________________________________

// accepts a table-generated ID and deletes the the row.
function deleteData(messageID) 
    {var req = new XMLHttpRequest()
    req.open('DELETE', '/delete-SavedMessages', true)
    req.setRequestHeader('Content-Type', 'application/json')
    req.addEventListener('load', function () {
        if (req.status >= 200 && req.status < 400) {
            var response = JSON.parse(req.responseText)
            var data = response.rows
            generate_table(data)} 
        else 
            {console.log("Error: " + req.statusText)}})
    var rowToDelete = {messageID:messageID}
    req.send(JSON.stringify(rowToDelete))}
    










getData()
