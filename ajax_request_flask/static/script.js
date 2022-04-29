const x = document.querySelector('#x')
const y = document.querySelector('#y')
const form = document.querySelector('form')
const result = document.querySelector('p')
const clear = document.querySelector('#clear')
const URL = '/add'

form.addEventListener('submit', (e) => {

    e.preventDefault()
    x_value = parseInt(x.value)
    y_value = parseInt(y.value)

    let request_options = {
        method: 'POST',
        headers: {
            'content-type':'application/json'
        },
        body: JSON.stringify({x:x_value, y:y_value})
    }
    
    fetch(URL, request_options)
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            result.innerHTML = 
            `
            ${data.Total}
            `
        })
        .catch((err) => {
            console.log('rejected: ', err)
        })
    

})

clear.addEventListener('click', () => {
    result.innerHTML = ""
})