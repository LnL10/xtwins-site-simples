# Gestor de Tarefas: requisitos

Aplicação web onde uma pessoa gere a sua lista de tarefas. Tem três páginas: As minhas tarefas (`tarefas.html`),
Nova tarefa (`nova-tarefa.html`) e Iniciar sessão (`login.html`). O endereço da aplicação (`index.html`) abre a página
As minhas tarefas.

Todas as páginas e funcionalidades estão disponíveis para qualquer visitante, sem conta. A secção 1 descreve uma
funcionalidade opcional e independente das outras; as secções 2 e 3 descrevem o uso por um visitante.

Os dados ficam no browser. Cada browser novo começa sempre com as mesmas três tarefas (RF-08): é esse o estado inicial
de qualquer teste.

## Utilizadores

Visitante: qualquer pessoa, sem sessão. Pode usar toda a aplicação.

| Perfil | Email | Nome |
|---|---|---|
| Utilizador registado | ana.silva@example.com | Ana Silva |

A password é entregue em separado (no xTwins, como credencial do projeto).

## 1. Iniciar sessão (opcional)

**RF-01.** A página Iniciar sessão abre-se pela ligação "Iniciar sessão" do cabeçalho da página As minhas tarefas. Tem
os campos "Email" e "Password", o botão "Entrar" e a ligação "Continuar sem sessão", que abre As minhas tarefas.

**RF-02.** Com o email e a password corretos, a aplicação abre a página As minhas tarefas, com o nome do utilizador
("Ana Silva") e o botão "Terminar sessão" no cabeçalho, em vez da ligação "Iniciar sessão". O email não distingue
maiúsculas de minúsculas.

**RF-03.** Com algum dos campos vazio, a aplicação mostra "Preencha o email e a password." e fica na página.

**RF-04.** Com um email ou uma password errados, a aplicação mostra "Email ou password incorretos." e fica na página.

**RF-05.** Com sessão iniciada, a página Iniciar sessão abre As minhas tarefas.

**RF-06.** O botão "Terminar sessão" termina a sessão, mostra "Sessão terminada." e o cabeçalho volta a mostrar a
ligação "Iniciar sessão". A página continua a ser As minhas tarefas.

## 2. As minhas tarefas

**RF-07.** A página mostra uma tabela com as colunas Tarefa, Prioridade, Data limite e Ações. A coluna Tarefa tem uma
caixa de verificação com o título da tarefa; a coluna Ações tem o botão "Apagar". Uma tarefa sem data limite mostra "—";
as datas aparecem como dd/mm/aaaa.

**RF-08.** As tarefas iniciais são:

| Título | Prioridade | Data limite | Concluída |
|---|---|---|---|
| Rever requisitos | Alta | — | Não |
| Preparar demonstração | Média | 31/12/2027 | Não |
| Enviar relatório semanal | Baixa | — | Sim |

**RF-09.** Por cima da tabela, um contador mostra quantas tarefas estão por fazer: "1 tarefa por fazer" ou
"N tarefas por fazer". Com as tarefas iniciais mostra "2 tarefas por fazer".

**RF-10.** Marcar a caixa de verificação de uma tarefa marca-a como concluída (o título aparece riscado) e atualiza o
contador. Desmarcar volta a pô-la por fazer.

**RF-11.** O botão "Apagar" de uma tarefa remove-a da tabela, sem pedir confirmação, e mostra "Tarefa apagada.". Sem
tarefas, a página mostra "Não tem tarefas." em vez da tabela.

**RF-12.** O botão "Nova tarefa" abre a página Nova tarefa.

## 3. Nova tarefa

**RF-13.** A página tem o campo "Título", a lista "Prioridade" (Baixa, Média, Alta; por omissão Média), o campo
"Data limite" (opcional), o botão "Guardar" e o botão "Cancelar".

**RF-14.** Validações ao guardar, todas mostradas de uma vez:

| Condição | Mensagem |
|---|---|
| Título vazio | O título é obrigatório. |
| Título com menos de 3 ou mais de 60 caracteres | O título deve ter entre 3 e 60 caracteres. |
| Data limite anterior a hoje | A data limite não pode ser no passado. |

Os espaços no início e no fim do título não contam. Com algum erro, a tarefa não é criada e a página não muda.

**RF-15.** Sem erros, "Guardar" cria a tarefa por fazer, abre a página As minhas tarefas, que a mostra no fim da
tabela, e mostra "Tarefa criada.".

**RF-16.** "Cancelar" volta à página As minhas tarefas sem criar a tarefa.
