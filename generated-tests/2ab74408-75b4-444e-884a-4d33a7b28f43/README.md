# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Mostrar um travessão quando não existe data limite (`features/consultar_e_utilizar_o_gestor_de_tarefas_sem_iniciar_sessao.feature`)
- Apresentar as colunas da lista (`features/consultar_e_utilizar_o_gestor_de_tarefas_sem_iniciar_sessao_2.feature`)
- Assinalar uma tarefa sem iniciar sessão (`features/consultar_e_utilizar_o_gestor_de_tarefas_sem_iniciar_sessao_3.feature`)
- Consultar a lista de tarefas sem autenticação (`features/consultar_e_utilizar_o_gestor_de_tarefas_sem_iniciar_sessao_4.feature`)
- Apresentar as três tarefas iniciais (`features/consultar_e_utilizar_o_gestor_de_tarefas_sem_iniciar_sessao_5.feature`)
- Apresentar duas tarefas por fazer (`features/consultar_e_utilizar_o_gestor_de_tarefas_sem_iniciar_sessao_6.feature`)
- Continuar sem sessão (`features/consultar_e_utilizar_o_gestor_de_tarefas_sem_iniciar_sessao_7.feature`)
- Assinalar uma tarefa por fazer como concluída (`features/marcar_ou_desmarcar_tarefas_como_concluidas.feature`)
- Desassinalar uma tarefa concluída (`features/marcar_ou_desmarcar_tarefas_como_concluidas_2.feature`)
- Apagar uma tarefa da lista (`features/apagar_uma_tarefa.feature`)
- Consultar e selecionar as opções de prioridade (`features/criar_ou_cancelar_a_criacao_de_uma_tarefa.feature`)
- Aceder ao formulário sem autenticação e verificar os campos predefinidos (`features/criar_ou_cancelar_a_criacao_de_uma_tarefa_2.feature`)
- Iniciar sessão com o e-mail em maiúsculas (`features/iniciar_sessao_no_gestor_de_tarefas.feature`)
- Apresentação dos campos de início de sessão (`features/iniciar_sessao_no_gestor_de_tarefas_2.feature`)
- Os dados das tarefas mantêm-se guardados no navegador (`features/guardar_os_dados_das_tarefas_no_navegador.feature`)
- As tarefas iniciais são apresentadas num navegador novo (`features/guardar_os_dados_das_tarefas_no_navegador_2.feature`)

## Cenários saltados

- Impedir a criação com uma data limite anterior a hoje: elemento não localizado: Then a tarefa não é criada
- Impedir a criação com o título vazio: elemento não localizado: Then a tarefa não é criada
- Criar uma tarefa sem data limite e verificar que fica no fim da tabela por fazer: elemento não localizado: And a tarefa "Preparar plano de testes" aparece no fim da tabela
- Cancelar a criação da tarefa e regressar à lista: elemento não localizado: And a tarefa "Tarefa a cancelar" não é apresentada na tabela da página "Lista de tarefas"
- Impedir a criação com um título inferior a 3 caracteres após remover espaços exteriores: elemento não localizado: Then a tarefa não é criada
- Impedir a criação com um título superior a 60 caracteres após remover espaços exteriores: elemento não localizado: Then a tarefa não é criada
- Terminar sessão e permanecer na lista de tarefas: elemento não localizado: When termino sessão

## Como correr

```bash
pip install -r requirements.txt
playwright install
APP_URL=https://lnl10.github.io/xtwins-site-simples/ pytest
```

`APP_URL` é o endereço da aplicação a testar; o código lê-o sempre do ambiente.

## Segredos

Estas variáveis de ambiente têm de estar definidas ao correr; os valores nunca ficam no pacote.

- `LOGIN_PASSWORD`
