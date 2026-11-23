Feature: Criar e validar uma nova tarefa
@XTW-75
Scenario Outline: Selecionar cada opção de prioridade disponível
Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
When a página é apresentada
And o utilizador seleciona a ligação "Nova tarefa"
Then a página "Nova tarefa" é apresentada
When o utilizador consulta a lista de seleção "Prioridade"
Then a lista de seleção "Prioridade" apresenta as opções "Baixa", "Média" e "Alta"
When o utilizador seleciona "<prioridade>" na lista de seleção "Prioridade"
Then a lista de seleção "Prioridade" apresenta a opção "<prioridade>" selecionada
Examples:
| prioridade |
| "Baixa" |
| "Média" |
| "Alta" |