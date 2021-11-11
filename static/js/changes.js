var form = document.querySelector(".box");
var loginForm = document.querySelector("#login");
var registerForm = document.querySelector("#register");
var btn = document.querySelector("#box__btn");
var w = form.offsetWidth;

function login() {
    registerForm.classList.replace("main", "off");
    loginForm.classList.replace("off", "main");
    btn.classList.replace("register", "log-in");

    form.style.setProperty("overflow-y", "hidden");
    form.style.setProperty("overflow-x", "hidden");
}

function register() {
    loginForm.classList.replace("main", "off");
    registerForm.classList.replace("off", "main");
    btn.classList.replace("log-in", "register");

    form.style.setProperty("overflow-y", "scroll");
    form.style.setProperty("overflow-x", "hidden");
}
