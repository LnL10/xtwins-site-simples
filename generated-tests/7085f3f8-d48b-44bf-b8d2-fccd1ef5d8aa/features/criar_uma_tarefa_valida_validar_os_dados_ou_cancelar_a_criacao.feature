Feature: Criar uma tarefa válida, validar os dados ou cancelar a criação

Scenario: Apresentar todas as mensagens de validação de uma vez
  Given o utilizador está autenticado como "cliente"
  When seleciono a ligação "Nova tarefa"
  And preencho o campo "Título" com ""
  And preencho o campo "Data limite" com "01/01/2000"
  And seleciono o botão "Guardar"
  Then é apresentada a página "Nova tarefa"
  And é apresentada a página "Nova tarefa"