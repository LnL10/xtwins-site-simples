Feature: Guardar os dados das tarefas no navegador

Scenario: As tarefas iniciais são apresentadas num navegador novo
  Given que abro a aplicação num navegador novo
  When abro a página "Lista de tarefas"
  Then vejo a tarefa "Rever requisitos" com prioridade "Alta"
  And vejo a tarefa "Preparar demonstração" com prioridade "Média"
  And vejo a tarefa "Enviar relatório semanal" com prioridade "Baixa"
  And a tarefa "Enviar relatório semanal" está assinalada