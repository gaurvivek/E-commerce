var title;
chrome.runtime.onMessage.addListener(function(message,sender,sendResponse){
  if(message.method == 'setTitle')
  {
    title = message.title;
  }
  else if(message.method == 'getTitle')
   {
    sendResponse(title);
   }
   else
   {}
});
