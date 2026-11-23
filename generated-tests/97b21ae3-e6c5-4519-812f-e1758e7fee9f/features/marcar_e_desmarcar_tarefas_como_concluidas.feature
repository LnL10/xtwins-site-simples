Feature: Marcar e desmarcar tarefas como concluídas

@XTW-81
Scenario: Desmarcar uma tarefa concluída
  Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
  When a página é apresentada
  Then a área "As minhas tarefas" é apresentada com a lista de tarefas
  When o utilizador seleciona a ligação "Nova tarefa"
  Then a página "Nova tarefa" é apresentada
  When o utilizador preenche o campo "Título" com "Preparar relatório"
  And seleciona "Alta" na lista de seleção "Prioridade"
  And preenche o campo "Data limite" com "2099-12-31"
  And seleciona o botão "Guardar"
  Then a página "Lista de tarefas" é apresentada
  And a tarefa "Preparar relatório" é apresentada na coluna "Tarefa"
  And a caixa de verificação da tarefa "Preparar relatório" não está selecionada
  When o utilizador seleciona a caixa de verificação da tarefa "Preparar relatório"
  Then a caixa de verificação da tarefa "Preparar relatório" está selecionada
  When o utilizador desmarca a caixa de verificação da tarefa "Preparar relatório"
  Then a caixa de verificação da tarefa "Preparar relatório" não está selecionada