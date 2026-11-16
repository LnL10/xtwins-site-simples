Feature: Guardar tarefas no navegador

Scenario: As tarefas guardadas ficam disponíveis no navegador
  Given que os dados das tarefas "Rever requisitos", "Preparar demonstração" e "Enviar relatório semanal" estão guardados no navegador, com prioridades "Alta", "Média" e "Baixa", respetivamente, sem datas limite, e que apenas "Enviar relatório semanal" está concluída
  When abro a página "Lista de tarefas"
  Then vejo a tarefa "Rever requisitos" com prioridade "Alta" e data limite "—" na página "Lista de tarefas"
  And a caixa de verificação da tarefa "Rever requisitos" está desmarcada
  And o título "Rever requisitos" não aparece riscado
  And vejo a tarefa "Preparar demonstração" com prioridade "Média" e data limite "—" na página "Lista de tarefas"
  And a caixa de verificação da tarefa "Preparar demonstração" está desmarcada
  And o título "Preparar demonstração" não aparece riscado
  And vejo a tarefa "Enviar relatório semanal" com prioridade "Baixa" e data limite "—" na página "Lista de tarefas"
  And a caixa de verificação da tarefa "Enviar relatório semanal" está marcada
  And o título "Enviar relatório semanal" aparece riscado
  And o resumo apresenta "2 tarefas por fazer"