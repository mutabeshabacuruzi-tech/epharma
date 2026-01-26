inputs = window.document.getElementsByTagName('form')

for (let i = 0; i < inputs.length; i++) {
    if(inputs[i].id != 'form-diary'){
        inputs[i].className = "d-flex flex-column"
    }
    for (let a = 0; a < inputs[i].children.length; a++) {
        tag = inputs[i].children[a].tagName
        if (tag === "INPUT" || tag === "SELECT" || tag === "TEXTAREA") {
            inputs[i].children[a].className = 'form-control form-control-sm'
        }
    }
}