Feature: Consultar e utilizar o gestor de tarefas sem iniciar sessão

Scenario: Apresentar as três tarefas iniciais
  Given que existem as três tarefas iniciais
  When abro a página "Lista de tarefas"
  Then vejo a tarefa "Rever requisitos" com prioridade "Alta"
  And vejo a tarefa "Preparar demonstração" com prioridade "Média"
  And vejo a tarefa "Enviar relatório semanal" com prioridade "Baixa"
  And a tarefa "Enviar relatório semanal" está assinalada