# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Consultar uma tarefa na lista (`features/consultar_a_lista_de_tarefas.feature`)
- Abrir a página de nova tarefa a partir da lista de tarefas (`features/abrir_o_formulario_de_nova_tarefa.feature`)
- Guardar uma nova tarefa com data limite válida (`features/criar_e_validar_uma_nova_tarefa.feature`)
- Impedir a criação de uma tarefa com data limite anterior à data atual (`features/criar_e_validar_uma_nova_tarefa_2.feature`)
- Selecionar cada opção de prioridade disponível (`features/criar_e_validar_uma_nova_tarefa_3.feature`)
- Guardar uma nova tarefa sem data limite (`features/criar_e_validar_uma_nova_tarefa_4.feature`)
- Impedir a criação de uma tarefa com título vazio ou inferior a 3 caracteres (`features/criar_e_validar_uma_nova_tarefa_5.feature`)
- Apresentar a prioridade Média selecionada por predefinição (`features/criar_e_validar_uma_nova_tarefa_6.feature`)
- Impedir a criação de uma tarefa com título superior a 60 caracteres (`features/criar_e_validar_uma_nova_tarefa_7.feature`)
- Cancelar a criação de uma tarefa (`features/cancelar_a_criacao_de_uma_tarefa.feature`)
- Desmarcar uma tarefa concluída (`features/marcar_e_desmarcar_tarefas_como_concluidas.feature`)

## Cenários saltados

- Ver os dados e o estado de uma tarefa: O passo «And existem tarefas na lista» depende de dados previamente existentes, mas não identifica quais as tarefas nem fixa uma forma de as preparar. O browser não pode garantir essa pré-condição apenas com os passos fornecidos.
- Apagar uma tarefa da lista: O passo «And existem tarefas na lista» depende de tarefas previamente existentes, mas não identifica quais dados devem ser preparados. O browser não consegue garantir esta pré-condição sem dados concretos definidos no cenário.
- Marcar uma tarefa como concluída: Não foi possível gerar o código do cenário: The step when 'o utilizador seleciona a ligação "Iniciar sessão"' is defined more than once (steps/login.py and steps/tarefas_login.py)
- Navegar para a página de início de sessão a partir da lista de tarefas: Não foi possível gerar o código do cenário: The step when 'o utilizador seleciona a ligação "Iniciar sessão"' is defined more than once (steps/login.py and steps/tarefas_login.py)
- Continuar sem sessão a partir da página de início de sessão: Não foi possível gerar o código do cenário: The step when 'o utilizador seleciona a ligação "Iniciar sessão"' is defined more than once (steps/login.py and steps/tarefas_login.py)
- Consultar a lista de tarefas sem sessão iniciada: Não foi possível gerar o código do cenário: The step when 'o utilizador seleciona a ligação "Iniciar sessão"' is defined more than once (steps/login.py and steps/tarefas_login.py)
- Submeter credenciais válidas para iniciar sessão: Não foi possível gerar o código do cenário: The step when 'o utilizador seleciona a ligação "Iniciar sessão"' is defined more than once (steps/login.py and steps/tarefas_login.py)

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
