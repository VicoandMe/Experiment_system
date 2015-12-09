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

function updateMessage(items) {
  if (items["is_End"] == "0") {
    document.getElementById('image').setAttribute('src', './static/img/' + items["image"] + '.png');
    document.getElementById('Question').innerHTML = items["Question"];
    document.getElementById('PselectA').innerHTML = items["SelectA"];
    document.getElementById('PselectB').innerHTML = items["SelectB"];
    document.getElementById('PselectC').innerHTML = items["SelectC"];
    document.getElementById('PselectD').innerHTML = items["SelectD"];
  } else {
    alert("实验结束，感谢您的参与～");
	var div = document.getElementById("Experiment");
	removeElement(div);
  }
}

function AcquireMessage() {
  AjaxHandler("POST", "/post/AcquireMessage", updateMessage, {});
}

function nvoid(items) {
  if (items["statue"] != "200") {
    alert("Experiment failed");
  }
}

function NextQuestion() {
  var form = document.getElementsByTagName("form")[0];
  var input = form.getElementsByTagName("input");
  var value = "A";
  var is_checked = 0;
  for (i = 0; i < 4; i++) {
    if (input[i].checked == true) {
	  value = input[i].value;
	  is_checked = 1;
	  input[i].checked = false;
	}
  }
  if (1 == is_checked) {
    AjaxHandler("POST", "/post/Answer", nvoid, {"value": value});
    AcquireMessage();
  } else {
    alert("选项不能为空");
  }
}

function removeElement(element) {
  var parentElement = element.parentNode;
  if (parentElement) {
    parentElement.removeChild(element);
  }
}

function setInputAttribute(item) {
  item.setAttribute("type", "radio");
  item.style.float = "left";
  item.style.marginRight = "5px";
}

function createSelection() {
  var form = document.createElement("form");
  var selectA = document.createElement("input");
  setInputAttribute(selectA);
  selectA.setAttribute("name", "select");
  selectA.setAttribute("id", "selectA");
  selectA.setAttribute("value", "A")
  var PselectA = document.createElement("p");
  PselectA.innerHTML = "test";
  PselectA.setAttribute("id", "PselectA");
  var selectB = document.createElement("input");
  setInputAttribute(selectB);
  selectB.setAttribute("name", "select");
  selectB.setAttribute("id", "selectB");
  selectB.setAttribute("value", "B");
  var PselectB = document.createElement("p");
  PselectB.innerHTML = "test";
  PselectB.setAttribute("id", "PselectB");
  var selectC = document.createElement("input");
  setInputAttribute(selectC);
  selectC.setAttribute("name", "select");
  selectC.setAttribute("id", "selectC");
  selectC.setAttribute("value", "C");
  var PselectC = document.createElement("p");
  PselectC.innerHTML = "test";
  PselectC.setAttribute("id", "PselectC");
  var selectD = document.createElement("input");
  setInputAttribute(selectD);
  selectD.setAttribute("name", "select");
  selectD.setAttribute("id", "selectD");
  selectD.setAttribute("value", "D");
  var PselectD = document.createElement("p");
  PselectD.innerHTML = "test";
  PselectD.setAttribute("id", "PselectD");
  PselectA.style.float = "left";
  PselectB.style.float = "left";
  PselectC.style.float = "left";
  PselectD.style.float = "left";
  form.appendChild(selectA);
  form.appendChild(PselectA);
  form.appendChild(document.createElement("br"));
  form.appendChild(document.createElement("br"));
  form.appendChild(selectB);
  form.appendChild(PselectB);
  form.appendChild(document.createElement("br"));
  form.appendChild(document.createElement("br"));
  form.appendChild(selectC);
  form.appendChild(PselectC);
  form.appendChild(document.createElement("br"));
  form.appendChild(document.createElement("br"));
  form.appendChild(selectD);
  form.appendChild(PselectD);
  form.appendChild(document.createElement("br"));
  return form;
}


function startExperiment() {
  var title = document.getElementById('title');
  removeElement(title);
  var container = document.getElementById('container');
  removeElement(container);
  var Experiment = document.getElementById('Experiment');
  Experiment.style.height = "70%";
  Experiment.style.paddingTop = "55px";
  var imageDiv = document.createElement("div");
  imageDiv.setAttribute("id", "ImageDiv");
  imageDiv.style.width = "80%";
  imageDiv.style.float = "left";
  var QuestionAndSelectDiv = document.createElement("div");
  QuestionAndSelectDiv.setAttribute("id", "QuestionAndSelectDiv");
  QuestionAndSelectDiv.style.width = "20%";
  QuestionAndSelectDiv.style.float = "left";
  QuestionAndSelectDiv.style.marginTop = "20%";
  var Question = document.createElement("h3");
  Question.setAttribute("id", "Question");
  Question.style.width = "100%";
  Question.style.paddingTop = "20px";
  Question.style.paddingRight = "20px";
  QuestionAndSelectDiv.appendChild(Question);
  QuestionAndSelectDiv.appendChild(document.createElement("br"));
  var selectDiv = document.createElement("div");
  selectDiv.style.width = "100%";
  var form = createSelection();
  selectDiv.appendChild(form);
  QuestionAndSelectDiv.appendChild(selectDiv);
  QuestionAndSelectDiv.appendChild(document.createElement("br"));
  var NextButton = document.createElement("button");
  NextButton.innerHTML = "下一题";
  NextButton.onclick = eval("(function() { NextQuestion(); })");
  NextButton.setAttribute("class", "button gray round");
  NextButton.style.marginTop = "25px";
  NextButton.style.marginLeft = "20px";
  NextButton.style.float = "left";
  var buttonDiv = document.createElement("div");
  buttonDiv.style.width = "100%";
  buttonDiv.appendChild(NextButton);
  QuestionAndSelectDiv.appendChild(buttonDiv);

  var image = document.createElement("img");
  image.setAttribute("id", "image");
  image.setAttribute("src", "");
  image.style.width = "90%";
  image.style.padding = "auto";
  image.style.marginLeft = "20px";
  imageDiv.appendChild(image);
  Experiment.appendChild(imageDiv);
  Experiment.appendChild(QuestionAndSelectDiv);
  AcquireMessage();
}


