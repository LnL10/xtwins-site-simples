Feature: Iniciar sessão ou continuar sem sessão

Scenario: Continuar sem sessão para a lista de tarefas
  Given o utilizador está na página "Iniciar sessão"
  When o utilizador seleciona a ligação "Continuar sem sessão"
  Then a área "As minhas tarefas" é apresentada com a lista de tarefas
  And as colunas "Tarefa", "Prioridade", "Data limite" e "Ações" são apresentadas
  And a indicação de "2 tarefas por fazer" é apresentada