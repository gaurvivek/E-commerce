var comments_str=[];
var response=[];
var productname=[];
var url;
//chrome.tabs.executeScript(null,{code:"var comeent_str="+comment_str})
chrome.tabs.executeScript(null,{file:'script.js'},function(result){
		comments_str=result[0];
});
function fetch_comments()
{
	chrome.runtime.sendMessage({method:'getTitle'}, function(response){
		var productname=response.split( '/' );
		//alert(response);
		//alert(productname[3]);
		//alert(productname[5]);
		//var patharray=productname[5];
		//var productid=patharray.split( '?' );
		//var pidname=productid[1];
		//var pidarray=pidname.split('=');
		//var finalarray=pidarray[1];
		//var final=finalarray.split('&');
		//url="http://www.flipkart.com/"+productname[3]+"/product-reviews/"+productid[0].toUpperCase()+"?pid="+final[0]+"&type=all";
		//alert(url);
		//chrome.tabs.create({url:url});
	});
	//var productarray=productname[5];
	
	
}
function xml_http_post(url, data, callback) {
    var req = false;
    try {
        // Firefox, Opera 8.0+, Safari
        req = new XMLHttpRequest();
    }
    catch (e) {
        // Internet Explorer
        try {
            req = new ActiveXObject("Msxml2.XMLHTTP");
        }
        catch (e) {
            try {
                req = new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch (e) {
                alert("Your browser does not support AJAX!");
                return false;
            }
        }
    }
    req.open("POST", url, true);
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            callback(req);
        }
    }
    req.send(data);
}


function test_button() {
    var data =document.getElementsByClassName("review-text");       
    xml_http_post("http://localhost:8080/", comments_str, test_handle);
}

function test_handle(req) {
    var overall = document.getElementById('overall');
    var price = document.getElementById('price');
    var battery = document.getElementById('Battery');
    var performance = document.getElementById('Performance');
    var processor = document.getElementById('Processor');
    var design = document.getElementById('Design');
    var weight = document.getElementById('Weight');
    var vibration = document.getElementById('Vibration');
    var cleaning = document.getElementById('Cleaning');
    var display = document.getElementById('Display');
    var camera = document.getElementById('Camera');
    var sound = document.getElementById('Sound');
    var res= req.responseText.split(",");
    var i=0;
    var res_str=[]
    //pname.innerHTML="<h2>"+productname[3].toUpperCase()+"</h2>";
    for(i=0;i<res.length;i++)
    {
    	if(res[i]=='0')
    	{
    		res_str[i]=' ';
    	}
    	else
    		res_str[i]=res[i];
    }
    var i=0
    if(res_str[0]==' ')
    	overall.innerHTML="Overall:-";
    else
    	overall.innerHTML="<h2>Overall:"+res_str[0]+"</h2>";
    if(res_str[1]==' ')
    	price.innerHTML="<h3>Price:-</h3>";
    else
    	price.innerHTML="<h3>Price:"+res_str[1]+"</h3>";
    if(res_str[2]==' ')
    	battery.innerHTML="<h3>Battery:-</h3>";
    else
    	battery.innerHTML="<h3>Battery:"+res_str[2]+"</h3>";
    if(res_str[3]==' ')
    {
    	performance.innerHTML=" ";
    }
    else
    	performance.innerHTML="<h3>Performance:"+res_str[3]+"</h3>";
    if(res_str[4]==' ')
    	processor.innerHTML="<h3>Processor:-</h3>";
    else
    	processor.innerHTML="<h3>Processor:"+res_str[4]+"</h3>";
    if(res_str[5]==' ')
    	design.innerHTML="<h3>Design:-</h3>";
    else
    	design.innerHTML="<h3>Design:"+res_str[5]+"</h3>";
    if(res_str[6]==' ')
    	weight.innerHTML="<h3>Weight:-</h3>";
    else
    	weight.innerHTML="<h3>Weight:"+res_str[6]+"</h3>";
    if(res_str[7].match(/^[^0]+/))
    {
    	vibration.innerHTML="";
    }
    else
    	vibration.innerHTML="<h3>Vibration:"+res_str[7]+"<h3>";
    if(res_str[8]==' ')
    	cleaning.innerHTML="<h3>Cleaning:-</h3>";
    else
    	cleaning.innerHTML="<h3>Cleaning:"+res_str[8]+"</h3>";
    if(res_str[9]==' ')
    	display.innerHTML="<h3>Display:-</h3>";
    else
    	display.innerHTML="<h3>Display:"+res_str[9]+"</h3>";
    if(res_str[10]==' ')
    	camera.innerHTML="<h3>Camera:-</h3>";
    else
    	camera.innerHTML="<h3>Camera:"+res_str[10]+"</h3>";
    if(res_str[11]==' ')
    	sound.innerHTML="<h3>Sound:-</h3>";
    else
    	sound.innerHTML="<h3>Sound:"+res_str[11]+"</h3>";
    
}
document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('link');
    // onClick's logic below:
    link.addEventListener('click', function() {
	fetch_comments();
	test_button();        
    });
});
	


