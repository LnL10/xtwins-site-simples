Feature: Consultar e utilizar o gestor de tarefas sem iniciar sessão

Scenario: Consultar a lista de tarefas sem autenticação
  Given que não estou autenticado
  When abro diretamente a página "Lista de tarefas"
  Then a página "Lista de tarefas" é apresentada sem exigir autenticação