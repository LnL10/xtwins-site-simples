Feature: Consultar e utilizar o gestor de tarefas sem iniciar sessão

Scenario: Apresentar as colunas da lista
  Given que abro a página "Lista de tarefas"
  When a página é apresentada
  Then vejo as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"