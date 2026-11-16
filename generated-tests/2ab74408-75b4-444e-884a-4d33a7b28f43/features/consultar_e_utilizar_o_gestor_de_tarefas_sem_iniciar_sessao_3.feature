Feature: Consultar e utilizar o gestor de tarefas sem iniciar sessão

Scenario: Assinalar uma tarefa sem iniciar sessão
  Given que não tenho sessão iniciada
  When acedo à página "Lista de tarefas" e assinalo a caixa de verificação da tarefa "Rever requisitos"
  Then a página "Lista de tarefas" continua apresentada e a tarefa "Rever requisitos" fica assinalada sem pedir autenticação