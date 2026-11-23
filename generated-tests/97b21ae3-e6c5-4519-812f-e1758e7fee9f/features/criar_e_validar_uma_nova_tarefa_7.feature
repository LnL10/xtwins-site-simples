Feature: Criar e validar uma nova tarefa
@XTW-79
Scenario: Impedir a criação de uma tarefa com título superior a 60 caracteres
Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
When a página é apresentada
And o utilizador seleciona a ligação "Nova tarefa"
Then a página "Nova tarefa" é apresentada
When o utilizador preenche o campo "Título" com "Título com mais de sessenta caracteres para validar o limite máximo permitido"
And seleciona "Média" na lista de seleção "Prioridade"
And seleciona o botão "Guardar"
Then a página "Nova tarefa" continua apresentada