


var display = document.getElementById(el).style.display;
function esconder(el){
    
    const mudabtn = document.getElementById('id-btn-ocultar')
    const filtro = document.getElementById('filter-colum');

    filtro.classList.toggle('active');
    mudabtn.classList.toggle('mudabtn');
    if(mudabtn.textContent == 'Ocultar Filtros'){
        mudabtn.textContent = 'Filtrar Produtos';
    }else{
        mudabtn.textContent = 'Ocultar Filtros';
    }

  
}



