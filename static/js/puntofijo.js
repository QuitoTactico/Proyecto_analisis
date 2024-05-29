window.onload = function () {
    let form = document.getElementById('form-all');
    let solucion = document.getElementById('solucion');
    let iter = document.getElementById('iter');
    let mensaje = document.getElementById('mensaje');

    let tab_soluciones = document.getElementsByClassName('soluciones');
    let resultsTable = document.getElementsByClassName('resultsTable');

    let formData = JSON.parse(sessionStorage.getItem('formData'));
    if (formData) {
        document.getElementById('funcion').value = formData.funcion;
        document.getElementById('funcion_g').value = formData.funcion_g;
        document.getElementById('x0').value = formData.x0;
        document.getElementById('tol').value = formData.tol;
        document.getElementById('niter').value = formData.niter;

        // Show the table if form data is present in session storage
        for (let i = 0; i < resultsTable.length; i++) {
            resultsTable[i].style.display = 'table';
        }
        solucion.style.display = 'block';
        iter.style.display = 'block';
        mensaje.style.display = 'block';
        tab_soluciones[0].style.display = 'table';
    }
    console.log(resultsTable);
    console.log(tab_soluciones);
    console.log(formData);

    form.addEventListener('submit', function (e) {
        sessionStorage.clear();
        let funcion = document.getElementById('funcion').value;
        let funcion_g = document.getElementById('funcion_g').value;
        let x0 = document.getElementById('x0').value;
        let tol = document.getElementById('tol').value;
        let niter = document.getElementById('niter').value;
        sessionStorage.setItem('formData', JSON.stringify({
            funcion: funcion,
            funcion_g: funcion_g,
            x0: x0,
            tol: tol,
            niter: niter,
        }));
    });
}