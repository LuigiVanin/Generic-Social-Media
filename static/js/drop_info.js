let btn = document.querySelector(".info-box span");
let icon = document.querySelector(".info-box span i");

btn.addEventListener("click", () => {
    let info = document.querySelector(".info-box");

    if (info.classList.length == 2) {
        info.classList.add("hidden");
        icon.style.setProperty("transform", "rotate(180deg)");
    } else {
        info.classList.remove("hidden");
        icon.style.setProperty("transform", "rotate(0deg)");
    }
});
