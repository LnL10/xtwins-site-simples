# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Continuar sem sessão para a lista de tarefas (`features/iniciar_sessao_ou_continuar_sem_sessao.feature`)
- Submeter as credenciais na página de início de sessão (`features/iniciar_sessao_ou_continuar_sem_sessao_2.feature`)
- Abrir a página de início de sessão a partir da lista de tarefas (`features/iniciar_sessao_ou_continuar_sem_sessao_3.feature`)

## Cenários saltados

- Nenhum.

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
