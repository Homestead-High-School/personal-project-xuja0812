requirejs.config({
  //By default load any module IDs from js/lib
  baseUrl: 'js/lib',
  //except, if the module ID starts with "app",
  //load it from the js/app directory. paths
  //config is relative to the baseUrl, and
  //never includes a ".js" extension since
  //the paths config could be for a directory.
  paths: {
      app: '../app'
  }
});
function submit(){
  let emailElement = document.getElementById('email');
  let email = emailElement.value;
  let passwordElement = document.getElementById('password');
  let password = passwordElement.value;
  requirejs(['app/main']);
}

function myFunction(){
  var x = document.getElementById("top-nav");
  if(x.className === "nav-bar"){
      x.className += " responsive";
  }
  else{
      x.className = "nav-bar";
  }
}

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
acc[i].addEventListener("click", function() {
  /* Toggle between adding and removing the "active" class,
  to highlight the button that controls the panel */
  this.classList.toggle("active");

  /* Toggle between hiding and showing the active panel */
  var panel = this.nextElementSibling;
  if (panel.style.display === "block") {
    panel.style.display = "none";
  } else {
    panel.style.display = "block";
  }
});
}

function runPyScript(input){
  var jqXHR = $.ajax({
      type: "POST",
      url: "/login",
      async: false,
      data: { mydata: input }
  });

  return jqXHR.responseText;
}

$('#submitbutton').click(function(){
  datatosend = 'this is my matrix';
  result = runPyScript(datatosend);
  console.log('Got back ' + result);
});