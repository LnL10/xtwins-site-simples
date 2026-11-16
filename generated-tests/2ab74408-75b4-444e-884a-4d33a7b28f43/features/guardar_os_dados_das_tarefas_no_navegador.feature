Feature: Guardar os dados das tarefas no navegador

Scenario: Os dados das tarefas mantêm-se guardados no navegador
  Given que não tenho sessão iniciada
  When acedo à página "Lista de tarefas" e assinalo a caixa de verificação da tarefa "Rever requisitos"
  Then a página "Lista de tarefas" continua apresentada e a tarefa "Rever requisitos" fica assinalada sem pedir autenticação
  When atualizo a página "Lista de tarefas"
  Then a tarefa "Rever requisitos" continua assinalada