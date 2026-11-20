Feature: Criar uma tarefa

@XTW-41
Scenario Outline: Consultar e selecionar as opções de prioridade
  Given estou na página "Nova tarefa"
  Then o campo "Prioridade" apresenta as opções "Baixa", "Média" e "Alta", com "Média" selecionada por predefinição
  When seleciono "<prioridade>" no campo "Prioridade"
  Then o campo "Prioridade" apresenta "<prioridade>" selecionada

Examples:
  | prioridade |
  | Baixa      |
  | Média      |
  | Alta       |