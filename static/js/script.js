

const validar = (e) =>{
    boton = document.getElementById('button');
    hide = document.getElementById('hide');
    e.preventDefault();
    let funcion = document.getElementById('funcion').value;
    let a = document.getElementById('a').value;
    let b = document.getElementById('b').value;
    let tol = document.getElementById('tol').value;
    let iter = document.getElementById('iter').value;
    
    if(funcion == '' || a == '' || b == ''|| tol == '' || iter == ''){
        alert('Todos los campos son obligatorios');
        return false;
    }else{
        hide.style.display='block';
        alert('Datos ingresados correctamente');
        return true;
    }
}