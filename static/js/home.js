const hearts = document.querySelectorAll('.svg-heart')
let user_on = false
let my_place_cookies = {}


function favorite_action(url) {

    const xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send(null)
    return xhr.responseText
}


function favorite(e) {
    if (user_on) {
        let ids = e.target.parentNode.id.split(';')
        let response = favorite_action(`/places/favorite/${ids[0]}/${ids[1]}`)
        if (response == 'add') {
            e.target.classList.add('active')
        } else {
            e.target.classList.remove('active')
        }
    } else {
        alert('Você precisa estar logado para favoritar um lugar')
    }
}




let ids = hearts[0].id.split(';')
if (ids[0] === "None") {
    user_on = false
} else {
    user_on = true
}

hearts.forEach(heart => {
    heart.addEventListener('click', favorite)
    if (user_on) {

        let ids = heart.id.split(';')
        let response = favorite_action(`/places/favorite/get/${ids[0]}/${ids[1]}`)

        if (response === 'true') {
            heart.childNodes[1].classList.add('active')
        } else {
            heart.childNodes[1].classList.remove('active')
        }
    }
})