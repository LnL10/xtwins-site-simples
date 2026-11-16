Feature: Consultar e atualizar as tarefas e o respetivo estado

Scenario: Consultar os dados e o formato das datas das tarefas
  Given o utilizador está autenticado como "cliente"
  When acedo ao endereço da aplicação
  And é apresentado o título "As minhas tarefas"
  Then a tabela da página "Lista de tarefas" apresenta, em cada tarefa, o título, o estado, a prioridade e a data limite
  And cada data limite da tabela da página "Lista de tarefas" está no formato "dd/mm/aaaa" ou é apresentada como "-"