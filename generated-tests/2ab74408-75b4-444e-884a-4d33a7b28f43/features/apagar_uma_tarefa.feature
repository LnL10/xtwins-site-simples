Feature: Apagar uma tarefa

Scenario: Apagar uma tarefa da lista
Given que existem as três tarefas iniciais
And que abro a página "Lista de tarefas"
When seleciono "Apagar" na tarefa "Rever requisitos" na página "Lista de tarefas"
Then a tarefa "Rever requisitos" deixa de ser apresentada na página "Lista de tarefas"