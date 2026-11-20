Feature: Criar ou cancelar a criação de uma tarefa

@XTW-58
Scenario: Criar uma tarefa com data limite
  Given que acedo à página "Lista de tarefas"
  When a página é apresentada
  Then vejo uma tabela com as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"
  And seleciono a ligação "Nova tarefa"
  Then vejo o formulário "Nova tarefa" na página "Nova tarefa"
  And preencho o campo "Título" com "Preparar relatório de testes"
  And seleciono a opção "Alta" no seletor "Prioridade"
  And preencho o campo "Data limite" com "2026-12-31"
  When seleciono o botão "Guardar"
  Then vejo na tabela da página "Lista de tarefas" a tarefa "Preparar relatório de testes" com prioridade "Alta" e data limite "2026-12-31"