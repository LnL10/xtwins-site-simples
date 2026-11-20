Feature: Criar uma tarefa

@XTW-45
Scenario: Criar uma tarefa sem autenticação com título válido
  Given abro a página "Nova tarefa" sem iniciar sessão
  When preencho o campo "Título" com "Preparar relatório" e seleciono "Guardar"
  Then é apresentada a página "Lista de tarefas"
  And a tarefa "Preparar relatório" é apresentada na página "Lista de tarefas"