Feature: Criar uma tarefa válida, validar os dados ou cancelar a criação

Scenario: Verificar as opções e a prioridade predefinida
  Given o utilizador está autenticado como "cliente"
  When seleciono a ligação "Nova tarefa"
  Then a seleção "Prioridade" apresenta "Média" selecionada por predefinição
  When seleciono "Baixa" na seleção "Prioridade"
  Then a seleção "Prioridade" apresenta "Baixa" selecionada
  When seleciono "Média" na seleção "Prioridade"
  Then a seleção "Prioridade" apresenta "Média" selecionada
  When seleciono "Alta" na seleção "Prioridade"
  Then a seleção "Prioridade" apresenta "Alta" selecionada