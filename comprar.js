const boton = document.getElementById('comprar')
const etiquetaTexto = document.getElementById('total')

function cambiarTexto() {
    
    etiquetaTexto.innerText = "¡Gracias por su compra!"
    etiquetaTexto.style.color = "green"

}

boton.addEventListener('click', cambiarTexto)