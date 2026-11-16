Feature: Criar uma tarefa válida, validar os dados ou cancelar a criação

Scenario: Cancelar a criação e regressar à lista sem criar a tarefa
  Given o utilizador está autenticado como "cliente"
  Then a tabela da página "Lista de tarefas" apresenta três tarefas predefinidas
  When seleciono a ligação "Nova tarefa"
  And seleciono a ligação "Cancelar"
  Then é apresentada a página "Lista de tarefas"
  And a tabela da página "Lista de tarefas" apresenta três tarefas predefinidas