let btn_updt = document.querySelector(".refresh");
let cover = document.querySelector(".cover");
let close_btn = document.querySelector(".cover i.fa-times");

btn_updt.addEventListener("click", () => {
    cover.classList.replace("hidden", "show");
});

close_btn.addEventListener("click", () => {
    cover.classList.replace("show", "hidden");
});
