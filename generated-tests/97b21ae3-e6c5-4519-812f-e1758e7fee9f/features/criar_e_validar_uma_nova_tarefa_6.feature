Feature: Criar e validar uma nova tarefa
@XTW-78
Scenario: Apresentar a prioridade Média selecionada por predefinição
Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
When a página é apresentada
And o utilizador seleciona a ligação "Nova tarefa"
Then a página "Nova tarefa" é apresentada
And a lista de seleção "Prioridade" apresenta a opção "Média" selecionada