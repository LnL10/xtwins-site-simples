Feature: Criar uma tarefa

@XTW-44
Scenario Outline: Impedir a gravação de uma tarefa sem título ou com título fora dos limites
  Given estou na página "Nova tarefa"
  When preencho o campo "Título" com "<título>" e seleciono "Guardar"
  Then continua apresentada a página "Nova tarefa"

Examples:
  | título                                                                                              |
  |                                                                                                     |
  | AB                                                                                                  |
  | Este título ultrapassa claramente o limite máximo de sessenta caracteres definido para uma tarefa nova |