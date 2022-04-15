const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

function search_function() {
    const searchInput = document.querySelector('.search-input');
    console.log(searchInput.value);
    return searchInput;
}