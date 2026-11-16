Feature: Consultar e utilizar o gestor de tarefas sem iniciar sessão

Scenario: Continuar sem sessão
  Given que abro a página "Iniciar sessão"
  When seleciono "Continuar sem sessão"
  Then a página "Lista de tarefas" é apresentada sem iniciar sessão