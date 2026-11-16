# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Um navegador novo apresenta as mesmas três tarefas iniciais (`features/guardar_os_dados_das_tarefas_no_navegador.feature`)
- Criar uma tarefa válida sem data limite (`features/criar_uma_tarefa.feature`)
- Consultar e escolher as opções de prioridade (`features/criar_uma_tarefa_2.feature`)

## Cenários saltados

- Marcar uma tarefa por fazer como concluída: A verificação «a indicação apresenta "2 tarefas por fazer"» depende do número de tarefas por fazer que já existe antes do teste, mas esse estado inicial não é definido nos passos. Assim, o resultado esperado não fica garantido.
- Iniciar sessão com um email que difere apenas na capitalização: elemento não localizado: Given que estou na página "Iniciar sessão" e tenho credenciais válidas para a conta de teste
- Submeter credenciais incorretas: elemento não localizado: Given que estou na página "Iniciar sessão" e introduzo credenciais incorretas
- Submeter o formulário de início de sessão vazio: elemento não localizado: Given que estou na página "Iniciar sessão" e deixo os campos vazios
- Continuar sem sessão e regressar à lista de tarefas: elemento não localizado: Given que estou na página "Iniciar sessão"
- Iniciar sessão com credenciais corretas: elemento não localizado: Given que estou na página "Iniciar sessão"
- Utilizar a aplicação sem iniciar sessão: elemento não localizado: Then regresso à página "Lista de tarefas" e vejo a tarefa "Preparar relatório" sem criar uma conta nem iniciar sessão
- A tarefa criada permanece disponível no mesmo navegador: elemento não localizado: Then regresso à página "Lista de tarefas" e vejo a tarefa "Preparar relatório" sem criar uma conta nem iniciar sessão
- Impedir a criação de uma tarefa com um título demasiado longo: elemento não localizado: Then é apresentado um erro de validação e a tarefa não é criada
- Impedir a criação de uma tarefa com o título vazio: elemento não localizado: Then é apresentado um erro de validação e a tarefa não é criada
- Impedir a criação de uma tarefa com um título demasiado curto: elemento não localizado: Then é apresentado um erro de validação e a tarefa não é criada
- Apresentar em conjunto todos os erros de validação: elemento não localizado: Then são apresentados em conjunto os erros de validação dos campos "Título" e "Data limite", e a tarefa não é criada
- Impedir a criação de uma tarefa com uma data limite anterior a hoje: elemento não localizado: Then é apresentado um erro de validação e a tarefa não é criada
- Cancelar o preenchimento de uma nova tarefa: elemento não localizado: Then regresso à página "Lista de tarefas" e não vejo a tarefa "Preparar relatório"
- Desmarcar uma tarefa concluída: elemento não localizado: Then é apresentada a página "Nova tarefa" com o formulário "Nova tarefa"
- Apagar uma tarefa sem pedir confirmação: elemento não localizado: And é apresentada uma mensagem após a remoção
- Apresentar a mensagem quando não existem tarefas: elemento não localizado: Then vejo a mensagem "Não tem tarefas."
- Terminar sessão e permanecer na página Lista de tarefas: elemento não localizado: Then é apresentada uma mensagem, a sessão termina e continuo na página "Lista de tarefas"
- Redirecionamento para As minhas tarefas ao abrir Iniciar sessão: elemento não localizado: When abro a página "Iniciar sessão"

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
