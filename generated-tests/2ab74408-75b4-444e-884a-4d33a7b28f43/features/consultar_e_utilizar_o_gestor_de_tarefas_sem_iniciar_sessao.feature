Feature: Consultar e utilizar o gestor de tarefas sem iniciar sessão

Scenario: Mostrar um travessão quando não existe data limite
  Given que a tarefa "Rever requisitos" não tem data limite
  When abro a página "Lista de tarefas"
  Then a data limite da tarefa "Rever requisitos" é apresentada como "—"