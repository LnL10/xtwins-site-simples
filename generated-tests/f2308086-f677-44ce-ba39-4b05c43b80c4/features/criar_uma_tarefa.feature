Feature: Criar uma tarefa

Scenario: Criar uma tarefa válida sem data limite
  Given que sou visitante e não tenho sessão iniciada
  When acedo à página "Lista de tarefas"
  And seleciono a ligação "Nova tarefa"
  Then é apresentada a página "Nova tarefa" com o formulário "Nova tarefa"
  When preencho o campo "Título" com "Preparar relatório" e seleciono "Média" na lista "Prioridade"
  And seleciono o botão "Guardar"
  Then na página "Lista de tarefas", a tarefa "Preparar relatório" aparece no fim da tabela com o estado "por fazer"
  And é apresentada uma mensagem de confirmação