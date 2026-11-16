Feature: Criar uma tarefa

Scenario: Verificar a prioridade média selecionada por predefinição
  Given que existem as tarefas "Preparar relatório", "Comprar leite" e "Enviar fatura", com as prioridades "Alta", "Média" e "Baixa", respetivamente, e que "Enviar fatura" está concluída
  When abro a página "Lista de tarefas"
  And seleciono o link "Nova tarefa" na página "Lista de tarefas"
  Then a opção "Média" está selecionada na lista "Prioridade" da página "Nova tarefa"