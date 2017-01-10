alert("Click The extension icon to get the rating");
var url = window.location.href;
chrome.runtime.sendMessage({method:'setTitle',title:url});
