Feature: Consultar a lista de tarefas

@XTW-71
Scenario: Consultar uma tarefa na lista
  Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
  When a página é apresentada
  Then a área "As minhas tarefas" é apresentada com a lista de tarefas
  And as colunas "Tarefa", "Prioridade", "Data limite" e "Ações" são apresentadas
  And a indicação de "2 tarefas por fazer" é apresentada