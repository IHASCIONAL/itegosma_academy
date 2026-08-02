# Itegosma Academy

Repositório de estudos de **estatística e Python**, mantido por três amigos aprendendo juntos.

O conteúdo é publicado como um site com [Zensical](https://zensical.org/), o gerador estático da mesma equipe do Material for MkDocs (lê a configuração no formato `mkdocs.yml` nativamente).

## Rodando o site localmente

Dependências gerenciadas com [uv](https://docs.astral.sh/uv/):

```bash
uv sync --all-groups
uv run zensical serve
```

O site fica disponível em <http://127.0.0.1:8000>.

## Gerando o build estático

```bash
uv run zensical build
```

O resultado vai para a pasta `site/` (ignorada pelo git).

> **Nota:** o projeto já usou o MkDocs + Material for MkDocs. Migramos para o Zensical (ainda em versão `0.0.x`, então esperem instabilidade) porque o MkDocs está sem manutenção há mais de um ano e a equipe do Material anunciou que a versão 2.0 dele vai quebrar compatibilidade com plugins e temas. O Zensical builda nosso `mkdocs.yml` atual sem nenhuma alteração. Uma limitação conhecida: notebooks `.ipynb` embutidos em página (via `mkdocs-jupyter`) ainda não são suportados — por isso eles ficam em `notebooks/`, fora de `docs/`.

## Testes e formatação

Funções de cálculo (em `notebooks/**/probabilidade.py` etc.) têm testes unitários com [pytest](https://docs.pytest.org/), e o código é formatado/lintado com [ruff](https://docs.astral.sh/ruff/):

```bash
uv sync --group dev

uv run task test           # roda os testes
uv run task lint           # verifica lint
uv run task lint-fix       # corrige o que der pra corrigir automaticamente
uv run task format         # formata o código
uv run task format-check   # só verifica formatação, sem alterar
```

Ao adicionar uma função de cálculo nova, adicione o teste correspondente no `test_*.py` da mesma pasta.

## CI/CD

Todo push e pull request para `main` roda automaticamente em [`.github/workflows/ci.yml`](.github/workflows/ci.yml):

- **lint** — `ruff check` + `ruff format --check`
- **test** — `pytest`
- **build-site** — garante que o `zensical build` continua funcionando

Se algum desses falhar, o PR fica sinalizado — é a nossa rede de proteção contra quebrar algo sem perceber.

## Fluxo de trabalho (branch protection)

A `main` é protegida: **ninguém** (nem admin) consegue dar `git push` direto nela, e todo merge exige os 3 checks do CI verdes. Ou seja, todo mundo passa pelo mesmo fluxo:

```bash
git checkout main
git pull
git checkout -b minha-branch-descritiva   # ex: estudo/distribuicao-normal

# ... trabalhe, commite ...

git push -u origin minha-branch-descritiva
gh pr create   # ou pelo site do GitHub
```

Depois:

1. Espere o CI rodar no PR (`gh pr checks --watch` ou aba "Checks" do GitHub).
2. Com os 3 checks verdes, dê merge (`gh pr merge --merge` ou pelo botão no GitHub).
3. Delete a branch (`--delete-branch` no `gh pr merge` já faz isso).
4. Localmente: `git checkout main && git pull`.

Se o CI falhar, rode `uv run task lint`, `uv run task format` e `uv run task test` localmente, corrija e dê push de novo na mesma branch — o PR atualiza sozinho.

## Estrutura

```
docs/
├── index.md                       # Página inicial
├── estatistica/
│   └── probabilidade.md           # Único tópico em andamento até agora
└── assets/                        # CSS e JS customizados
notebooks/
└── estatistica/
    └── probabilidade/             # Scripts/notebooks de trabalho (Estatística)
mkdocs.yml                         # Configuração do site
```

O site é enxuto de propósito: só existe página para o que já foi estudado de verdade. Conforme novos tópicos entrarem (Python, outras frentes de estatística, projetos), criamos o arquivo `.md` em `docs/` e registramos na seção `nav` do `mkdocs.yml` — nada de esqueleto/placeholder adiantado.

A pasta `notebooks/` é a bancada de trabalho: scripts `.py` e notebooks `.ipynb` soltos, usados enquanto se estuda/testa algo, sem compromisso de virar página do site. Quando um estudo amadurecer, resuma o resultado em uma página dentro de `docs/`.
