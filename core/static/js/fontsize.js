const botaoAumentar = document.getElementById("aumentar");
const botaoDiminuir = document.getElementById("diminuir");

const elementosProtegidos = document.querySelectorAll(".font-size-selector *");
const tamanhosOriginais = new Map();

elementosProtegidos.forEach(el => {
  const tamanho = parseFloat(getComputedStyle(el).fontSize);
  if (!isNaN(tamanho)) {
    tamanhosOriginais.set(el, tamanho);
  }
});

function alterarTamanhoFonte(valor) {
  const elementos = document.querySelectorAll("*");

  elementos.forEach(el => {
    const tamanhoFonte = parseFloat(getComputedStyle(el).fontSize);

    if (!isNaN(tamanhoFonte)) {
      el.style.fontSize = (tamanhoFonte + valor) + "px";
    }
  });

  tamanhosOriginais.forEach((tamanho, el) => {
    el.style.fontSize = tamanho + "px";
  });

  const input = document.querySelector(".display-numero");
  input.value = parseInt(input.value || 0) + (valor > 0 ? 1 : -1);
}

const input = document.querySelector(".display-numero");

botaoAumentar.onclick = () => {
  const valorAtual = parseInt(input.value || 0);
  if (valorAtual < 25) {
    alterarTamanhoFonte(1);
  }
};

botaoDiminuir.onclick = () => {
  const valorAtual = parseInt(input.value || 0);
  if (valorAtual > 1) {
    alterarTamanhoFonte(-1);
  }
};
