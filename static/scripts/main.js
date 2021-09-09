/*  side menu */
var side_menu = document.getElementById("side-menu")
var width = 0

function open_sideMenu(){

    if (width == 0){
        side_menu.style.width = "300px";
        width = 200;
    }
    else{
        side_menu.style.width = "0px"
        width = 0;
    }
}

alert("WELCOME TO OUR WEBAPP... THIS IS STILL A BETA VERSION, HOWEVER, WILL BE UPDATED VERY SOON...")