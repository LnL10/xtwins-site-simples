Feature: Criar uma tarefa

@XTW-42
Scenario: Criar uma tarefa sem data-limite
  Given estou na página "Nova tarefa"
  When preencho o campo "Título" com "Organizar arquivo" e seleciono "Guardar"
  Then é apresentada a página "Lista de tarefas"
  And a tarefa "Organizar arquivo" é apresentada na tabela da página "Lista de tarefas" com a coluna "Data limite" vazia