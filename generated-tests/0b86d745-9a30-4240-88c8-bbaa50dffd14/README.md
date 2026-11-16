# Testes automatizados (pytest-bdd + Playwright)

Pacote gerado pelo test-automator: um ficheiro `.feature` por caso de teste, as step definitions em `steps/`,
as páginas e locators em `pages/` e a configuração do browser em `conftest.py`.

## Cenários cobertos

- Apresentar a lista de tarefas e as colunas esperadas (`features/consultar_a_lista_e_atualizar_o_estado_das_tarefas.feature`)
- Um navegador novo apresenta as mesmas três tarefas iniciais (`features/guardar_os_dados_das_tarefas_no_navegador.feature`)
- Verificar a prioridade predefinida e as opções disponíveis (`features/criar_ou_cancelar_a_criacao_de_uma_tarefa.feature`)

## Cenários saltados

- Representar a ausência de data limite: O passo «que uma tarefa não tem data limite» não identifica a tarefa nem garante que exista uma com essa condição. Assim, não é possível preparar os dados necessários para verificar como a data limite é apresentada.
- Apresentar a data limite no formato esperado: O passo «que uma tarefa tem data limite» não identifica a tarefa nem fixa que exista uma tarefa com data limite. Assim, não é possível preparar de forma determinada os dados necessários para verificar o formato apresentado.
- Identificar uma tarefa concluída pelo seu estado: O passo «que uma tarefa está concluída» não identifica qual é a tarefa nem fixa os dados necessários. Assim, não é possível preparar de forma determinística a tarefa a verificar no browser.
- Desmarcar uma tarefa concluída: O passo «que uma tarefa está concluída» não identifica qual tarefa deve estar concluída. Sem essa referência, não é possível preparar e selecionar de forma determinada a tarefa a desmarcar.
- Continuar sem sessão a partir da página de início de sessão: O passo «que uma tarefa está por fazer» não identifica qual tarefa deve existir e estar por fazer. Assim, não é possível preparar com garantia os dados necessários para marcar a caixa de verificação dessa tarefa.
- Os dados das tarefas mantêm-se no mesmo navegador: O passo «que uma tarefa está por fazer» não identifica qual é a tarefa nem fixa os dados necessários para a preparar. Como há mais do que uma tarefa por fazer, não é possível determinar qual caixa de verificação marcar e verificar após a atualização.
- Apagar uma tarefa sem confirmação: O passo «existe uma tarefa na lista» não identifica a tarefa nem fixa os dados necessários para a preparar. Assim, não é possível garantir que o cenário tenha a tarefa necessária para testar a remoção.
- Apagar a última tarefa da lista: O passo «And resta apenas uma tarefa na lista» depende de um estado inicial que não é especificado nem preparado pelos passos. Assim, não é possível garantir no teste que a lista contenha apenas uma tarefa antes de a apagar.
- Iniciar sessão com credenciais corretas: O passo «Then a sessão é iniciada» afirma um estado de sessão, mas não indica qualquer página, mensagem ou elemento visível no browser que permita verificá-lo.
- Marcar uma tarefa como concluída: elemento não localizado: When marco a caixa de verificação da tarefa
- Atualizar o contador de tarefas por fazer: elemento não localizado: When marco a caixa de verificação de uma tarefa por fazer
- Utilizar a lista de tarefas sem sessão iniciada: elemento não localizado: When marco a caixa de verificação da tarefa
- Criar uma tarefa válida sem data limite: elemento não localizado: And a tarefa "Preparar relatório semanal" aparece no fim da tabela
- Impedir a criação com uma data limite anterior a hoje: elemento não localizado: Then é apresentado um erro relativo à data limite no formulário "Nova tarefa"
- Impedir a criação com um título inferior a 3 caracteres: elemento não localizado: Then é apresentado um erro relativo ao título no formulário "Nova tarefa"
- Impedir a criação com um título superior a 60 caracteres: elemento não localizado: Then é apresentado um erro relativo ao título no formulário "Nova tarefa"
- Apresentar simultaneamente todos os erros e impedir a criação: elemento não localizado: Then são apresentados simultaneamente os erros relativos ao título e à data limite no formulário "Nova tarefa"
- Cancelar a criação e regressar à lista de tarefas: elemento não localizado: And a tarefa com o título "Ler documentação" não é apresentada na lista
- Iniciar sessão ignorando maiúsculas e minúsculas no endereço de correio eletrónico: elemento não localizado: Then a sessão é iniciada
- Apresentar uma mensagem de erro e permanecer na página ao submeter credenciais incorretas: elemento não localizado: Then é apresentada uma mensagem de erro
- Redirecionamento para a lista de tarefas com sessão iniciada: elemento não localizado: Then a sessão é iniciada
- Terminar sessão e permanecer na página atual: elemento não localizado: Then a sessão é iniciada

## Como correr

```bash
pip install -r requirements.txt
playwright install
APP_URL=https://lnl10.github.io/xtwins-site-simples/ pytest
```

`APP_URL` é o endereço da aplicação a testar; o código lê-o sempre do ambiente.
