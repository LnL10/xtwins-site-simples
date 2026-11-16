Feature: Criar uma tarefa válida, validar os dados ou cancelar a criação

Scenario Outline: Apresentar a validação para dados inválidos
  Given o utilizador está autenticado como "cliente"
  When seleciono a ligação "Nova tarefa"
  And preencho o campo "Título" com <titulo>
  And preencho o campo "Data limite" com <data_limite>
  And seleciono o botão "Guardar"
  Then é apresentado o campo "Título"
  And é apresentada a página "Nova tarefa"

Examples:
  | titulo                                                           | data_limite  |
  | ""                                                               | ""           |
  | "AB"                                                             | ""           |
  | "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"  | ""           |
  | "Tarefa válida"                                                  | "01/01/2000" |