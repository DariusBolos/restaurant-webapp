const buttons = document.querySelectorAll(".load-button");
const pages = ["order", "menu", "customers"];

const homeButtonContainer = document.querySelector('.menu-container');
homeButtonContainer.addEventListener("click", (e) => {
        const pageIndex = pages.indexOf(e.target.classList[1])
        const path = window.location.href + pages[pageIndex];
        window.location.replace(path);
});