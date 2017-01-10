var x = document.getElementsByClassName("review-text");
var i=0;
var comment=[];
if(x==null)
	alert("No reviews");
while(i<x.length)
{
	comment[i]=x[i].innerHTML.toString();
	i=i+1;
}
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    var scriptOptions = message.title;
    if(scriptOptions=='gettitle')
    {
    	sendResponse(comment);
    }
});comment
