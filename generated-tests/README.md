# generated-tests

Pasta onde o **test-automator do xTwins** entrega os pacotes de testes do Gestor de Tarefas (OI-071): cada pedido fica
em `generated-tests/<request_id>/`, numa branch `xtwins/<request_id>-<AAAAMMDDhhmmss>`, com um pull request para `main`.

Os pacotes da Loja Aurora vão para [LnL10/xtwins-github-sandbox](https://github.com/LnL10/xtwins-github-sandbox): cada
app tem o seu repositório, para o CI correr cada pacote contra a app certa.

## Correr um pacote

```bash
cd generated-tests/<pacote>
pip install -r requirements.txt
playwright install chromium
APP_URL=https://lnl10.github.io/xtwins-site-simples/ APP_USERNAME=ana.silva@example.com APP_PASSWORD='Cliente#2026' pytest
```

Cada pacote corre sozinho, a partir da sua pasta (os pacotes não partilham código). `APP_USERNAME` e `APP_PASSWORD`
só são usados pelos pacotes gerados com credencial; os outros ignoram-nos.

## Regras

- Não fazer merge dos PRs do xTwins em `main`, a não ser que se queira que passem a contar como testes existentes
  para a reutilização de passos.
- O workflow **Testes gerados** corre os pacotes alterados em cada PR contra uma cópia local do Gestor de Tarefas. O
  resultado é informativo: a execução dos testes não faz parte do xTwins (OI-005).
