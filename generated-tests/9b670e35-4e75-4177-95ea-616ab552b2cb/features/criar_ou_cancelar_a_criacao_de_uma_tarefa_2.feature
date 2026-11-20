Feature: Criar ou cancelar a criação de uma tarefa

@XTW-56
Scenario: Criar uma tarefa sem data limite
  Given que acedo à página "Lista de tarefas"
  When a página é apresentada
  Then vejo uma tabela com as colunas "Tarefa", "Prioridade", "Data limite" e "Ações"
  And seleciono a ligação "Nova tarefa"
  Then vejo o formulário "Nova tarefa" na página "Nova tarefa"
  And preencho o campo "Título" com "Rever plano de testes"
  And seleciono a opção "Baixa" no seletor "Prioridade"
  When seleciono o botão "Guardar"
  Then vejo na tabela da página "Lista de tarefas" uma tarefa com prioridade "Baixa" e sem data limite