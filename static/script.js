let quoteSelect = document.querySelector('.quote');
let authorSelect = document.querySelector('.author');
let yearsSelect = document.querySelector('.year');
let idSelect = document.querySelector('.inputID');
let button = document.getElementById('Get');
let buttonAdd = document.getElementById('Put');
let buttonChange = document.getElementById('Change');
let buttonDelete = document.getElementById('Delete');
let buttonCommit = document.getElementById('Commit');
let changeAuthor = document.querySelector('.changeAuthor');
let changeYear = document.querySelector('.changeYear');
let changeQuote = document.querySelector('.changeQuote');
const url = 'http://127.0.0.1:5000/';

// Запрос GET
button.addEventListener('click', function () {
    buttonCommit.style.display = "none";
    // Передаем id
    fetch(url + 'quotes/' + idSelect.value, {
        method: 'GET'
    })
        // Парсим полученный JSON
        .then(response => response.json())
        .then(data => {
            let nameValue = data['author'];
            let yearValue = data['years'];
            let quoteValue = data['quote'];

            authorSelect.innerHTML = 'Автор: ' + nameValue;
            yearsSelect.innerHTML = 'Годы жизни: ' + yearValue;
            quoteSelect.innerHTML = quoteValue;
        });
})

// Делаем запрос GET для получения данных, которые будем изменять
buttonChange.addEventListener('click', function () {
    buttonCommit.style.display = "inline-block";
    buttonAdd.style.display = "none";
    buttonDelete.style.display = "none";
    fetch(url + 'quotes/' + idSelect.value, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(data => {
            let nameValue = data['author'];
            let yearValue = data['years'];
            let quoteValue = data['quote'];

            changeAuthor.value = nameValue;
            changeQuote.value = quoteValue;
            changeYear.value = yearValue;
        });
})

// Запрос PUT
buttonCommit.addEventListener('click', function () {
    let idValue = idSelect.value;
    let nameValue = changeAuthor.value;
    let yearValue = changeYear.value;
    let quoteValue = changeQuote.value;
    fetch(url + 'quotes/' + idSelect.value, {
        method: "PUT",
        headers: {'Content-Type': 'quotes/json'},
        // Формируем JSON, который будем передавать в теле запроса
        body: JSON.stringify({
            id: idValue, author: nameValue, years: yearValue, quote: quoteValue
        })
    })
        .then(function () {
            console.log(JSON.stringify({id: idValue, author: nameValue, years: yearValue, quote: quoteValue}));
            changeAuthor.value = "";
            changeQuote.value = "";
            changeYear.value = "";
        })
    buttonCommit.style.display = "none";
    buttonAdd.style.display = "inline-block";
    buttonDelete.style.display = "inline-block";
})

// Запрос POST
buttonAdd.addEventListener('click', function () {
    let idValue = idSelect.value;
    let nameValue = changeAuthor.value;
    let yearValue = changeYear.value;
    let quoteValue = changeQuote.value;
    fetch(url + 'quotes', {
        method: "POST",
        headers: {'Content-Type': 'quotes/json'},
        // Формируем JSON, который будем передавать в теле запроса
        body: JSON.stringify({
            id: idValue, author: nameValue, years: yearValue, quote: quoteValue
        })
    })
        .then(function () {
            console.log(JSON.stringify({id: idValue, author: nameValue, years: yearValue, quote: quoteValue}));
            changeAuthor.value = "";
            changeQuote.value = "";
            changeYear.value = "";
        })
})

// Запрос DELETE
buttonDelete.addEventListener('click', function () {
    buttonCommit.style.display = "none";
    fetch(url + 'quotes/' + idSelect.value, {
        method: 'DELETE'
    }).then()
})