Feature: Abrir o formulário de nova tarefa

@XTW-72
Scenario: Abrir a página de nova tarefa a partir da lista de tarefas
  Given o utilizador acede à página "Lista de tarefas" sem sessão iniciada
  When o utilizador seleciona a ligação "Nova tarefa"
  Then a página "Nova tarefa" é apresentada