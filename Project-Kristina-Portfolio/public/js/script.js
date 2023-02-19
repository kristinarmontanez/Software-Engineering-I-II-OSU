//||||||||||||||||||||||||||||||||||||||| SCRIPT.JS |||||||||||||||||||||||||||||||||||||||||




// To save a text file, I found javascript that will allow a user to 
// save the text file after typing in the textbox. The script was 
// provided by Websparrow, at:
// https://www.websparrow.org/web/how-to-create-and-save-text-file-in-javascript



// "File-Saver" Library:
//_____________________________________________________________________________________
// Because this is a "library", The comments/code are left unchanged for purposes of 
// cleaning up smells. 

var _global = typeof window === 'object' && window.window === window
  ? window : typeof self === 'object' && self.self === self
  ? self : typeof global === 'object' && global.global === global
  ? global
  : this

function bom (blob, opts) {
  if (typeof opts === 'undefined') opts = { autoBom: false }
  else if (typeof opts !== 'object') {
    console.warn('Deprecated: Expected third argument to be a object')
    opts = { autoBom: !opts }
  }

  // prepend BOM for UTF-8 XML and text/* types (including HTML)
  // The browser will automatically convert UTF-16 U+FEFF to EF BB BF
  if (opts.autoBom && /^\s*(?:text\/\S*|application\/xml|\S*\/\S*\+xml)\s*;.*charset\s*=\s*utf-8/i.test(blob.type)) {
    return new Blob([String.fromCharCode(0xFEFF), blob], { type: blob.type })
  }
  return blob
}

function download (url, name, opts) {
  var xhr = new XMLHttpRequest()
  xhr.open('GET', url)
  xhr.responseType = 'blob'
  xhr.onload = function () {
    saveAs(xhr.response, name, opts)
  }
  xhr.onerror = function () {
    console.error('could not download file')
  }
  xhr.send()
}

function corsEnabled (url) {
  var xhr = new XMLHttpRequest()
  // use sync to avoid popup blocker
  xhr.open('HEAD', url, false)
  try {
    xhr.send()
  } catch (e) {}
  return xhr.status >= 200 && xhr.status <= 299
}

// `a.click()` doesn't work for all browsers (#465)
function click (node) {
  try {
    node.dispatchEvent(new MouseEvent('click'))
  } catch (e) {
    var evt = document.createEvent('MouseEvents')
    evt.initMouseEvent('click', true, true, window, 0, 0, 0, 80,
                          20, false, false, false, false, 0, null)
    node.dispatchEvent(evt)
  }
}

// Detect WebView inside a native macOS app by ruling out all browsers
// We just need to check for 'Safari' because all other browsers (besides Firefox) include that too
// https://www.whatismybrowser.com/guides/the-latest-user-agent/macos
var isMacOSWebView = _global.navigator && /Macintosh/.test(navigator.userAgent) 
&& /AppleWebKit/.test(navigator.userAgent) && !/Safari/.test(navigator.userAgent)

