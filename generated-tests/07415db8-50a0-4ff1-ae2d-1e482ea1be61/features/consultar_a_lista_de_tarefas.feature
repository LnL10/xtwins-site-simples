Feature: Consultar a lista de tarefas

@XTW-40
Scenario: Consultar tarefas sem iniciar sessão
  Given estou na página "Iniciar sessão"
  When seleciono "Continuar sem sessão"
  Then é apresentada a página "Lista de tarefas"
  And são apresentadas três tarefas, cada uma com a respetiva prioridade, data-limite e uma caixa de verificação que indica o estado
  And é indicada a existência de "2 tarefas por fazer"