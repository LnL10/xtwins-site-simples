Feature: Guardar os dados das tarefas no navegador

Scenario: Um navegador novo apresenta as mesmas três tarefas iniciais
  Given que utilizo um navegador
  And que acedo ao endereço "https://lnl10.github.io/xtwins-site-simples/tarefas.html"
  When a página "Lista de tarefas" é aberta
  Then são apresentadas as tarefas iniciais e registo os nomes e estados apresentados
  When abro um navegador novo e acedo ao endereço "https://lnl10.github.io/xtwins-site-simples/tarefas.html"
  Then são apresentadas "3" tarefas com os mesmos nomes e estados que no navegador anterior