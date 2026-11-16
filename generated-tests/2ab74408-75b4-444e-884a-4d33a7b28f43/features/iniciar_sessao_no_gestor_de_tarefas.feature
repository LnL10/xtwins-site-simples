Feature: Iniciar sessão no gestor de tarefas

Scenario: Iniciar sessão com o e-mail em maiúsculas
  Given que abro a página "Iniciar sessão"
  When preencho o campo "Email" com "ANA.SILVA@EXAMPLE.COM" na página "Iniciar sessão"
  And preencho o campo "Password" com a palavra-passe da utilizadora Ana Silva na página "Iniciar sessão"
  And seleciono o botão "Entrar" na página "Iniciar sessão"
  Then a página "Lista de tarefas" é apresentada