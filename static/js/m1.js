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
            document.getElementById('m').value = formData.m;
            document.getElementById('tol').value = formData.tol;
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
        let funcion = document.getElementById('funcion').value;
        let x0 = document.getElementById('x0').value;
        let m = document.getElementById('m').value;
        let tol = document.getElementById('tol').value;
        let iter = document.getElementById('niter').value;

            sessionStorage.setItem('formData', JSON.stringify({
                funcion: funcion,
                x0:x0,
                m:m,
                tol: tol,
                iter: iter,

            }));
        // If form fields are not empty, show the table
        if (funcion !== '' && a !== '' && b !== '' && tol !== '' && iter !== '') {
            resultsTable.style.display = 'table'; // show the table
        }

    });

    if (!formData) {
        document.getElementById('funcion').value = '';
        document.getElementById('a').value = '';
        document.getElementById('b').value = '';
        document.getElementById('tol').value = '';
        document.getElementById('niter').value = '';
        resultsTable[0].style.display = 'none';
        solucion.style.display = 'none';
        iter.style.display = 'none';
        mensaje.style.display = 'none';
        tab_soluciones[0].display = 'none';
        sessionStorage.clear();
    }
}