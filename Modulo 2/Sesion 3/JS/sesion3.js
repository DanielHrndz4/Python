function contar(n,r){
    let i = 0;
    numero = document.getElementById(n)
    respuesta = document.getElementById(r)
    while (i < numero.value){
        console.log(i);
        respuesta.innerHTML += i + '<br>';
        i++;
    }
}
function buscar(b, r){
    respuesta = document.getElementById(r);
    txtBuscar = document.getElementById(b);

    respuesta.innerHTML += txtBuscar.value
}