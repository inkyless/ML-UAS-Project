
const cardList = document.querySelectorAll("div.card")
const bottomReturn = document.querySelectorAll('#return-button')[1]

if (cardList.length < 5) {
    bottomReturn.style.display = "none"
}
console.log(cardList.length)
console.log(bottomReturn)
