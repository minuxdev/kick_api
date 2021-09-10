/*  side menu */
var side_menu = document.getElementById("side-menu")
var width = 0

function open_side_menu(element){

    if (width == 0){
        side_menu.style.width = "250px";
        element.innerHTML = "&#10761;"
        width = 2;
    }
    else{
        side_menu.style.width = "0px"
        element.innerHTML = "&#9776;"
        width = 0;
    }
}


function open_contact_section(){
    var aside = document.getElementById("contact")

    if (aside.style.display == "block"){
        aside.style.display = "none"
    } else {
        aside.style.display = "block"
    }
}

alert("WELCOME TO OUR WEBAPP... THIS IS STILL A BETA VERSION, HOWEVER, WILL BE UPDATED VERY SOON...")