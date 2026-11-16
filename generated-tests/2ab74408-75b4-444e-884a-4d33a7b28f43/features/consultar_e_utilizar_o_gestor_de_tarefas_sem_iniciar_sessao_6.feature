Feature: Consultar e utilizar o gestor de tarefas sem iniciar sessão

Scenario: Apresentar duas tarefas por fazer
  Given que abro a página "Lista de tarefas"
  When a área "As minhas tarefas" é apresentada
  Then é indicada a existência de "2" tarefas por fazer