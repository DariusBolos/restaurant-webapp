const wrapper = document.querySelector(".customer-container"),
    selectButton = document.querySelector(".select-button"),
    displayedCustomers = document.querySelectorAll("li"),
    searchbar = document.querySelector(".searchbar"),
    searchedUsers = document.querySelector(".user-container ");
let listValues = []


displayedCustomers.forEach(element => listValues.push(element.innerText))

selectButton.addEventListener("click", () => {
    wrapper.classList.toggle("active");
})

function updateText(listElement) {
    searchbar.value = "";
    selectButton.firstElementChild.innerText = listElement.innerText;
    wrapper.classList.remove("active");
}

function displaySelectedElement(element) {
    element.addEventListener("click", (e) => {
        updateText(element);
        console.log(e.target);
    });
}

displayedCustomers.forEach(element => displaySelectedElement(element));

function searchByInput() {
    let namesToDisplay = [];
    let searchedValue = searchbar.value.toLowerCase();
    namesToDisplay = listValues.filter(data => {
        return data.toLowerCase().startsWith(searchedValue);
    }).map(data => `<li>${data}</li>`).join("");
    searchedUsers.innerHTML = namesToDisplay ? namesToDisplay : `<p>Customer not found</p>`;
    const newListElements = document.querySelectorAll("li");
    newListElements.forEach(element => displaySelectedElement(element));
}

searchbar.addEventListener("keyup", () => searchByInput());