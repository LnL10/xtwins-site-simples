Feature: Iniciar a lista com tarefas predefinidas

Scenario: A lista apresenta três tarefas predefinidas
  Given o utilizador está autenticado como "cliente"
  When acedo ao endereço da aplicação
  And é apresentado o título "As minhas tarefas"
  Then a tabela da página "Lista de tarefas" apresenta três tarefas predefinidas