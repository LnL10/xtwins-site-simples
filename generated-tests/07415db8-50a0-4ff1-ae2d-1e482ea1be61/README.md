# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Consultar tarefas sem iniciar sessão (`features/consultar_a_lista_de_tarefas.feature`)
- Consultar e selecionar as opções de prioridade (`features/criar_uma_tarefa.feature`)
- Criar uma tarefa sem data-limite (`features/criar_uma_tarefa_2.feature`)
- Impedir a gravação de uma tarefa com data-limite no passado (`features/criar_uma_tarefa_3.feature`)
- Impedir a gravação de uma tarefa sem título ou com título fora dos limites (`features/criar_uma_tarefa_4.feature`)
- Criar uma tarefa sem autenticação com título válido (`features/criar_uma_tarefa_5.feature`)

## Cenários saltados

- Nenhum.

## Como correr

```bash
pip install -r requirements.txt
playwright install
APP_URL=https://lnl10.github.io/xtwins-site-simples/ pytest
```

`APP_URL` é o endereço da aplicação a testar; o código lê-o sempre do ambiente.

## Resultados no Xray

Cada cenário dos casos de teste publicados no Xray tem a tag com a chave do teste (`@<chave>`). Corra os testes
gerando o `cucumber.json` e importe-o para o Xray:

```bash
pytest --cucumberjson=cucumber.json
python scripts/import_xray_results.py
```

O script cria uma execução no Xray com os resultados e mostra a sua chave. Só usa a biblioteca padrão do Python;
o caminho do ficheiro pode ser dado como argumento (por omissão `cucumber.json`). Defina estas variáveis de
ambiente (uma API key do Xray Cloud; os valores nunca ficam no pacote):

- `XRAY_CLIENT_ID`
- `XRAY_CLIENT_SECRET`
