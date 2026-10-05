# doc

Central documentation for end users, published at https://eida.github.io/doc/.

Built with [MkDocs](https://www.mkdocs.org/) and
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Preview locally

With [uv](https://docs.astral.sh/uv/):

```bash
uv run --no-project --with-requirements requirements.txt python scripts/fetch_tools.py
uv run --no-project --with-requirements requirements.txt mkdocs serve
```

Then open http://127.0.0.1:8000/doc/. The first command fetches the tool docs;
run it again to pick up changes in the tool repositories.

To check the build the way CI does:

```bash
uv run --no-project --with-requirements requirements.txt mkdocs build
```

The build is strict: broken links, broken anchors and unknown tags fail it.

## How it is organised

| Path | What it is |
|---|---|
| `docs/` | Pages of this site. Page order comes from `.nav.yml` files. |
| `tools.yml` | The list of tools shown under Tools. |
| `scripts/fetch_tools.py` | Copies each tool's docs into `docs/tools/<name>/` and writes the Tools menu and table. |
| `hooks/tools.py` | Points the edit button of tool pages at the tool's own repository. |
| `doc_template/` | Docs folder for tool repositories to copy. |
| `.github/workflows/build.yml` | Builds and deploys the site on push to `main` and every night. |

`docs/tools/` is generated and not committed.

## Add a tool

1. In the tool's repository, copy the template and fill it in:
   `cp -r doc_template my-repo/docs`.
   See the [tool docs template](https://eida.github.io/doc/contributing/tool-docs-template/).
2. Add the tool to `tools.yml` and open a pull request.

## Conventions

- Tags are only `data-user`, `node-operator` and `developer`.
- Dependencies in `requirements.txt` are pinned on purpose. Do not loosen them.
