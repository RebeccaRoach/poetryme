var colors = ['#d1d1f6','#c4fff9','#f9444d','#e5c1bf','#6568a','#3dccc7'];
 
var poem = '';
var author = '';

function getPoem(){
  

};

function changeColor(){
  var colorNum = Math.floor((Math.random()*colors.length));
  var newColor = colors[colorNum];
   $("#mainBackground").fadeOut(500).css("background-color",newColor).fadeIn(1000);
  $(".round-btn").fadeOut(500).css("background-color",newColor).fadeIn(1000);
  $("#nextPoem").fadeOut(500).css("background-color",'white').fadeIn(1000);
  $("#previousPoem").fadeOut(500).css("background-color",'white').fadeIn(1000);
}

$(document).ready(function(){
  
  $("#nextPoem").on("click", function(){
    $("#currentPoem").html("new poem ");
    $("#author").html("new author");
   
    
    changeColor();
     
    //$("#mainBackground").fadeToggle(2500);
  
  //TO-DO: connect to http://poetrydb.org/index.html
  // and use their api to fetch poems
    
  })
})

