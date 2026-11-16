Feature: Criar ou cancelar a criação de uma tarefa

Scenario: Aceder ao formulário sem autenticação e verificar os campos predefinidos
  Given que não estou autenticado
  And que abro a página "Lista de tarefas"
  When seleciono a ligação "Nova tarefa" na página "Lista de tarefas"
  Then a página "Nova tarefa" é apresentada
  And estão disponíveis os campos "Título", "Prioridade" e "Data limite" no formulário "Nova tarefa"
  And a opção "Média" está selecionada por predefinição no campo "Prioridade"