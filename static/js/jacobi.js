window.onload = function () {
    let form = document.getElementById('form-all');
    let solucion = document.getElementById('solucion');
    let iter = document.getElementById('iter');
    let mensaje = document.getElementById('mensaje');

    let tab_soluciones = document.getElementsByClassName('soluciones');
    let resultsTable = document.getElementsByClassName('resultsTable');

    let formData = JSON.parse(sessionStorage.getItem('formData'));
    if (formData) {
        document.getElementById('x0').value = formData.x0;
        document.getElementById('A').value = formData.A;
        document.getElementById('b').value = formData.b;
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

    form.addEventListener('submit', function (e) {
        sessionStorage.clear();
        let x0 = document.getElementById('x0').value;
        let a = document.getElementById('A').value;
        let b = document.getElementById('b').value;
        let tol = document.getElementById('tol').value;
        let niter = document.getElementById('niter').value;
        sessionStorage.setItem('formData', JSON.stringify({
            x0: x0,
            A: a,
            b: b,
            tol: tol,
            niter: niter,
        }));
    });
}