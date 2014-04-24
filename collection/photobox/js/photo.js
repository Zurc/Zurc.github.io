var Users = [
    {
      "user_id": 4,
      "name": "Marta Jasinska",
      "mention_name": "kreska",
      "email": "kreskasbox@gmail.com",
    },
    {
      "user_id": 3,
      "name": "Santa Claus",
      "mention_name": "SC",
      "email": "santa@northpole.com",
    },
    {
      "user_id": 5,
      "name": "Nathan Drake",
      "mention_name": "nate",
      "email": "ndrake@awesome.com",
    },
    {
      "user_id": 1,
      "name": "Scott Pilgrim",
      "mention_name": "scott",
      "email": "soLazy@emailcompany.com",
    },
    {
      "user_id": 2,
      "name": "Snow White",
      "mention_name": "snow",
      "email": "snow@fables.com",
    },
    {
      "user_id": 6,
      "name": "Bruce Campbell",
      "mention_name": "Ash",
      "email": "thatchin@gmail.com",
    },
    {
      "user_id": 7,
      "name": "Veronica Mars",
      "mention_name": "veronica",
      "email": "vmars@marsinvestigations.com",
    },
    {
      "user_id": 8,
      "name": "Albert Einstein",
      "mention_name": "albert",
      "email": "amc@2.com",
    },
    {
      "user_id": 9,
      "name": "Charles Chaplin",
      "mention_name": "charles",
      "email": "modern@times.com",
    }
  ]

$(document).ready(function(){
 
  function SortByUserId(a,b){
    return ((a.user_id == b.user_id) ? 0 : ((a.user_id > b.user_id) ? 1 : -1 ));
    }
    Users.sort(SortByUserId);
  
  for (i=0; i<Users.length; i++){
    
    $("<style type='text/css'> .box+i </style>").appendTo("body");
    $("<div>").addClass('box'+i).html("Name: "+(Users[i].name) + "<br />" + "Mention Name: " + (Users[i].mention_name) + "<br />" + "Email: "+(Users[i].email)).appendTo("body");
    
    var color_1 = '#'+Math.floor(Math.random()*16777215).toString(16);
    $('.box'+i).css("background-color", color_1);
    $('.box'+i).css("color", color_1);
    $('.box'+i).css("width",300);
    $('.box'+i).css("height",300); 
    $('.box'+i).css("float","left");
    $('.box'+i).css("margin",5);
   
    $('.box'+i).mouseover(function(){
    var color_0 = "#fff";
    var color_t = "#000";
    $(this).css("background-color", color_0);
    $(this).css("color", color_t);
    });
    
    $('.box'+i).mouseout(function(){ 
    var color_2 = '#'+Math.floor(Math.random()*16777215).toString(16);   
    $(this).css("background-color", color_2);
    $(this).css("color", color_2);
    });

  }
});