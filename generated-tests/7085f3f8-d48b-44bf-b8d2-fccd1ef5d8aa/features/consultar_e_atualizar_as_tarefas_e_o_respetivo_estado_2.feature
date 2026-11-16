Feature: Consultar e atualizar as tarefas e o respetivo estado

Scenario: Desmarcar uma tarefa concluída e atualizar o contador
  Given o utilizador está autenticado como "cliente"
  When acedo ao endereço da aplicação
  And é apresentado o título "As minhas tarefas"
  And o contador apresenta "2 tarefas por fazer"
  When desmarco a caixa de verificação da primeira tarefa concluída na tabela da página "Lista de tarefas"
  Then na linha da primeira tarefa concluída da página "Lista de tarefas", a caixa de verificação aparece desmarcada
  And o título da primeira tarefa da tabela aparece sem estar riscado
  And o contador apresenta "3 tarefas por fazer"