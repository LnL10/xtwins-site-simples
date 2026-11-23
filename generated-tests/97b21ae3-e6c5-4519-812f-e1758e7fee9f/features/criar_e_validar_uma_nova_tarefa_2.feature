Feature: Criar e validar uma nova tarefa
@XTW-74
Scenario: Impedir a criação de uma tarefa com data limite anterior à data atual
Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
When a página é apresentada
And o utilizador seleciona a ligação "Nova tarefa"
Then a página "Nova tarefa" é apresentada
When o utilizador preenche o campo "Título" com "Preparar reunião"
And seleciona "Média" na lista de seleção "Prioridade"
And preenche o campo "Data limite" com "2000-01-01"
And seleciona o botão "Guardar"
Then a página "Nova tarefa" continua apresentada