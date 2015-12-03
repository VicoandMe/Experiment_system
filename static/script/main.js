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

function AcquireMessage(items) {
  alert("kao");
}

function removeElement(element) {
  var parentElement = element.parentNode;
  if (parentElement) {
    parentElement.removeChild(element);
  }
}

function startExperiment() {
  var title = document.getElementById('title');
  removeElement(title);
  var container = document.getElementById('container');
  removeElement(container);
  var Experiment = document.getElementById('Experiment');
  Experiment.style.height = "70%";
  Experiment.style.paddingTop = "50px";
  var imageDiv = document.createElement("div");
  imageDiv.setAttribute("id", "ImageDiv");
  imageDiv.style.width = "60%";
  imageDiv.style.float = "left";
  var QuestionAndSelectDiv = document.createElement("div");
  QuestionAndSelectDiv.setAttribute("id", "QuestionAndSelectDiv");
  QuestionAndSelectDiv.style.width = "40%";
  QuestionAndSelectDiv.style.float = "left";
  var image = document.createElement("img");
  image.setAttribute("src", "/static/img/main.jpg");
  imageDiv.appendChild(image);
  Experiment.appendChild(imageDiv);
  Experiment.appendChild(QuestionAndSelectDiv);
}


