const btnfavorito = document.getElementById('btn-favorito');

function activeBtnFav() {
    const div = document.getElementById('div-fav');
    div.classList.toggle('active')

    if (div.classList.contains('active') == true) {
        alterarImagem("icon-favorito",{% static 'home/img/carrinho_icon.svg' %});
    }else{
        alterarImagem("icon-favorito",{% static 'home/img/lupa_icon.png' %});
    }
}

btnfavorito.addEventListener('click', activeBtnFav)
 


function alterarImagem(id_objeto, caminhoNovaImagem){
    document.getElementById(id_objeto).src = caminhoNovaImagem;
}