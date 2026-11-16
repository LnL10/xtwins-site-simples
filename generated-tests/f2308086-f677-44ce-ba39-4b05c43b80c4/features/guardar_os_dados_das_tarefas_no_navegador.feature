Feature: Guardar os dados das tarefas no navegador

Scenario: Um navegador novo apresenta as mesmas três tarefas iniciais
  Given que utilizo um navegador novo sem dados guardados
  When acedo à página "Lista de tarefas"
  Then vejo "3" tarefas na tabela da página "Lista de tarefas", na coluna "Tarefa"
  When acedo à página "Lista de tarefas" num segundo navegador novo sem dados guardados
  Then vejo as mesmas "3" tarefas iniciais na coluna "Tarefa" da página "Lista de tarefas" que vi no primeiro navegador