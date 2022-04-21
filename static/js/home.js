const values = document.cookie.split(';')
const hearts = document.querySelectorAll('.svg-heart')


function favorite_action(url) {

    const xhr = new XMLHttpRequest();

    xhr.open('GET', url, false);
    xhr.send(null)
    return xhr.responseText
}


function setCookies(key, value) {
    text = key + '=' + value
    document.cookie = text
}

function saveCookiePlace(data) {

    text = ""
    count = 0
    for (let key in data) {
        count++
    }
    for (let key in data) {
        if (count > 1) {
            text += key.replace(";", "_") + '>' + data[key] + '**'
        } else {
            text += key.replace(";", "_") + '>' + data[key]
        }
        count--
    }
    document.cookie = 'places=' + text
}
function desmemberCookiePlaces() {

    let listCookies = document.cookie.split(';')
    data = {}
    for (let i = 0; i < listCookies.length; i++) {
        let cookie = listCookies[i].split('=')
        data[cookie[0]] = cookie[1]
    }

    let values = {
        'places': data[' places'].split('**')
    }
    data = {}
    for (let i = 0; i < values.places.length; i++) {
        keyValue = values.places[i].split('>')
        data[keyValue[0].replace("_", ";")] = keyValue[1]

    }
    return data
}
let user_on = false

hearts.forEach(heart => {
    heart.addEventListener('click', favorite)
    let ids = heart.id.split(';')
    if (ids[0] === "None") {
    } else {
        user_on = true
    }
})


if (document.cookie.search('places=') === -1 && user_on) {
    let places = ""
    let count = 0;
    hearts.forEach(heart => {


        let ids = heart.id.split(';')
        let response = favorite_action('/places/favorite/get/' + ids[0] + '/' + ids[1])
        heart.childNodes[1].classList.add('active')

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

        count++;
    })

    setCookies("places", places)

} else if (document.cookie.search('places=') !== -1 && user_on) {

    let my_cookies = desmemberCookiePlaces()
    hearts.forEach(heart => {

        let ids = heart.id.split(';')
        if (my_cookies[heart.id]) {
            if (my_cookies[heart.id] === 'true') {
                heart.childNodes[1].classList.add('active')
            }
        } else {
            let response = favorite_action('/places/favorite/get/' + ids[0] + '/' + ids[1])
            if (response === 'true') {
                heart.childNodes[1].classList.add('active')
            } else {
                heart.childNodes[1].classList.remove('active')
            }

            my_cookies[ids[0] + ";" + ids[1]] = response
        }
    })
    saveCookiePlace(my_cookies)
}


function favorite(e) {

    if (user_on) {
        let ids = e.target.parentNode.id.split(';')
        let response = favorite_action('/places/favorite/' + ids[0] + '/' + ids[1])

        if (response === 'true') {
            e.target.classList.add('active')
        } else {
            e.target.classList.remove('active')
        }
    } else {
        alert('Você precisa estar logado para favoritar um lugar')
    }
}