var saveAs = _global.saveAs || (
  // probably in some web worker
  (typeof window !== 'object' || window !== _global)
    ? function saveAs () { /* noop */ }

  // Use download attribute first if possible (#193 Lumia mobile) unless this is a macOS WebView
  : ('download' in HTMLAnchorElement.prototype && !isMacOSWebView)
  ? function saveAs (blob, name, opts) {
    var URL = _global.URL || _global.webkitURL
    var a = document.createElement('a')
    name = name || blob.name || 'download'

    a.download = name
    a.rel = 'noopener' // tabnabbing

    // TODO: detect chrome extensions & packaged apps
    // a.target = '_blank'

    if (typeof blob === 'string') {
      // Support regular links
      a.href = blob
      if (a.origin !== location.origin) {
        corsEnabled(a.href)
          ? download(blob, name, opts)
          : click(a, a.target = '_blank')
      } else {
        click(a)
      }
    } else {
      // Support blobs
      a.href = URL.createObjectURL(blob)
      setTimeout(function () { URL.revokeObjectURL(a.href) }, 4E4) // 40s
      setTimeout(function () { click(a) }, 0)
    }
  }

  // Use msSaveOrOpenBlob as a second approach
  : 'msSaveOrOpenBlob' in navigator
  ? function saveAs (blob, name, opts) {
    name = name || blob.name || 'download'

    if (typeof blob === 'string') {
      if (corsEnabled(blob)) {
        download(blob, name, opts)
      } else {
        var a = document.createElement('a')
        a.href = blob
        a.target = '_blank'
        setTimeout(function () { click(a) })
      }
    } else {
      navigator.msSaveOrOpenBlob(bom(blob, opts), name)
    }
  }

  // Fallback to using FileReader and a popup
  : function saveAs (blob, name, opts, popup) {
    // Open a popup immediately do go around popup blocker
    // Mostly only available on user interaction and the fileReader is async so...
    popup = popup || open('', '_blank')
    if (popup) {
      popup.document.title =
      popup.document.body.innerText = 'downloading...'
    }

    if (typeof blob === 'string') return download(blob, name, opts)

    var force = blob.type === 'application/octet-stream'
    var isSafari = /constructor/i.test(_global.HTMLElement) || _global.safari
    var isChromeIOS = /CriOS\/[\d]+/.test(navigator.userAgent)

    if ((isChromeIOS || (force && isSafari) || isMacOSWebView) && typeof FileReader !== 'undefined') {
      // Safari doesn't allow downloading of blob URLs
      var reader = new FileReader()
      reader.onloadend = function () {
        var url = reader.result
        url = isChromeIOS ? url : url.replace(/^data:[^;]*;/, 'data:attachment/file;')
        if (popup) popup.location.href = url
        else location = url
        popup = null // reverse-tabnabbing #460
      }
      reader.readAsDataURL(blob)
    } else {
      var URL = _global.URL || _global.webkitURL
      var url = URL.createObjectURL(blob)
      if (popup) popup.location = url
      else location.href = url
      popup = null // reverse-tabnabbing #460
      setTimeout(function () { URL.revokeObjectURL(url) }, 4E4) // 40s
    }
  }
)

_global.saveAs = saveAs.saveAs = saveAs

if (typeof module !== 'undefined') {
  module.exports = saveAs;
}

//_________________________________________________________________________________________










//________________________________ADDITIONAL BUTTON FUNCTIONS________________________________





//________________________________________________________________
//Ability to save text to a text file "SecretMessage.txt". 
function saveDynamicDataToFile() {
  var userInput = document.getElementById("myText").value;
  var blob = new Blob([userInput], { type: "text/plain;charset=utf-8" });
  saveAs(blob, "SecretMessage.txt");
            }





//________________________________________________________________
//Warning windows for emailing content in textbox. 
function emailToFriend() {
  var inputField = document.getElementById("myText").value;
  var subjectField = document.getElementById("to-whom").value;
  var link = "mailto:me@example.com"
             + "?cc=montanek@oregonstate.edu"
             + "&subject=" + subjectField
             + "&body=" + inputField
  window.open(link)}





//________________________________________________________________
//Warning windows for user resetting textbox. 
function myFunction() {
  var inputField = document.getElementById("myText");
  var btn = document.getElementById("reset_button");
  if (confirm("Are you sure you want to delete your message?")) {
      inputField.value = "";} 
  else 
    {pass;} }




//________________________________________________________________
// Textbox Encrypt. 
function encryptFunct() 
  {const originalMessage = document.getElementById("myText").value
    console.log(`Your original message was:`)
    console.log(`${originalMessage}`)
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    let raw = JSON.stringify({
    "message": originalMessage});
    

    let requestOptions = 
      {method: 'POST',
      headers: myHeaders,
      body: raw };
   

    fetch("https://cs361-ms-crypto.uw.r.appspot.com/encrypt", requestOptions)
    .then(response => response.json())
    .then(result => {
                    document.getElementById("myText").value = result.message
                    console.log(`Your encrypted message is now:`)
                    console.log(`${result.message}`)
                    })
    .catch(error => console.log('error', error));}


  
  
  




//________________________________________________________________
// Textbox Decrypt. 
function decryptFunct() 
  {const encryptedMessage= document.getElementById("myText").value
    console.log(`Your encrypted message was:`)
    console.log(`${encryptedMessage}`)
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    let raw = JSON.stringify({
    "message": encryptedMessage});
    
    let requestOptions = 
      {method: 'POST',
      headers: myHeaders,
      body: raw };
   

    fetch("https://cs361-ms-crypto.uw.r.appspot.com/decrypt", requestOptions)
    .then(response => response.json())
    .then(result => {
                    document.getElementById("myText").value = result.message
                    console.log(`Your decrypted message is:`)
                    console.log(`${result.message}`)
                    })
    .catch(error => console.log('error', error));}



