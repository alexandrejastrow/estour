const hearts = document.querySelectorAll('.svg-heart')
let user_on = false
let my_place_cookies = {}


function favorite_action(url) {

    const xhr = new XMLHttpRequest();

    xhr.open('GET', url, false);
    xhr.send(null)
    return xhr.responseText
}


function remove_place_cookie() {
    document.cookie = 'places' + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    my_place_cookies = {}
}

function load_all_places() {
    let places = ""
    let count = 0;
    hearts.forEach(heart => {
        let ids = heart.id.split(';')
        let response = favorite_action('/places/favorite/get/' + ids[0] + '/' + ids[1])
        if (response === 'true') {
            heart.childNodes[1].classList.add('active')
        } else {
            heart.childNodes[1].classList.remove('active')
        }

        if (count < hearts.length - 1) {
            places += ids[0] + "_" + ids[1] + '>' + response + '**'
        } else {
            places += ids[0] + "_" + ids[1] + '>' + response
        }
        my_place_cookies[ids[0] + ";" + ids[1]] = response
        count++;
    })
    return places;
}
function load_place_cookie() {
    let listCookies = document.cookie.split(';')

    if (document.cookie.includes('places')) {
        for (let i = 0; i < listCookies.length; i++) {
            let cookie = listCookies[i].split('=')
            if (cookie[0].trim() === 'places') {
                let places = cookie[1].split('**')
                for (let i = 0; i < places.length; i++) {
                    let keyValue = places[i].split('>')
                    my_place_cookies[keyValue[0].replace("_", ";")] = keyValue[1]
                }

            }
        }
        set_favorite_places()
    } else {
        let place_cookie_text = load_all_places()
        document.cookie = 'places=' + place_cookie_text
    }
}
function saveCookiePlace() {
    let places = ""
    let count = 0;
    for (let key in my_place_cookies) {
        count++
    }
    for (let key in my_place_cookies) {
        if (count > 1) {
            places += key.replace(";", "_") + '>' + my_place_cookies[key] + '**'
        } else {
            places += key.replace(";", "_") + '>' + my_place_cookies[key]
        }
        count--
    }
    document.cookie = 'places=' + places
}

function favorite(e) {
    if (user_on) {
        if (!my_place_cookies[e.target.parentNode.id]) {
            let ids = e.target.parentNode.id.split(';')
            let response = favorite_action('/places/favorite/' + ids[0] + '/' + ids[1])
            if (response === 'true') {
                e.target.classList.add('active')
            } else {
                e.target.classList.remove('active')
            }
            my_place_cookies[e.target.parentNode.id] = response
            saveCookiePlace()
        } else {

            let ids = e.target.parentNode.id.split(';')
            let response = favorite_action('/places/favorite/' + ids[0] + '/' + ids[1])

            if (response === 'true') {
                e.target.classList.add('active')
            } else {
                e.target.classList.remove('active')
            }
            my_place_cookies[e.target.parentNode.id] = response
            saveCookiePlace()
        }
    } else {
        alert('Você precisa estar logado para favoritar um lugar')
    }
}
function set_favorite_places() {

    hearts.forEach(heart => {
        if (my_place_cookies[heart.id] === 'true') {
            heart.childNodes[1].classList.add('active')
        } else {
            heart.childNodes[1].classList.remove('active')
        }
    })
}


hearts.forEach(heart => {
    heart.addEventListener('click', favorite)
})

let ids = hearts[0].id.split(';')
if (ids[0] === "None") {
    user_on = false
    remove_place_cookie()
} else {
    user_on = true
    load_place_cookie()
}

