Feature: Criar uma tarefa

Scenario: Consultar e escolher as opções de prioridade
  Given que sou visitante e não tenho sessão iniciada
  When acedo à página "Lista de tarefas"
  And seleciono a ligação "Nova tarefa"
  Then é apresentada a página "Nova tarefa" com o formulário "Nova tarefa"
  And a lista "Prioridade" apresenta as opções "Baixa", "Média" e "Alta", com "Média" selecionada por omissão
  When escolho "Baixa" na lista "Prioridade"
  Then a lista "Prioridade" apresenta "Baixa" selecionada
  When escolho "Média" na lista "Prioridade"
  Then a lista "Prioridade" apresenta "Média" selecionada
  When escolho "Alta" na lista "Prioridade"
  Then a lista "Prioridade" apresenta "Alta" selecionada