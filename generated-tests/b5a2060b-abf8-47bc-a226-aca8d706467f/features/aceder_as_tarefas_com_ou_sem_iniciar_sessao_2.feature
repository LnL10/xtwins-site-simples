Feature: Aceder às tarefas com ou sem iniciar sessão

Scenario: Aceder à Lista de tarefas sem sessão iniciada
  Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
  When a página é apresentada
  Then a página "Lista de tarefas" é apresentada sem exigir autenticação