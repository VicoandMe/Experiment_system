function AjaxHandler(method, url, callback, content, vargs) {
	var xmlhttp;
	if (window.XMLHttpRequest) {
	  xmlhttp = new XMLHttpRequest();
	} else {
	  xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange = function() {
	  if (xmlhttp.readyState == 4) {
	    if (xmlhttp.status == 200) {
		  rtext = xmlhttp.responseText.split("======")[0];
		  rtext = JSON.parse(rtext);
		  console.log(rtext['data']);
		  callback(rtext['data'], vargs);
		} else {
		  callback({'status':'0'}, vargs);
		}
	  }
	}
	if (method == "GET" || method == "POST") {
	  xmlhttp.open(method, url, true);
	  if (content != undefined) {
	    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		contstring = JSON.stringify(content);
		xmlhttp.send(contstring);
	  } else {
	    xmlhttp.send();
	  }
	}
}
