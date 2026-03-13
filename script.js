// Smooth scroll navigation
document.querySelectorAll("nav a").forEach(function(link){
    link.addEventListener("click", function(e){

        var target = this.getAttribute("href");

        if(target.startsWith("#")){
            e.preventDefault();

            var section = document.querySelector(target);

            section.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});


// Button click alert
var buttons = document.querySelectorAll("button");

buttons.forEach(function(btn){

    btn.addEventListener("click", function(){

        var carName = this.parentElement.querySelector("h3").innerText;

        alert("Booking request sent for " + carName);

    });

});


// Number counting animation
var numbers = document.querySelectorAll(".brand-box strong, .brand-box b");

numbers.forEach(function(num){

    var target = parseInt(num.innerText);
    var count = 0;

    var interval = setInterval(function(){

        count++;
        num.innerText = count;

        if(count >= target){
            clearInterval(interval);
        }

    }, 100);

});