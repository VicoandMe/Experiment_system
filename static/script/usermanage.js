function createLayout() {
  var layout = document.createElement("div");
  layout.setAttribute("id", "layout");
  layout.onclick = eval("(function() { clearArea(); })");
  return layout
}

function clearArea() {
  if (document.getElementsByClassName('org_box').length != 0)
	  document.getElementsByClassName('org_box')[0].remove();
  if (document.getElementById('layout') != null)
	  document.getElementById('layout').remove();
}

function createInput(name, type, value) {
  var view = document.createElement("input");
  view.setAttribute("type", type);
  view.setAttribute("name", name);
  view.setAttribute("value", value);
  view.setAttribute("default", value);

  view.onfocus = eval("(function() { if(this.value == '"+value+"') this.value = ''; })");
  view.onblur = eval("(function() { if(this.value == '') this.value = '"+value+"'; })");
  return view
}

function updateUserArea(items) {
  if (items["statue"] == "200") {
	document.getElementById('UserArea').innerHTML = items["student_ID"];
	var title = document.getElementById('title');
	title.style.height = "25%";
	var container = document.getElementById('container');
	var pro = document.createElement("h3");
	pro.innerHTML = "实验注意事项";
	pro.style.paddingTop = "20px";
	var details = document.createElement("p");
	details.innerHTML = "(1) 请认真阅读图表 <br> (2) 请选定答案后再点击下一题，不可空缺";
	container.appendChild(pro);
	container.appendChild(details);
	var startButton = document.createElement("button");
	startButton.style.marginTop = "20px";
	startButton.innerHTML = "start Experiment";
	startButton.onclick = eval("(function(){ startExperiment(); })");
	startButton.setAttribute("class", "button gray round");
	container.appendChild(startButton);
	container.style.width = "30%";
	container.style.margin = "auto";
  } else {
    alert("请使用未注册的Student ID");
  }
}

function Register() {
  var box = document.getElementsByClassName("org_box")[0];
  var inputs = box.getElementsByTagName("input");
  AjaxHandler("POST", "/post/Regist", updateUserArea, {"Name":inputs[0].value, "Student_ID":inputs[1].value});
  removeElement(box);
}


function RegisterArea() {
  var body = document.getElementsByTagName("body")[0];
  clearArea();
  body.appendChild(createLayout());
  var orgbox = document.createElement("div");
  orgbox.setAttribute("class", "org_box");
  var orgboxcor = document.createElement("span");
  orgboxcor.setAttribute("class", "org_box_cor");
  orgbox.appendChild(orgboxcor);
  orgbox.appendChild(createInput("Name", "text", "Your Name"));
  orgbox.appendChild(createInput("Student_Id", "text", "Your student ID"));
  var RegisterButton = document.createElement("button");
  RegisterButton.innerHTML = "Regist";
  RegisterButton.onclick = eval("(function(){ Register(); })");
  orgbox.appendChild(RegisterButton);
  body.appendChild(orgbox);
}
