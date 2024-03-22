window.onload = function () {
    let form = document.getElementById('form-all');
    let solucion = document.getElementById('solucion');
    let iter = document.getElementById('iter');
    let mensaje = document.getElementById('mensaje');

    //let resultsTable = document.getElementById('resultsTable');
    //let tab_soluciones = document.getElementById('soluciones');
    let tab_soluciones = document.getElementsByClassName('soluciones');
    let resultsTable = document.getElementsByClassName('resultsTable');
    //let tablaprueba1 = document.getElementById('tablaprueba1');

    let formData = JSON.parse(sessionStorage.getItem('formData'));
    if (formData) {
            document.getElementById('funcion').value = formData.funcion;
            document.getElementById('x0').value = formData.x0;
            document.getElementById('dx').value = formData.dx;
            document.getElementById('niter').value = formData.iter;

            resultsTable[0].style.display = 'table'; // show the table
            solucion.style.display = 'block';
            iter.style.display = 'block';
            mensaje.style.display = 'block';
            tab_soluciones[0].style.display = 'table';
    }
    else {
        sessionStorage.clear();
        resultsTable[0].style.display = 'none';
        solucion.style.display = 'none';
        iter.style.display = 'none';
        mensaje.style.display = 'none';
        tab_soluciones[0].style.display = 'none';
    }

    form.addEventListener('submit', function (e) {
        sessionStorage.clear();
        let funcion = document.getElementById('funcion').value;
        let x0 = document.getElementById('x0').value;
        let dx = document.getElementById('dx').value;
        let iter = document.getElementById('niter').value;
            sessionStorage.setItem('formData', JSON.stringify({
                funcion: funcion,
                x0: x0,
                dx: dx,
                iter: iter,

            }));

    });

    if (!formData) {
        document.getElementById('funcion').value = '';
        document.getElementById('x0').value = '';
        document.getElementById('dx').value = '';
        document.getElementById('niter').value = '';
        resultsTable[0].style.display = 'none';
        solucion.style.display = 'none';
        iter.style.display = 'none';
        mensaje.style.display = 'none';
        tab_soluciones[0].display = 'none';
        sessionStorage.clear();
    }
}