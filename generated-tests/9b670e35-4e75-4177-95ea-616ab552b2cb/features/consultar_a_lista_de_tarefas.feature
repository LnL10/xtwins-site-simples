Feature: Consultar a lista de tarefas

@XTW-54
Scenario: Ver as colunas da tabela de tarefas
  Given que acedo à página "Lista de tarefas"
  When a página é apresentada
  Then vejo uma tabela com as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"