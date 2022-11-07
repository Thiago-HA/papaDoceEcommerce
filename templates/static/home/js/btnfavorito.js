
function activeBtnFav(id) {
    alert('Produto adicionado com sucesso '+ id)
    fetch('/favoritos_add/' + id)

    const nav = document.getElementById('div-fav');
    nav.classList.toggle('active')

    if (nav.classList.contains('active') == true) {
        alterarImagem("icon-favorito","home/img/carrinho_icon.svg");
    }else{
        alterarImagem("icon-favorito","home/img/lupa_icon.png");
    }
    


}

function alterarImagem(id_objeto, caminhoNovaImagem){
    document.getElementById(id_objeto).src = caminhoNovaImagem;
}

