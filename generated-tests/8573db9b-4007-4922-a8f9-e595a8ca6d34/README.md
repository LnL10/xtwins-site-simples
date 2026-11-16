# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Selecionar cada opção de prioridade (`features/criar_uma_tarefa.feature`)
- Verificar a prioridade média selecionada por predefinição (`features/criar_uma_tarefa_2.feature`)
- Abrir o formulário de criação de tarefa (`features/criar_uma_tarefa_3.feature`)
- As tarefas guardadas ficam disponíveis no navegador (`features/guardar_tarefas_no_navegador.feature`)
- As tarefas predefinidas são apresentadas num navegador novo (`features/guardar_tarefas_no_navegador_2.feature`)

## Cenários saltados

- A pessoa utilizadora com sessão iniciada é encaminhada para a lista de tarefas: O passo «Given que tenho sessão iniciada» depende de uma sessão já iniciada, mas não especifica o utilizador nem como preparar esse estado. A sessão não é uma ação ou verificação feita no browser descrita pelo cenário.
- Terminar a sessão a partir da lista de tarefas: O passo «Given que tenho sessão iniciada» depende de uma sessão previamente iniciada, mas não especifica o utilizador nem como essa sessão é estabelecida. É uma precondição que o Gherkin não fixa.
- Consultar tarefas por fazer e concluídas: elemento não localizado: And vejo as tarefas "Preparar relatório", "Comprar leite" e "Enviar fatura", cada uma com uma caixa de verificação e um botão "Apagar"
- Consultar uma tarefa sem data limite: elemento não localizado: Then vejo a data limite da tarefa "Organizar secretária" apresentada como "—"
- Consultar a lista sem tarefas: elemento não localizado: Then vejo a mensagem "Não tem tarefas."
- Consultar uma tarefa com data limite: elemento não localizado: Then vejo a data limite da tarefa "Entregar proposta" apresentada como "05/12/2026" no formato dd/mm/aaaa
- Desmarcar uma tarefa concluída: elemento não localizado: And desmarco a caixa de verificação da tarefa "Enviar fatura" na página "Lista de tarefas"
- Marcar uma tarefa por fazer como concluída: elemento não localizado: And marco a caixa de verificação da tarefa "Comprar leite" na página "Lista de tarefas"
- Apagar uma tarefa sem confirmação: elemento não localizado: And seleciono o botão "Apagar" da tarefa "Preparar relatório" na página "Lista de tarefas"
- Impedir a criação de uma tarefa com título vazio: elemento não localizado: And não vejo a mensagem "Tarefa criada."
- Cancelar a criação de uma tarefa: elemento não localizado: And a tarefa "Rascunho de teste" não aparece na lista de tarefas
- Impedir a criação de uma tarefa com título fora do comprimento permitido: elemento não localizado: And não vejo a mensagem "Tarefa criada."
- Criar uma tarefa com dados válidos: elemento não localizado: Then vejo a mensagem "Tarefa criada." na página "Lista de tarefas"
- Impedir a criação de uma tarefa com data limite anterior a hoje: elemento não localizado: And não vejo a mensagem "Tarefa criada."
- Aceder à lista de tarefas sem sessão iniciada: elemento não localizado: And vejo as tarefas "Preparar relatório", "Comprar leite" e "Enviar fatura", cada uma com uma caixa de verificação e um botão "Apagar"
- Abrir a página de início de sessão a partir da lista de tarefas: elemento não localizado: When seleciono "Iniciar sessão" na página "Lista de tarefas"
- A pessoa utilizadora regressa à lista de tarefas com a sessão iniciada: elemento não localizado: When seleciono "Iniciar sessão" na página "Lista de tarefas"
- É apresentada uma mensagem quando o email ou a palavra-passe estão incorretos: elemento não localizado: When seleciono "Iniciar sessão" na página "Lista de tarefas"
- É apresentada uma mensagem quando o email ou a palavra-passe estão vazios: elemento não localizado: When seleciono "Iniciar sessão" na página "Lista de tarefas"
- O email é tratado sem distinção entre maiúsculas e minúsculas: elemento não localizado: When seleciono "Iniciar sessão" na página "Lista de tarefas"

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
