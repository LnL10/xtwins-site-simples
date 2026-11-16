Feature: Marcar ou desmarcar tarefas como concluídas

Scenario: Assinalar uma tarefa por fazer como concluída
  Given que não tenho sessão iniciada
  When acedo à página "Lista de tarefas" e assinalo a caixa de verificação da tarefa "Rever requisitos"
  Then a página "Lista de tarefas" continua apresentada e a tarefa "Rever requisitos" fica assinalada sem pedir autenticação