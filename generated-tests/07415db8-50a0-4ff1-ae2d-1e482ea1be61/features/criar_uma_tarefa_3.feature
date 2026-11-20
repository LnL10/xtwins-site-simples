Feature: Criar uma tarefa

@XTW-43
Scenario: Impedir a gravação de uma tarefa com data-limite no passado
  Given estou na página "Nova tarefa"
  When preencho o campo "Título" com "Rever documentos" e o campo "Data limite" com "2020-01-01" e seleciono "Guardar"
  Then continua apresentada a página "Nova tarefa"