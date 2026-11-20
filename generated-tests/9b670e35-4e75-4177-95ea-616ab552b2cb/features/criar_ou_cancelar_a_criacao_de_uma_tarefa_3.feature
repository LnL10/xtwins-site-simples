Feature: Criar ou cancelar a criação de uma tarefa

@XTW-57
Scenario: Consultar as opções de prioridade
  Given que acedo à página "Lista de tarefas"
  When a página é apresentada
  Then vejo uma tabela com as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"
  And seleciono a ligação "Nova tarefa"
  Then vejo o formulário "Nova tarefa" na página "Nova tarefa"
  And vejo no seletor "Prioridade" as opções "Baixa", "Média" e "Alta", com "Média" selecionada por predefinição