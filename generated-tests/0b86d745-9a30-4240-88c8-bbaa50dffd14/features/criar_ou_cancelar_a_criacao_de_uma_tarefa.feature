Feature: Criar ou cancelar a criação de uma tarefa

Scenario: Verificar a prioridade predefinida e as opções disponíveis
  Given que acedo ao endereço "https://lnl10.github.io/xtwins-site-simples/tarefas.html"
  When a página "Lista de tarefas" é aberta
  And seleciono a ligação "Nova tarefa"
  Then é apresentada a página "Nova tarefa"
  And a opção "Média" está selecionada por predefinição na "seleção de prioridade"
  When seleciono "Baixa" na "seleção de prioridade"
  Then a opção "Baixa" está selecionada na "seleção de prioridade"
  When seleciono "Média" na "seleção de prioridade"
  Then a opção "Média" está selecionada na "seleção de prioridade"
  When seleciono "Alta" na "seleção de prioridade"
  Then a opção "Alta" está selecionada na "seleção de prioridade"