Feature: Criar uma tarefa

Scenario Outline: Selecionar cada opção de prioridade
  Given que existem as tarefas "Preparar relatório", "Comprar leite" e "Enviar fatura", com as prioridades "Alta", "Média" e "Baixa", respetivamente, e que "Enviar fatura" está concluída
  When abro a página "Lista de tarefas"
  And seleciono o link "Nova tarefa" na página "Lista de tarefas"
  And seleciono a opção "<prioridade>" na lista "Prioridade" da página "Nova tarefa"
  Then a opção "<prioridade>" está selecionada na lista "Prioridade" da página "Nova tarefa"

  Examples:
    | prioridade |
    | Baixa      |
    | Média      |
    | Alta       |