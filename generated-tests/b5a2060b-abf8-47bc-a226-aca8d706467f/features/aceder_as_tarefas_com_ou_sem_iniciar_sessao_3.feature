Feature: Aceder às tarefas com ou sem iniciar sessão

Scenario: Continuar sem iniciar sessão
  Given o utilizador está na página "Iniciar sessão"
  When o utilizador seleciona a ligação "Continuar sem sessão"
  Then a área "As minhas tarefas" é apresentada com a lista de tarefas
  And as colunas "Tarefa", "Prioridade", "Data limite" e "Ações" são apresentadas
  And a indicação de "2 tarefas por fazer" é apresentada