Feature: Marcar ou desmarcar tarefas como concluídas

Scenario: Desassinalar uma tarefa concluída
  Given que abro a página "Lista de tarefas"
  And a tarefa "Enviar relatório semanal" está assinalada
  When desassinalo a caixa de verificação da tarefa "Enviar relatório semanal"
  Then a tarefa "Enviar relatório semanal" fica por fazer