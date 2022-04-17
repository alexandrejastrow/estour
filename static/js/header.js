const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const main = document.querySelector('.main-content');

const SIZE_TO_CHANGE_MARGIN_TOP = '282px';

function changeMarginTop(value) {

    if (main.style.marginTop === '') {
        main.style.marginTop = value
    } else {
        main.style.marginTop = ""
    }
}
hamburger.addEventListener('click', () => {


    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');

    changeMarginTop(SIZE_TO_CHANGE_MARGIN_TOP)

});

document.addEventListener('scroll', function (e) {

    if (hamburger.classList.contains('active')) {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
        let windowWidth = window.innerWidth;
        if (windowWidth < 1197) {
            changeMarginTop(SIZE_TO_CHANGE_MARGIN_TOP)
        }
    }
})

window.addEventListener('resize', () => {
    let windowWidth = window.innerWidth;
    if (windowWidth > 1197) {
        changeMarginTop("0")
    }
    if (hamburger.classList.contains('active') && windowWidth > 1197) {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }
});

function search_function() {
    const searchInput = document.querySelector('.search-input');

    return searchInput;
}