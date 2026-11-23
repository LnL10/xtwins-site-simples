Feature: Aceder às tarefas com ou sem iniciar sessão

Scenario: Iniciar sessão com credenciais válidas
  Given o utilizador está na página "Iniciar sessão"
  When o utilizador preenche o campo "Email" com o email do utilizador
  And preenche o campo "Password" com a palavra-passe do utilizador
  And seleciona o botão "Entrar"
  Then a página "Lista de tarefas" é apresentada