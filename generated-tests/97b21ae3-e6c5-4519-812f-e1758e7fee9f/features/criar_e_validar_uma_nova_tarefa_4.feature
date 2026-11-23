Feature: Criar e validar uma nova tarefa
@XTW-76
Scenario: Guardar uma nova tarefa sem data limite
Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
When a página é apresentada
And o utilizador seleciona a ligação "Nova tarefa"
Then a página "Nova tarefa" é apresentada
When o utilizador preenche o campo "Título" com "Rever requisitos"
And seleciona "Média" na lista de seleção "Prioridade"
And seleciona o botão "Guardar"
Then a página "Lista de tarefas" é apresentada
And a tarefa "Rever requisitos" é apresentada na coluna "Tarefa"
And a tarefa apresenta "Média" na coluna "Prioridade"
And a tarefa "Rever requisitos" é apresentada sem data limite na coluna "Data limite"