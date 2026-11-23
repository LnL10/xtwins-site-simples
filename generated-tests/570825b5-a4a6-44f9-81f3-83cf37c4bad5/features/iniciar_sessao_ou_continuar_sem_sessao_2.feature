Feature: Iniciar sessão ou continuar sem sessão

Scenario: Submeter as credenciais na página de início de sessão
  Given o utilizador está na página "Iniciar sessão"
  When o utilizador preenche o campo "Email" com o email do utilizador
  And preenche o campo "Password" com a palavra-passe do utilizador
  And seleciona o botão "Entrar"
  Then a página "Lista de tarefas" é apresentada