# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Iniciar sessão com credenciais válidas (`features/aceder_as_tarefas_com_ou_sem_iniciar_sessao.feature`)
- Aceder à Lista de tarefas sem sessão iniciada (`features/aceder_as_tarefas_com_ou_sem_iniciar_sessao_2.feature`)
- Continuar sem iniciar sessão (`features/aceder_as_tarefas_com_ou_sem_iniciar_sessao_3.feature`)

## Cenários saltados

- Validar campos obrigatórios vazios: elemento não localizado: Then é apresentada a validação definida para os campos ""Email"" em falta
- Recusar credenciais inválidas: elemento não localizado: Then é apresentada a mensagem "mensagem de erro definida pelo produto"

## Como correr

```bash
pip install -r requirements.txt
playwright install
APP_URL=https://lnl10.github.io/xtwins-site-simples/ pytest
```

`APP_URL` é o endereço da aplicação a testar; o código lê-o sempre do ambiente.

## Segredos

Estas variáveis de ambiente têm de estar definidas ao correr; os valores nunca ficam no pacote.

- `LOGIN_EMAIL`
- `LOGIN_PASSWORD`
