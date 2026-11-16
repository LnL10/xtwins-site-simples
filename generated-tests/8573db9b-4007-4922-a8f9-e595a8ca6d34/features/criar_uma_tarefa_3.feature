Feature: Criar uma tarefa

Scenario: Abrir o formulário de criação de tarefa
  Given que existem as tarefas "Preparar relatório", "Comprar leite" e "Enviar fatura", com as prioridades "Alta", "Média" e "Baixa", respetivamente, e que "Enviar fatura" está concluída
  When abro a página "Lista de tarefas"
  And seleciono o link "Nova tarefa" na página "Lista de tarefas"
  Then vejo a página "Nova tarefa" e o formulário com o campo "Título", a lista "Prioridade" e o campo "Data limite"