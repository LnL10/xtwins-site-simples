Feature: Guardar os dados das tarefas no navegador

Scenario: Verificar a persistência dos dados das tarefas ao reabrir a aplicação
  Given o utilizador está autenticado como "cliente"
  And a tabela da página "Lista de tarefas" apresenta três tarefas predefinidas
  When volto a abrir a aplicação no mesmo navegador
  Then a tabela da página "Lista de tarefas" continua a apresentar os mesmos dados de tarefas