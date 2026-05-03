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

botaoAumentar.onclick = () => alterarTamanhoFonte(1);
botaoDiminuir.onclick = () => alterarTamanhoFonte(-1);