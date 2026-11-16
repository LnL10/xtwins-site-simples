# xtwins-site-simples

Site **só para testes** do xTwins next-gen: um gestor de tarefas com 3 páginas, para os testes de ponta a ponta
(app-explorer, story-writer, test-designer, test-automator) correrem depressa. A alternativa completa, com 20 páginas,
é a Loja Aurora em [LnL10/xtwins-github-sandbox](https://github.com/LnL10/xtwins-github-sandbox).

Nada aqui é produção: a conta e as tarefas são fictícias e ficam no browser.

**Site:** https://lnl10.github.io/xtwins-site-simples/

## Páginas

| Página | Ficheiro |
|---|---|
| As minhas tarefas | `tarefas.html` (a raiz abre esta) |
| Nova tarefa | `nova-tarefa.html` |
| Iniciar sessão | `login.html` (opcional) |

**Não é preciso credenciais:** todas as páginas funcionam sem sessão. Iniciar sessão é opcional e só mostra o nome no
cabeçalho; serve para testar o fluxo de login do xTwins quando se quiser. Conta: `ana.silva@example.com` /
`Cliente#2026` (a mesma credencial da Loja Aurora).
Cada browser novo começa com 3 tarefas: Rever requisitos, Preparar demonstração e Enviar relatório semanal (concluída).

Requisitos (input do story-writer): [`requirements/requisitos-gestor-tarefas.md`](requirements/requisitos-gestor-tarefas.md)
e o [PDF](requirements/requisitos-gestor-tarefas.pdf), com 16 regras (RF-01 a RF-16).

## Usar no xTwins

```json
{ "app_url": "https://lnl10.github.io/xtwins-site-simples/" }
```

Sem `credential_ref`, o app-explorer e os testes gerados usam o site como visitante.

Os pacotes de testes do Gestor de Tarefas são entregues neste repositório, em [`generated-tests/`](generated-tests):

```json
{ "publish": { "repository": "LnL10/xtwins-site-simples", "base_branch": "main", "mode": "pull_request" },
  "app_url": "https://lnl10.github.io/xtwins-site-simples/" }
```

O token do conector GitHub (`GITHUB_TOKEN`) tem de incluir este repositório (Contents e Pull requests em leitura e
escrita). Cada PR que muda `generated-tests/` corre os pacotes alterados contra uma cópia local do site (workflow
**Testes gerados**).

## Desenvolvimento

```bash
python tools/serve.py                       # http://localhost:8765/xtwins-site-simples/
pip install pytest==9.1.1 playwright==1.64.1 && playwright install chromium
pytest tests                                # contra a cópia local (11 testes, ~6 s)
SITE_URL=https://lnl10.github.io/xtwins-site-simples/ pytest tests   # contra o site publicado
python tools/build_pdf.py                   # regenera o PDF dos requisitos (precisa de markdown)
```

Um push para `main` corre os testes e, se passarem, publica `website/` no GitHub Pages (workflow **Site**).
