const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const main = document.querySelector('.main-content');

const sizes = {
    "482": '282px',
    "1197": '282px',
};

function changeMarginTop(value) {

    if (main.style.marginTop === '') {
        main.style.marginTop = value
    } else {
        main.style.marginTop = ""
    }
}
hamburger.addEventListener('click', () => {

    let windowWidth = window.innerWidth;

    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');

    if (windowWidth < 1197) {
        changeMarginTop("282px")
    }
});

function search_function() {
    const searchInput = document.querySelector('.search-input');

    return searchInput;
}