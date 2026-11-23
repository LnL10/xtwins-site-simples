Feature: Iniciar sessão ou continuar sem sessão

Scenario: Abrir a página de início de sessão a partir da lista de tarefas
  Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
  When a página é apresentada
  And o utilizador seleciona a ligação "Iniciar sessão"
  Then a página "Iniciar sessão" é apresentada
  And o campo "Email" é apresentado
  And o campo "Password" é apresentado
  And o botão "Entrar" é apresentado
  And a ligação "Continuar sem sessão" é apresentada