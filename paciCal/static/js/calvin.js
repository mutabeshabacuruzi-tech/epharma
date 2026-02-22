element = window.document.getElementsByTagName('input')
select = window.document.getElementsByTagName('select')
labels = window.document.getElementsByTagName('label')
forms = window.document.getElementsByTagName('form')
textarea = window.document.getElementsByTagName('textarea')
for (let i = 0; i < element.length; i++) {
    element[i].className = "form-control form-control-sm"
    if (element[i].type === 'text' || element[i].type === 'date') {
        element[i].className = "form-control form-control-sm"
    }
    if (element[i].type === 'submit') {
        element[i].className = "form-control form-control-sm btn-submit"
    }
    if (element[i].type === 'checkbox') {
        element[i].className = "form-check-input"
    }
}
for (let i = 0; i < textarea.length; i++) {
    textarea[i].rows = 2
    textarea[i].className = "form-control form-control-sm"
}
for (let i = 0; i < select.length; i++) {
    select[i].className = "form-control form-control-sm"
}
// for (let i = 0; i < labels.length; i++) {
//     labels[i].className = "input-group"
// }
const alert_container = document.getElementById("messages-column")
let alerts = document.getElementsByClassName("alert")
if (alerts && alert_container) {
    if (alert_container.children.length === 0) {
        alert_container.style = "display:none; z-index: 1"
    }
    setInterval(function () {
        setTimeout(function () {
            for (let i = 0; i < alerts.length; i++) {
                alerts[i].remove();
            }
            alert_container.style = "z-index: 0"
        }, 5000)
    }, 2000)
}





// for (let i = 0; i < forms.length; i++) {
//     for (let child = 1; child < forms[i].children.length; child++) {
//         if (forms[i].children[child].children.length > 1) {
//             forms[i].children[child].children[0].className = "input-group-text"
//             forms[i].children[child].className = "input-group input-group-sm"
//         }

//     }
// }

