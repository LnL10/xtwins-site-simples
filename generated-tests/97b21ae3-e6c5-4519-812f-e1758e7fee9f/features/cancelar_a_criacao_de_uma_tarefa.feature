Feature: Cancelar a criação de uma tarefa
@XTW-80
Scenario: Cancelar a criação de uma tarefa
Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
When a página é apresentada
Then a indicação de "2 tarefas por fazer" é apresentada
When o utilizador seleciona a ligação "Nova tarefa"
Then a página "Nova tarefa" é apresentada
When o utilizador seleciona o botão "Cancelar"
Then a página "Lista de tarefas" é apresentada
And a indicação de "2 tarefas por fazer" é apresentada