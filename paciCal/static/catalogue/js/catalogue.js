function add_to_chart(sender) {
    let this_sender = document.getElementById(`produit-${sender}`)
    let target = document.getElementById("panier")
    let element_to_add = document.createElement('div')
    element_to_add.className = "col-md-12 p-0 d-flex flex-column"
    element_to_add.innerHTML = `
    <div class="d-flex flex-column flex-md-row flex-wrap">
        <div class="col-md-12 p-md-0 d-flex justify-content-center align-items-stretch mb-1 mt-1">
            <label class="col-md-10 text-dark m-0" for="${sender}">${this_sender.attributes['product-name'].value}</label>
            <div onclick="remove_product_in_chart(${sender})" class="col-md-1 d-flex align-items-center justify-content-center mx-md-2 bg-danger text-white rounded-3">
                <small>X</small>
            </div>
        </div>
        <div class="col-md-12 p-md-0 d-flex flex-column">
            <input type="number" required min="0" placeholder="qte ${this_sender.attributes['product-name'].value}" name="${sender}">
        </div>
    </div>
    `
    element_to_add.id = `product-in-char-${sender}`
    let set_target_children = new Set()
    for(let i = 0; i < target.children.length; i ++){
        set_target_children.add(target.children[i].id)
    }
    if (!set_target_children.has(element_to_add.id)) {
        target.appendChild(element_to_add)
        this_sender.classList.add('selected-product')
    }else{
        alert(`Vous avez déjà choisi ce produi : ${this_sender.attributes['product-name'].value}`)
    }
    
}
function remove_product_in_chart(product_id){
    let this_product_in_chart = document.getElementById(`product-in-char-${product_id}`)
    let this_product = document.getElementById(`produit-${product_id}`)
    if (this_product_in_chart) {
        this_product_in_chart.remove()        
    }
    this_product.classList.remove('selected-product')
}