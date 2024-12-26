const itemButton = document.querySelector(".item-button");
const menuOptionButtons = document.querySelectorAll(".js-menuRadioButton");
const displayMenuButton = document.querySelector(".display-button");
const popup = document.querySelector(".js-popup");

function displayPopup(){
    popup.classList.add("open-popup");
}


function loadMenu(){
    const path = `${window.location.href}catalogue`;
    window.location.replace(path);
}

itemButton.addEventListener("click", () => displayPopup());
displayMenuButton.addEventListener("click", () => loadMenu());

function removeField(){
    const specificPropertyField = document.querySelector(".option-field");

    if (specificPropertyField) {
        specificPropertyField.remove();
    }
}

function createField(type){
    const parent = document.querySelector(".radio-container");
    const textField = document.createElement("INPUT");
    const placeholder = {
        dish: "Estimated preparation time",
        drink: "Alcohol Percentage",
    };

    textField.classList.add("option-field");
    textField.type = "number";
    textField.name = "item-info";
    textField.placeholder = placeholder[type];
    parent.appendChild(textField);
}

menuOptionButtons.forEach((radioButton, index) => {
    const menuOptions = ["dish", "drink"]
    radioButton.addEventListener("click", (e) => {
        removeField();
        createField(menuOptions[index]);
    });
});