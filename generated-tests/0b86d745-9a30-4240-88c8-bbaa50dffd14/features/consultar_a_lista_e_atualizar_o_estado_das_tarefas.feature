Feature: Consultar a lista e atualizar o estado das tarefas

Scenario: Apresentar a lista de tarefas e as colunas esperadas
  Given que acedo ao endereço "https://lnl10.github.io/xtwins-site-simples/tarefas.html"
  When a página "Lista de tarefas" é aberta
  Then é apresentada a tabela com as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"