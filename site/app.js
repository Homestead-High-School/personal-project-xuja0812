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

function display(){

  // FIRST CALL THE NEW_MODEL PYTHON FILE
  const fileUrl = 'FINAL_DATA.txt';
  fetch(fileUrl).then(r => r.text()).then((t) => {
    // GENERATE HTML ELEMENTS
    const arr = t.split("\n");
    let n = arr.length;
    for(let j = 0; j<n; j++){
      let text = arr[j];
      let rec = "";
      let review = text.split(/[" "]+/);
      let index = 0;
      while(review[index] != 'recommend' && review[index] != 'recommends'){
        rec += review[index] + " ";
        index++;
      }
      rec += review[index];
      let name = review[index + 1];
      let rev = "";
      for(let i = index + 2; i<review.length-1; i++){
        rev += review[i] + " ";
      }
      let rating = review[review.length-1];
      let all = document.createElement("div");
      all.className = "full-review";
      let name_e = document.createElement("div");
      name_e.innerText = name;
      name_e.className = "name";
      let rec_e = document.createElement("div");
      rec_e.innerText = rec;
      rec_e.className = "rec";
      let rev_e = document.createElement("div");
      rev_e.innerText = rev;
      rev_e.className = "rev";
      let rating_e = document.createElement("div");
      rating_e.innerText = rating;
      rating_e.className = "rating";
      all.appendChild(name_e);
      all.appendChild(rec_e);
      all.appendChild(rev_e);
      all.appendChild(rating_e);
      let element = document.getElementById("list");
      element.appendChild(all);
    }
  });
}

function display2(t){
  const arr = t.split("\n");
    let n = arr.length;
    for(let j = 0; j<n; j++){
      let text = arr[j];
      let rec = "";
      let review = text.split(/[" "]+/);
      let index = 0;
      while(review[index] != 'recommend' && review[index] != 'recommends'){
        rec += review[index] + " ";
        index++;
      }
      rec += review[index];
      let name = review[index + 1];
      let rev = "";
      for(let i = index + 2; i<review.length-1; i++){
        rev += review[i] + " ";
      }
      let rating = review[review.length-1];
      let all = document.createElement("div");
      all.className = "full-review";
      let name_e = document.createElement("div");
      name_e.innerText = name;
      name_e.className = "name";
      let rec_e = document.createElement("div");
      rec_e.innerText = rec;
      rec_e.className = "rec";
      let rev_e = document.createElement("div");
      rev_e.innerText = rev;
      rev_e.className = "rev";
      let rating_e = document.createElement("div");
      rating_e.innerText = rating;
      rating_e.className = "rating";
      all.appendChild(name_e);
      all.appendChild(rec_e);
      all.appendChild(rev_e);
      all.appendChild(rating_e);
      let element = document.getElementById("list");
      element.appendChild(all);
    }
}

function process(text){
  console.log(text);
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

