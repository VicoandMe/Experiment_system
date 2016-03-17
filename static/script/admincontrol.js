window.onload = display;

function display() {
  var contain = document.getElementById("container");
  contain.style.display = "none";
  var containQ = document.getElementById("containerQ");
  containQ.style.display = "none";
}
function uploadCallBack2(items) {
	if (items['status'] == "500") {
	  alert("服务器错误");
  } else if (items['is_End'] == "1") {
	  alert("已是最后一题");
	} else {
	  document.getElementById("QuestionId").innerHTML = "问题编号:" + items['questionId'];
	}
}

function uploadCallBack(items) {
	if (items['status'] == "500") {
	  alert("服务器错误");
  } else if (items['is_End'] == "1") {
	  alert("已是最后一题，上传完毕");
	} else {
	  document.getElementById("QuestionId").innerHTML = "问题编号:" + items['questionId'];
	  document.getElementById("Question").value = "";
	  document.getElementById("answerA").value = "";
    document.getElementById("answerB").value = "";
    document.getElementById("answerC").value = "";
    document.getElementById("answerD").value = "";
    document.getElementById("correctAnswer").value = "";
  
	}
}

function lastQuestion() {
   var questionId = document.getElementById("QuestionId").innerHTML;
   AjaxHandler("POST", "/post/lnQuestion", uploadCallBack2,{"command" : "last", "questionId": questionId})
}

function nextQuestion() {
   var questionId = document.getElementById("QuestionId").innerHTML;
   AjaxHandler("POST", "/post/lnQuestion", uploadCallBack2,{"command" : "next", "questionId": questionId})
}

function uploadQuestions() {
  var questionId = document.getElementById("QuestionId").innerHTML;
	var question = document.getElementById("Question").value;
	var answerA = document.getElementById("answerA").value;
  var answerB = document.getElementById("answerB").value;
  var answerC = document.getElementById("answerC").value;
  var answerD = document.getElementById("answerD").value;
  var correctAnswer = document.getElementById("correctAnswer").value;
  var msg = {"questionId":questionId,
	"question":question,
	"answerA":answerA,
	"answerB":answerB,
	"answerC":answerC,
	"answerD":answerD,
	"correctAnswer":correctAnswer};
	console.log(msg);
  AjaxHandler("POST", "/post/UploadQuestions", uploadCallBack, msg);
}

function showUploadQuestions(items) {
  var contain = document.getElementById("container");
  contain.style.display = "none";
  var containQ = document.getElementById("containerQ");
  containQ.style.display = "block";
	var form = document.getElementById("questionForm");
	form.style.display = "";
}

function updateSettings() {
  var imageCount = document.getElementById("imageCount");
  var imageCountEach = document.getElementById("imageCountEach");
  var questionCount = document.getElementById("questionCount");
  var sevenPointQuestion = document.getElementById("sevenPointQuestion");
	var imageURL = document.getElementById("imageURL");
	var msg = {"imageCount":imageCount.value,
	"imageCountEach":imageCountEach.value,
	"questionCount":questionCount.value,
	"sevenPointQuestion":sevenPointQuestion.value,
	"imageURL":imageURL.value};
	AjaxHandler("POST", "/post/UpdateSettings", showUploadQuestions, msg);
}

function adminInterface(items) {
	if (items['status'] == "500") {
	  alert("用户不存在或密码错误");
		window.location.reload();
	} else if (items['status'] == "200") {
    document.getElementById("welcome").hidden = true;
    var contain = document.getElementById("container");
    contain.style.display = "block";
		var form = document.getElementById("form");
		var b = document.getElementById("login-button");
		b.disabled = true;
		form.style.display = "";
	}
}

function adminLogin() {
  var user = document.getElementById("username").value;
	var password = document.getElementById("password").value;

	AjaxHandler("POST", "/post/Admin", adminInterface, {"user":user, "password":password});
}
