Feature: Criar e validar uma nova tarefa
@XTW-77
Scenario Outline: Impedir a criação de uma tarefa com título vazio ou inferior a 3 caracteres
Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
When a página é apresentada
And o utilizador seleciona a ligação "Nova tarefa"
Then a página "Nova tarefa" é apresentada
When o utilizador preenche o campo "Título" com "<título>"
And seleciona "Média" na lista de seleção "Prioridade"
And seleciona o botão "Guardar"
Then a página "Nova tarefa" continua apresentada
Examples:
| título |
| "" |
| "Ab" |