Feature: Aceder à aplicação e gerir a sessão

Scenario: Aceder à aplicação e consultar As minhas tarefas
  Given o utilizador está autenticado como "cliente"
  When acedo ao endereço da aplicação
  Then é apresentada a página "Lista de tarefas"
  And é apresentado o título "As minhas tarefas"