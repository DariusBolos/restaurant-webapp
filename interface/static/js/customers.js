const itemButton = document.querySelector(".item-button")
const displayCustomersButton = document.querySelector(".display-button")
const popup = document.querySelector("#popup")

function displayPopup(){
    popup.classList.add("open-popup")
}

function loadMenu(){
    const path = window.location.href + "users"
    window.location.replace(path)
}

itemButton.addEventListener("click", () => displayPopup())
displayCustomersButton.addEventListener("click", () => loadMenu())