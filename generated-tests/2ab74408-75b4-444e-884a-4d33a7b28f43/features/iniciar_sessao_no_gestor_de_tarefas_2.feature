Feature: Iniciar sessão no gestor de tarefas

Scenario: Apresentação dos campos de início de sessão
  Given que abro a página "Iniciar sessão"
  When a página é apresentada
  Then estão disponíveis os campos "Email" e "Password" e o botão "Entrar" na página "Iniciar sessão"