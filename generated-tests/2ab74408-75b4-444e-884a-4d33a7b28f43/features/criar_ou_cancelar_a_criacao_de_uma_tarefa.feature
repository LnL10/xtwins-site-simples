Feature: Criar ou cancelar a criação de uma tarefa

Scenario: Consultar e selecionar as opções de prioridade
  Given que não estou autenticado
  And que abro a página "Lista de tarefas"
  When seleciono a ligação "Nova tarefa" na página "Lista de tarefas"
  Then a página "Nova tarefa" é apresentada
  When abro o campo "Prioridade" no formulário "Nova tarefa"
  Then estão disponíveis as opções "Baixa", "Média" e "Alta" no campo "Prioridade"
  And seleciono a opção "Baixa" no campo "Prioridade"
  And a opção "Baixa" fica selecionada no campo "Prioridade"
  And seleciono a opção "Média" no campo "Prioridade"
  And a opção "Média" fica selecionada no campo "Prioridade"
  And seleciono a opção "Alta" no campo "Prioridade"
  And a opção "Alta" fica selecionada no campo "Prioridade"