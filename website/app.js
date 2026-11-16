// Gestor de Tarefas: sem servidor. A sessão e as tarefas ficam no localStorage do browser.
// Um browser novo (ou um contexto novo do Playwright) começa sempre com os mesmos dados.
// A sessão é opcional: todas as páginas funcionam sem ela; com sessão, o cabeçalho mostra o nome.

const CONTA = { email: "ana.silva@example.com", password: "Cliente#2026", nome: "Ana Silva" };
const K_SESSAO = "simples:sessao";
const K_TAREFAS = "simples:tarefas";
const K_AVISO = "simples:aviso";

const TAREFAS_INICIAIS = [
  { id: 1, titulo: "Rever requisitos", prioridade: "Alta", dataLimite: "", concluida: false },
  { id: 2, titulo: "Preparar demonstração", prioridade: "Média", dataLimite: "", concluida: false },
  { id: 3, titulo: "Enviar relatório semanal", prioridade: "Baixa", dataLimite: "", concluida: true },
];

function ler(chave, omissao) {
  try {
    const valor = localStorage.getItem(chave);
    return valor === null ? omissao : JSON.parse(valor);
  } catch (e) {
    return omissao;
  }
}

function gravar(chave, valor) {
  localStorage.setItem(chave, JSON.stringify(valor));
}

function sessao() {
  return ler(K_SESSAO, null);
}

function desenharCabecalho() {
  const atual = sessao();
  document.getElementById("com-sessao").hidden = !atual;
  document.getElementById("sem-sessao").hidden = !!atual;
  if (atual) document.getElementById("utilizador").textContent = atual.nome;
  document.getElementById("terminar-sessao").onclick = () => {
    localStorage.removeItem(K_SESSAO);
    desenharCabecalho();
    const caixa = document.getElementById("aviso");
    caixa.textContent = "Sessão terminada.";
    caixa.hidden = false;
  };
}

function tarefas() {
  return ler(K_TAREFAS, TAREFAS_INICIAIS);
}

function avisar(texto) {
  gravar(K_AVISO, texto);
}

function mostrarAviso() {
  const texto = ler(K_AVISO, null);
  localStorage.removeItem(K_AVISO);
  const caixa = document.getElementById("aviso");
  if (texto && caixa) {
    caixa.textContent = texto;
    caixa.hidden = false;
  }
}

function mostrarErros(lista) {
  const caixa = document.getElementById("erros");
  caixa.innerHTML = "";
  lista.forEach((texto) => {
    const item = document.createElement("li");
    item.textContent = texto;
    caixa.appendChild(item);
  });
  caixa.hidden = lista.length === 0;
}

function hoje() {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
}

function formatarData(iso) {
  if (!iso) return "—";
  const [a, m, d] = iso.split("-");
  return `${d}/${m}/${a}`;
}

// ---- login.html ----

function paginaLogin() {
  if (sessao()) {
    location.replace("tarefas.html");
    return;
  }
  mostrarAviso();
  document.getElementById("form-login").addEventListener("submit", (evento) => {
    evento.preventDefault();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    if (!email || !password) {
      mostrarErros(["Preencha o email e a password."]);
      return;
    }
    if (email.toLowerCase() !== CONTA.email || password !== CONTA.password) {
      mostrarErros(["Email ou password incorretos."]);
      return;
    }
    gravar(K_SESSAO, { email: CONTA.email, nome: CONTA.nome });
    location.href = "tarefas.html";
  });
}

// ---- tarefas.html ----

function paginaTarefas() {
  desenharCabecalho();
  mostrarAviso();
  desenharTarefas();
}

function desenharTarefas() {
  const lista = tarefas();
  const corpo = document.getElementById("lista-tarefas");
  corpo.innerHTML = "";
  lista.forEach((tarefa) => {
    const linha = document.createElement("tr");
    linha.dataset.id = tarefa.id;
    if (tarefa.concluida) linha.className = "concluida";

    const celConcluida = document.createElement("td");
    const caixa = document.createElement("input");
    caixa.type = "checkbox";
    caixa.checked = tarefa.concluida;
    caixa.id = `concluida-${tarefa.id}`;
    caixa.setAttribute("aria-label", `Concluída: ${tarefa.titulo}`);
    caixa.addEventListener("change", () => alterarTarefa(tarefa.id, { concluida: caixa.checked }));
    celConcluida.appendChild(caixa);

    const celTitulo = document.createElement("td");
    celTitulo.textContent = tarefa.titulo;
    const celPrioridade = document.createElement("td");
    celPrioridade.textContent = tarefa.prioridade;
    const celData = document.createElement("td");
    celData.textContent = formatarData(tarefa.dataLimite);

    const celAcoes = document.createElement("td");
    const apagar = document.createElement("button");
    apagar.type = "button";
    apagar.className = "secundario";
    apagar.textContent = "Apagar";
    apagar.setAttribute("aria-label", `Apagar ${tarefa.titulo}`);
    apagar.addEventListener("click", () => apagarTarefa(tarefa.id));
    celAcoes.appendChild(apagar);

    linha.append(celConcluida, celTitulo, celPrioridade, celData, celAcoes);
    corpo.appendChild(linha);
  });

  const porFazer = lista.filter((t) => !t.concluida).length;
  document.getElementById("contador").textContent =
    porFazer === 1 ? "1 tarefa por fazer" : `${porFazer} tarefas por fazer`;
  document.getElementById("tabela-tarefas").hidden = lista.length === 0;
  document.getElementById("sem-tarefas").hidden = lista.length > 0;
}

function alterarTarefa(id, campos) {
  gravar(K_TAREFAS, tarefas().map((t) => (t.id === id ? { ...t, ...campos } : t)));
  desenharTarefas();
}

function apagarTarefa(id) {
  gravar(K_TAREFAS, tarefas().filter((t) => t.id !== id));
  desenharTarefas();
  const caixa = document.getElementById("aviso");
  caixa.textContent = "Tarefa apagada.";
  caixa.hidden = false;
}

// ---- nova-tarefa.html ----

function paginaNovaTarefa() {
  const dataLimite = document.getElementById("data-limite");
  dataLimite.min = hoje();
  document.getElementById("form-tarefa").addEventListener("submit", (evento) => {
    evento.preventDefault();
    const titulo = document.getElementById("titulo").value.trim();
    const prioridade = document.getElementById("prioridade").value;
    const data = dataLimite.value;
    const erros = [];
    if (!titulo) erros.push("O título é obrigatório.");
    else if (titulo.length < 3 || titulo.length > 60) erros.push("O título deve ter entre 3 e 60 caracteres.");
    if (data && data < hoje()) erros.push("A data limite não pode ser no passado.");
    mostrarErros(erros);
    if (erros.length) return;

    const lista = tarefas();
    const id = lista.reduce((maior, t) => Math.max(maior, t.id), 0) + 1;
    lista.push({ id, titulo, prioridade, dataLimite: data, concluida: false });
    gravar(K_TAREFAS, lista);
    avisar("Tarefa criada.");
    location.href = "tarefas.html";
  });
}

const PAGINAS = { login: paginaLogin, tarefas: paginaTarefas, "nova-tarefa": paginaNovaTarefa };
document.addEventListener("DOMContentLoaded", () => {
  PAGINAS[document.body.dataset.pagina]();
  document.body.dataset.ready = "true";
});
