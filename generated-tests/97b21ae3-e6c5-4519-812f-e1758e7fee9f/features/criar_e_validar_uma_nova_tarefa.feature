Feature: Criar e validar uma nova tarefa
@XTW-73
Scenario: Guardar uma nova tarefa com data limite válida
Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
When a página é apresentada
And o utilizador seleciona a ligação "Nova tarefa"
Then a página "Nova tarefa" é apresentada
When o utilizador preenche o campo "Título" com "Preparar relatório"
And seleciona "Alta" na lista de seleção "Prioridade"
And preenche o campo "Data limite" com "2099-12-31"
And seleciona o botão "Guardar"
Then a página "Lista de tarefas" é apresentada
And a tarefa "Preparar relatório" é apresentada na coluna "Tarefa"
And a tarefa apresenta "Alta" na coluna "Prioridade"
And a tarefa apresenta "2099-12-31" na coluna "Data limite"