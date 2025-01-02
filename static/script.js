
const genresList = ['Drama',
    'Crime',
    'History',
    'War',
    'Comedy',
    'Romance',
    'Animation',
    'Family',
    'Fantasy',
    'Thriller',
    'Action',
    'Adventure',
    'Western',
    'Horror',
    'Science Fiction',
    'Music',
    'Mystery',
    'Documentary',
    'TV Movie']

const langList = ['en', 'hi', 'ja', 'ko', 'it', 'fr', 'ru', 'de', 'es', 'cn', 'ml']
const fullList = ["English", "Indian", "Japanese", "Korean", "Italian",
    "French", "Russian", "Germany", "Spanish", "Chinese", "Malaysian"
]

const periodList = ["2010~Current", "1970-2010", "1970 or older"]

function createGenres(values) {
    const genreContainer = document.querySelector("#genres")
    values.forEach(value => {
        const inputBox = document.createElement("div")
        inputBox.classList.add("genre_class")

        const input = document.createElement("input")
        input.name = "genre"
        input.id = value
        input.value = value
        input.type = "checkbox"

        const label = document.createElement("label")
        label.htmlFor = value
        label.innerText = value

        inputBox.appendChild(input)
        inputBox.appendChild(label)
        genreContainer.appendChild(inputBox)
    })
}

function createLang(values, index) {
    const selector = document.querySelector("#language")
    values.forEach((value, idx) => {
        const longFlag = index[idx]
        const fullTerm = `${value} (${longFlag})`

        const spanBox = document.createElement("option")
        spanBox.classList.add(`lang`)
        spanBox.value = value
        spanBox.innerText = fullTerm
        selector.insertBefore(spanBox, selector.children[0])
    })
}

function createPeriod(e) {
    const selector = document.querySelector("#period")
    e.forEach((item, idx) => {
        const periodBox = document.createElement("div")
        periodBox.classList.add("period_class")
        const input = document.createElement("input")
        input.name = "period"
        input.id = item
        input.value = idx
        input.type = "radio"

        const label = document.createElement("label")
        label.htmlFor = item
        label.innerText = item

        periodBox.appendChild(input)
        periodBox.appendChild(label)
        selector.appendChild(periodBox)
    })
}

function createPoster() {
    const imageBox = document.querySelector("#image")
    let img = document.createElement("img")
    img.src = "https://image.tmdb.org/t/p/w220_and_h330_face"
    img.alt = "Poster Image"

    imageBox()
}


createGenres(genresList.sort())
createLang(langList.reverse(), fullList.reverse())
createPeriod(periodList)

