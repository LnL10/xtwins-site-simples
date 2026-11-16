Feature: Consultar e atualizar as tarefas e o respetivo estado

Scenario: Marcar uma tarefa como concluída e atualizar o contador
  Given o utilizador está autenticado como "cliente"
  When acedo ao endereço da aplicação
  And é apresentado o título "As minhas tarefas"
  And o contador apresenta "2 tarefas por fazer"
  When seleciono a caixa de verificação da primeira tarefa por fazer na tabela da página "Lista de tarefas"
  Then a primeira linha da tabela da página "Lista de tarefas" apresenta o título da tarefa riscado
  And o contador apresenta "1 tarefa por fazer"