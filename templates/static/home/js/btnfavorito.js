const btnfavorito = document.getElementById('btn-favorito');

function activeBtnFav() {
    alert('Produto adicionado com sucesso')

}

function alterarImagem(id_objeto, caminhoNovaImagem){
    document.getElementById(id_objeto).src = caminhoNovaImagem;
}

