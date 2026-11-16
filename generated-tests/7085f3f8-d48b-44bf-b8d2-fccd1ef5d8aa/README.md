# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Aceder à aplicação e consultar As minhas tarefas (`features/aceder_a_aplicacao_e_gerir_a_sessao.feature`)
- A lista apresenta três tarefas predefinidas (`features/iniciar_a_lista_com_tarefas_predefinidas.feature`)
- Verificar a persistência dos dados das tarefas ao reabrir a aplicação (`features/guardar_os_dados_das_tarefas_no_navegador.feature`)
- Consultar os dados e o formato das datas das tarefas (`features/consultar_e_atualizar_as_tarefas_e_o_respetivo_estado.feature`)
- Desmarcar uma tarefa concluída e atualizar o contador (`features/consultar_e_atualizar_as_tarefas_e_o_respetivo_estado_2.feature`)
- Marcar uma tarefa como concluída e atualizar o contador (`features/consultar_e_atualizar_as_tarefas_e_o_respetivo_estado_3.feature`)
- Apresentar todas as mensagens de validação de uma vez (`features/criar_uma_tarefa_valida_validar_os_dados_ou_cancelar_a_criacao.feature`)
- Cancelar a criação e regressar à lista sem criar a tarefa (`features/criar_uma_tarefa_valida_validar_os_dados_ou_cancelar_a_criacao_2.feature`)
- Apresentar a validação para dados inválidos (`features/criar_uma_tarefa_valida_validar_os_dados_ou_cancelar_a_criacao_3.feature`)
- Verificar as opções e a prioridade predefinida (`features/criar_uma_tarefa_valida_validar_os_dados_ou_cancelar_a_criacao_4.feature`)

## Cenários saltados

- Iniciar sessão com credenciais corretas: O passo «o utilizador está autenticado como "cliente"» pressupõe um estado de autenticação já estabelecido, que não é uma ação nem uma verificação feita no browser. Além disso, contradiz o passo seguinte, que coloca o utilizador na página de início de sessão.
- Abrir a página de início de sessão: O passo «Given o utilizador está autenticado como "cliente"» pressupõe um estado de autenticação, mas não indica uma ação no browser para o estabelecer nem algo visível para o confirmar.
- Ver o título riscado de uma tarefa concluída: O passo «o título de cada tarefa concluída na tabela da página "Lista de tarefas" aparece riscado» depende de existirem tarefas concluídas, mas o cenário não identifica nenhuma nem fixa esse estado. Assim, não é possível preparar os dados necessários para verificar o comportamento.
- Campos vazios ou credenciais incorretas mantêm a página de início de sessão: elemento não localizado: Given estou na página de início de sessão
- Continuar sem sessão para a lista de tarefas: elemento não localizado: And estou na página de início de sessão
- Terminar sessão mantém a página e apresenta Iniciar sessão no cabeçalho: elemento não localizado: And o cabeçalho apresenta a ligação "Iniciar sessão"
- Abrir Iniciar sessão com sessão iniciada conduz à lista de tarefas: elemento não localizado: When abro a ligação "Iniciar sessão"
- Iniciar sessão com um email que difere apenas em maiúsculas e minúsculas: elemento não localizado: And estou na página de início de sessão
- Apresentar a mensagem quando não existem tarefas: elemento não localizado: Then é apresentada a mensagem "Não tem tarefas."
- Apagar uma tarefa sem confirmação: elemento não localizado: Then a tabela da página "Lista de tarefas" apresenta duas tarefas e não é apresentada uma confirmação
- Criar uma tarefa válida e verificar que aparece no fim da tabela: elemento não localizado: And a tabela da página "Lista de tarefas" apresenta a tarefa "Preparar relatório" no fim

## Como correr

```bash
pip install -r requirements.txt
playwright install
APP_URL=https://lnl10.github.io/xtwins-site-simples/ pytest
```

`APP_URL` é o endereço da aplicação a testar; o código lê-o sempre do ambiente.

## Segredos

Estas variáveis de ambiente têm de estar definidas ao correr; os valores nunca ficam no pacote
(`.env.example` lista-as). O login é feito uma vez por sessão de testes, no `conftest.py`, com o utilizador
de teste destas variáveis; os cenários autenticados começam já com sessão.

- `APP_URL`
- `APP_USERNAME`
- `APP_PASSWORD`

A página de login é aberta relativamente à pasta de `APP_URL`, por isso uma aplicação servida sob um
prefixo (`https://servidor/prefixo/`) faz o login no sítio certo; termine `APP_URL` em `/` quando for uma
pasta. Limitação conhecida: as páginas dos cenários são abertas pelo caminho absoluto no servidor, como
na geração, por isso o prefixo do caminho tem de ser o mesmo na geração e na execução.
